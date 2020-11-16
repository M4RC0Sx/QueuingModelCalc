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
        raise WrongParamsException

    # Check lambda.
    if lambda_value > c_value * mu_value:
        raise WrongParamsException

    # Calculate data.
    mmc_data = calc_utils.calculate_mmc(c_value, lambda_value, mu_value)
    if mmc_data is None:
        raise CalculationErrorException

    data = {
        'status_code': status.HTTP_200_OK,
        'data': mmc_data
    }

    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def MMCCModelView(request):

    # Check that all GET params are present.
    if 'c' not in request.GET or 'lambda' not in request.GET or 'mu' not in request.GET:
        raise MissingParamsException

    # GET params.
    c_value = int(request.GET['c'])
    lambda_value = int(request.GET['lambda'])
    mu_value = int(request.GET['mu'])

    # Check values.
    if c_value < 1 or lambda_value <= 0 or mu_value <= 0:
        raise WrongParamsException

    # Check lambda.
    if lambda_value > c_value * mu_value:
        raise WrongParamsException

    # Calculate data.
    mmcc_data = calc_utils.calculate_mmcc(c_value, lambda_value, mu_value)
    if mmcc_data is None:
        raise CalculationErrorException

    data = {
        'status_code': status.HTTP_200_OK,
        'data': mmcc_data
    }

    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def MM1KModelView(request):

    # Check that all GET params are present.
    if 'k' not in request.GET or 'lambda' not in request.GET or 'mu' not in request.GET:
        raise MissingParamsException()

    # GET params.
    k_value = int(request.GET['k'])
    lambda_value = int(request.GET['lambda'])
    mu_value = int(request.GET['mu'])

    # Check values.
    if k_value < 1 or lambda_value <= 0 or mu_value <= 0:
        raise WrongParamsException

    # Check lambda.
    if lambda_value > k_value * mu_value:
        raise WrongParamsException

    # Calculate data.
    mm1k_data = calc_utils.calculate_mm1k(k_value, lambda_value, mu_value)
    if mm1k_data is None:
        raise CalculationErrorException

    data = {
        'status_code': status.HTTP_200_OK,
        'data': mm1k_data
    }

    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def MM1InfMModelView(request):

    # Check that all GET params are present.
    if 'm' not in request.GET or 'lambda' not in request.GET or 'mu' not in request.GET:
        raise MissingParamsException()

    # GET params.
    m_value = int(request.GET['m'])
    lambda_value = int(request.GET['lambda'])
    mu_value = int(request.GET['mu'])

    # Check values.
    if m_value < 1 or lambda_value <= 0 or mu_value <= 0:
        raise WrongParamsException

    # Check lambda.
    if lambda_value > m_value * mu_value:
        raise WrongParamsException

    # Calculate data.
    mm1infm_data = calc_utils.calculate_mm1infm(
        m_value, lambda_value, mu_value)
    if mm1infm_data is None:
        raise CalculationErrorException

    data = {
        'status_code': status.HTTP_200_OK,
        'data': mm1infm_data
    }

    return Response(data, status=status.HTTP_200_OK)
