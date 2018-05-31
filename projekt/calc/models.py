from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
import numpy as np

# Create your models here.

class Input(models.Model):
	Title = models.CharField(max_length=100,default='Plot title')
	A = models.CharField(max_length=50,default='1')
	B = models.CharField(max_length=50,default='1')
	V = models.CharField(max_length=50,default='1-np.exp(-p*x)')
	p1 = models.FloatField(default=0.01)
	p2 = models.FloatField(default=1)
	plist = models.CharField(max_length=500,default='0.1,0.2,0.3')
	Nlist = models.CharField(max_length=500,default='50,60')
	Planck_1s=models.BooleanField(default=False)
	Planck_2s=models.BooleanField(default=False)
	Planck_BKP_1s=models.BooleanField(default=False)
	Planck_BKP_2s=models.BooleanField(default=False)
	Planck_BAO_1s=models.BooleanField(default=True)
	Planck_BAO_2s=models.BooleanField(default=True)

class InputForm(ModelForm):
	class Meta:
		model = Input
		fields = '__all__'