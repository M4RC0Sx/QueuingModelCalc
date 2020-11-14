from django.db import models
from api.validators import GreaterThanZeroValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class MMCModel(models.Model):

    c_value = models.IntegerField(
        'C', default=1, null=False, validators=[MinValueValidator(1)])
    lambda_value = models.FloatField(
        validators=[GreaterThanZeroValidator], null=False, verbose_name=' λ')
    mu_value = models.FloatField(
        validators=[GreaterThanZeroValidator], null=False, verbose_name=' μ')

    l_value = models.FloatField(
        'L', null=False, validators=[MinValueValidator(0)])
    lq_value = models.FloatField(
        'Lq', null=False, validators=[MinValueValidator(0)])
    w_value = models.FloatField(
        'W', null=False, validators=[MinValueValidator(0)])
    wq_value = models.FloatField(
        'Wq', null=False, validators=[MinValueValidator(0)])
    rho_value = models.FloatField(
        null=False, validators=[MinValueValidator(0)], verbose_name=' ρ')
    p0_value = models.FloatField(
        null=False, default=0, validators=[MinValueValidator(0)], verbose_name=' p0')

    class Meta:
        verbose_name = "MMC Queuing Model"
        verbose_name_plural = "MMC Queuing Models"
        unique_together = (('c_value', 'lambda_value', 'mu_value'), )

    def _validate_lambda(self):
        if self.lambda_value > self.mu_value * self.c_value:
            raise ValidationError("Lambda cannot be greater than C*Mu!")

    def save(self, *args, **kwargs):
        self._validate_lambda()
        return super().save(*args, **kwargs)
