__author__ = 'lisa'

from django import template

register = template.Library()

@register.filter
def mapLangName(value):
    if value == "HTML":
        return value.replace("HTML", "markup")
    elif value == "Plain":
        return value.replace("Plain", "none")
    elif value == "Python":
        return value.replace("P", "p")
    elif value == "CSS":
        return value.replace("CSS", "css")
    elif value == "Javascript":
        return value.replace("J", "j")
    elif value == "SQL":
        return value.replace("SQL", "sql")

register.filter('mapLangName', mapLangName)