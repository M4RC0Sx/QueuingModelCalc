import math


def calculate_mmc(c_value: int, lambda_value: float, mu_value: float):

    mmc_data = {}

    mmc_data['model_name'] = 'M/M/{}'.format(c_value)

    mmc_data['c_value'] = c_value
    mmc_data['lambda_value'] = lambda_value
    mmc_data['mu_value'] = mu_value

    try:
        mmc_data['rho_value'] = lambda_value/(c_value*mu_value)
        mmc_data['p0_value'] = 1 / (sum(((lambda_value/mu_value)**n)/math.factorial(n) for n in range(c_value)) +
                                    ((lambda_value/mu_value)**c_value/(math.factorial(c_value)*(1-mmc_data['rho_value']))))

        mmc_data['pc_value'] = mmc_data['p0_value'] * \
            (c_value**c_value/math.factorial(c_value)) * \
            (mmc_data['rho_value']**c_value)
        mmc_data['pq_value'] = mmc_data['pc_value']/(1-mmc_data['rho_value'])
        mmc_data['l_value'] = mmc_data['pq_value']*mmc_data['rho_value'] / \
            (1-mmc_data['rho_value'])+c_value*mmc_data['rho_value']
        mmc_data['w_value'] = mmc_data['l_value']/lambda_value
        mmc_data['lq_value'] = mmc_data['l_value'] - lambda_value/mu_value
        mmc_data['wq_value'] = mmc_data['lq_value']/lambda_value

    except:
        return None

    return mmc_data
