from django import template
register = template.Library()

@register.filter(name="divAdd",is_safe=True)
def divsAdd(value,arg):
    return value+str(arg)

@register.inclusion_tag("result.html")
def show_results(lst):
    return {"choices":lst}