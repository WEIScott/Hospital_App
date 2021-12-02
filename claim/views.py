from django.shortcuts import render
from .models import Claim

# Create your views here.

def ClaimData(request):
	all_claim = Claim.objects.all()
	context = {
		'all_claim_key': all_claim
	}
	return render(request, 'claim/claimdata.html', context)