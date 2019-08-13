from django.shortcuts import render
from issue.models import Issue
from issue.forms import IssueForm, IssuePriorityForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


# Create your views here.
def issue_list(request):
    # return StandardTableView.as_view()(request)
    loggedInUser = str(request.user.username)
    issues = Issue.objects.all()
    return render(request, "issues/list.html",{issues:issues})

def issue_create(request):
    form = IssueForm()
    return render(request, "issues/issue_new.html", {"form":form})


def issuepriority_create(request):
    form = IssuePriorityForm()
    return render(request, "issues/issuepriority_new.html",{"form":form})


def issuepriority_create_post(request):
    form = IssuePriorityForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("issues/priorities/list.html")
    else:
        return render(request, "issues/issuepriority_new.html",{"form":form})
    
    