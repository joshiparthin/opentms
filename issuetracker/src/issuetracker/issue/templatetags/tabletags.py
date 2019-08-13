from django import template

register = template.Library()

@register.inclusion_tag('table.html',takes_context =True)
def table_view(context):

    return {
        "headers":["One", "Two", "Three"],
        "rows": [["One", "Two", "Three"],["One", "Two", "Three"]]
    }
    

