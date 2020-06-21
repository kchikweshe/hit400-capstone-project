from django.db import models

# Create your models here.
from django.db import models
from django.core.files import File


# Create your models here.
# class Country(models.Model):
#     name =models.CharField(max_length=60).name
#     control_of_corruption = models.FloatField(max_length=10)
#     political_stability = models.FloatField(max_length=10)
#     rule_of_law = models.FloatField(max_length=10)
#     inflation_rate = models.FloatField(max_length=10)
#     gdp_growth = models.FloatField(max_length=10)
#     ease_of_doing_business = models.FloatField(max_length=10)
#     unemployment_rate = models.FloatField(max_length=10)
#     internet_usage = models.FloatField(max_length=10)
#     literacy_rate = models.FloatField(max_length=10)
#     urban_population = models.FloatField(max_length=10)
#     paying_taxes = models.FloatField(max_length=10)
#     protecting_minority_investors_score = models.FloatField(max_length=10)
#     starting_a_business = models.FloatField(max_length=10)
#     registering_property = models.FloatField(max_length=10)


class CsvFile(models.Model):
    csv_file = File(open('template.csv', 'w'))
    # template_file=File()