from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import api.calculation_utils as calc_utils
from .exceptions import MissingParamsException, WrongParamsException, CalculationErrorException


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def MMCModelView(request):

    # Check that all GET params are present.
    if 'c' not in request.GET or 'lambda' not in request.GET or 'mu' not in request.GET:
        raise MissingParamsException()

    # GET params.
    c_value = int(request.GET['c'])
    lambda_value = int(request.GET['lambda'])
    mu_value = int(request.GET['mu'])

    # Check values.
    if c_value < 1 or lambda_value <= 0 or mu_value <= 0:
        raise WrongParamsException()

    # Check lambda.
    if lambda_value > c_value * mu_value:
        raise WrongParamsException()

    # Calculate data.
    mmc_data = calc_utils.calculate_mmc(c_value, lambda_value, mu_value)
    if mmc_data is None:
        raise CalculationErrorException

    data = {
        'status_code': status.HTTP_200_OK,
        'data': mmc_data
    }

    return Response(data, status=status.HTTP_200_OK)
