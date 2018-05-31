from django.shortcuts import render
from django.template import RequestContext
from .models import *
from .compute import *
import os

# Create your views here.

def index(request):
	os.chdir(os.path.dirname(__file__))
	result = None
	if request.method == 'POST':
		form = InputForm(request.POST)
		ptype = request.POST.get('ptype')
		if form.is_valid():
			form2 = form.save(commit=False)
			result = compute(form2.A, form2.B, form2.V,[form2.Planck_1s,form2.Planck_2s,form2.Planck_BKP_1s,form2.Planck_BKP_2s,form2.Planck_BAO_1s,form2.Planck_BAO_2s],[form2.p1,form2.p2,form2.plist,form2.Nlist],ptype,form2.Title)
	else:
		form = InputForm()
		ptype = 'list'
		result=[None,None,None]
	#for e in result:
	#	print(e)
	return render(request,'calc/index.html',{'check':ptype,'form': form,'resultN': result[0],'resulte': result[1],'resultr': result[2]})