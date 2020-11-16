import math


def calculate_mmc(c_value: int, lambda_value: float, mu_value: float):

    data = {}

    data['model_name'] = 'M/M/{}'.format(c_value)

    data['c_value'] = c_value
    data['lambda_value'] = lambda_value
    data['mu_value'] = mu_value

    try:
        data['rho_value'] = lambda_value/(c_value*mu_value)
        data['p0_value'] = 1 / (sum(((lambda_value/mu_value)**n)/math.factorial(n) for n in range(c_value)) +
                                ((lambda_value/mu_value)**c_value/(math.factorial(c_value)*(1-data['rho_value']))))

        data['pc_value'] = data['p0_value'] * \
            (c_value**c_value/math.factorial(c_value)) * \
            (data['rho_value']**c_value)
        data['pq_value'] = data['pc_value']/(1-data['rho_value'])
        data['l_value'] = data['pq_value']*data['rho_value'] / \
            (1-data['rho_value'])+c_value*data['rho_value']
        data['w_value'] = data['l_value']/lambda_value
        data['lq_value'] = data['l_value'] - lambda_value/mu_value
        data['wq_value'] = data['lq_value']/lambda_value

    except:
        return None

    return data


def calculate_mmcc(c_value: int, lambda_value: float, mu_value: float):

    data = {}

    data['model_name'] = 'M/M/{c}/{c}'.format(c=c_value)

    data['c_value'] = c_value
    data['lambda_value'] = lambda_value
    data['mu_value'] = mu_value

    try:
        data['p0_value'] = 1/sum(((lambda_value/mu_value)**n
                                  * (1/math.factorial(n))) for n in range(c_value+1))
        data['pc_value'] = (((lambda_value/mu_value)**c_value)/math.factorial(c_value)) / sum(
            ((lambda_value/mu_value)**i)/math.factorial(i) for i in range(c_value+1))

        data['lambda_prime_value'] = lambda_value * \
            (1 - data['pc_value'])
        data['rho_value'] = data['lambda_prime_value'] / \
            (c_value * mu_value)

        data['lq_value'] = 0
        data['wq_value'] = 0

        data['w_value'] = 1/mu_value
        data['l_value'] = c_value * data['rho_value']

    except:
        return None

    return data


def calculate_mm1k(k_value: int, lambda_value: float, mu_value: float):

    data = {}

    data['model_name'] = 'M/M/1/{}'.format(k_value)

    data['k_value'] = k_value
    data['lambda_value'] = lambda_value
    data['mu_value'] = mu_value

    try:
        if lambda_value == mu_value:
            data['p0_value'] = 1/(k_value + 1)
            data['lambda_prime_value'] = lambda_value * \
                (k_value/(k_value + 1))
            data['rho_value'] = k_value/(k_value+1)
            data['l_value'] = k_value/2
        else:
            data['p0_value'] = (
                1-lambda_value/mu_value)/(1-(lambda_value/mu_value)**(k_value+1))
            data['lambda_prime_value'] = lambda_value * \
                (1-(lambda_value/mu_value) ** k_value) / \
                (1-(lambda_value/mu_value)**(k_value+1))
            data['rho_value'] = lambda_value/mu_value * (1-(lambda_value/mu_value) ** k_value) / \
                (1-(lambda_value/mu_value)**(k_value+1))
            data['l_value'] = data['p0_value'] * \
                sum(n * ((lambda_value/mu_value)**n)
                    for n in range(0, k_value+1))

        data['pk_value'] = data['p0_value'] * \
            ((lambda_value/mu_value)**k_value)

        data['w_value'] = data['l_value'] / \
            data['lambda_prime_value']

        data['wq_value'] = data['w_value'] - (1/mu_value)
        data['lq_value'] = data['l_value'] - data['rho_value']
    except:
        return None

    return data


def calculate_mm1infm(m_value: int, lambda_value: float, mu_value: float):

    data = {}

    data['model_name'] = 'M/M/1/∞/{}'.format(m_value)

    data['m_value'] = m_value
    data['lambda_value'] = lambda_value
    data['mu_value'] = mu_value

    try:
        data['p0_value'] = 1/((sum((math.factorial(m_value)/math.factorial(m_value-n))
                                   * ((lambda_value/mu_value)**n) for n in range(0, m_value+1))))

        data['rho_value'] = 1-data['p0_value']
        data['lambda_prime_value'] = mu_value*data['rho_value']

        data['l_value'] = m_value - (mu_value/lambda_value)*data['rho_value']
        data['w_value'] = (
            m_value/(mu_value*data['rho_value'])) - (1/lambda_value)

        data['wq_value'] = data['w_value'] - 1/mu_value
        data['lq_value'] = data['wq_value']*data['lambda_prime_value']
    except:
        return None

    return data


def calculate_mmcinfm(c_value: int, m_value: int, lambda_value: float, mu_value: float):

    # TODO ALL
    pass
