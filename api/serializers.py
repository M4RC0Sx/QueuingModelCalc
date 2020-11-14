from rest_framework import serializers
from api.models import MMCModel


class MMCModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MMCModel
        fields = ('c_value', 'lambda_value', 'mu_value', 'l_value', 'lq_value',
                  'w_value', 'wq_value', 'rho_value', 'p0_value')
