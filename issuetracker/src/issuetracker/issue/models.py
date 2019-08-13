from django.db import models
from userapp.models import User
# Create your models here.


class IssuePriority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Issue(models.Model):
    subject = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by_user")
    description = models.TextField(max_length=1000)
    priority = models.ForeignKey(IssuePriority, models.DO_NOTHING, related_name="issue_priority", null=True)
    project = models.CharField(max_length = 50, null=True, blank=True)
    status = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_to_user", default=None, blank = True, null= True)
    ticketid = models.CharField(max_length=20, null=True, blank=True)
    issuetype = models.ForeignKey(IssueType, models.DO_NOTHING, related_name="issue_type", null=True)
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Issue: "+ str(self.subject) + " : "+self.user + ":"+self.status


