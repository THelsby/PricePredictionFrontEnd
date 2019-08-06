from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from .models import HouseInput
from django.http import Http404
from django.shortcuts import render, get_object_or_404

option = [
    {"MSSubClass": {
        "1-STORY 1946 & NEWER ALL STYLES",
        "1-STORY 1945 & OLDER",
        "1-STORY W/FINISHED ATTIC ALL AGES",
        "1-1/2 STORY - UNFINISHED ALL AGES",
        "1-1/2 STORY FINISHED ALL AGES",
        "2-STORY 1946 & NEWER",
        "2-STORY 1945 & OLDER",
        "2-1/2 STORY ALL AGES",
        "SPLIT OR MULTI-LEVEL",
        "SPLIT FOYER",
        "DUPLEX - ALL STYLES AND AGES",
        "1-STORY PUD (Planned Unit Development) - 1946 & NEWER",
        "1-1/2 STORY PUD - ALL AGES",
        "2-STORY PUD - 1946 & NEWER",
        "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER",
        "2 FAMILY CONVERSION - ALL STYLES AND AGES"
        }
    }
]


def index(request):
    return render(request, 'housePrediction/index.html')


def generateEstimate(request):
    print(request.POST.get("qualityId"))
    return render(request, 'housePrediction/index.html')


def prediction(request, housePrediction_id):
    return HttpResponse("You're looking at house prediction %s." % housePrediction_id)
