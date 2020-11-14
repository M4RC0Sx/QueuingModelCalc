from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import math
from api.models import MMCModel
from api.serializers import MMCModelSerializer


@api_view(('GET',))
def MMCModelView(request):

    c_value = int(request.GET['c'])
    lambda_value = int(request.GET['lambda'])
    mu_value = int(request.GET['mu'])

    try:
        mmc = MMCModel.objects.get(
            c_value=c_value, lambda_value=lambda_value, mu_value=mu_value)

    except MMCModel.DoesNotExist:

        if c_value < 1 or lambda_value <= 0 or mu_value <= 0:
            # TODO Return error.
            pass

        if lambda_value > c_value * mu_value:
            # TODO Return error.
            pass

        rho_value = lambda_value/(c_value*mu_value)
        p0_value = 1 / (sum(((lambda_value/mu_value)**n)/math.factorial(n) for n in range(c_value)) +
                        ((lambda_value/mu_value)**c_value/(math.factorial(c_value)*(1-rho_value))))
        pc_value = p0_value * \
            (c_value**c_value/math.factorial(c_value))*(rho_value**c_value)
        pq_value = pc_value/(1-rho_value)
        l_value = pq_value*rho_value/(1-rho_value)+c_value*rho_value
        w_value = l_value/lambda_value
        lq_value = l_value - lambda_value/mu_value
        wq_value = lq_value/lambda_value

        mmc = MMCModel.objects.create(
            c_value=c_value, lambda_value=lambda_value, mu_value=mu_value, l_value=l_value, lq_value=lq_value, w_value=w_value,
            wq_value=wq_value, rho_value=rho_value, p0_value=p0_value)

    serializer = MMCModelSerializer(mmc, context={'request': request})
    return Response(serializer.data)
