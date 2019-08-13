from django import forms
from userapp.models import User
from issue.models import IssuePriority, Issue


class IssueForm(forms.ModelForm):
    # subject = models.CharField(max_length=50)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by_user")
    # description = models.TextField(max_length=1000)
    # priority = models.ForeignKey(IssuePriority, models.DO_NOTHING, related_name="issue_priority", null=True)
    # project = models.CharField(max_length = 50, null=True, blank=True)
    # status = models.CharField(max_length=20)
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_to_user", default=None, blank = True, null= True)
    # ticketid = models.CharField(max_length=20, null=True, blank=True)
    # issuetype = models.ForeignKey(IssueType, models.DO_NOTHING, related_name="issue_type", null=True)
    # created_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        model = Issue
        fields = ('subject', 'created_by','description', 'priority','project','status', 'assigned_to','ticketid','issuetype')
        widgets = {
            'priority':forms.Select(choices=tuple([(priority.name,priority.name)for priority in IssuePriority.objects.all()])),
            'subject': forms.TextInput,
            'description':forms.Textarea,
        }
    

    # def clean_user(self):
        # if not User.objects.filter(id=self.cleaned_data.get('user')):
        #     self.add_error("user", "Invalid user. Please check the data or login again")
        # return self.cleaned_data
    
    def clean(self):
        pass


class IssuePriorityForm(forms.ModelForm):
    # name = forms.CharField(max_length=50, widget=forms.TextInput)
    class Meta:
        model = IssuePriority
        fields = ('name',)
        widgets = {
            "name": forms.TextInput,
        }

    def clean(self):
        # super().clean()
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            self.errors["name"] = "Name can only contain alphabets"
        return self.cleaned_data
    