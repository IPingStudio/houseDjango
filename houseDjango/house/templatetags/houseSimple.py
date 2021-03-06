from django import template
from dicts.models import dict
register = template.Library()


@register.simple_tag
def error_msg(error_list):
    if error_list:
        return error_list[0]


@register.filter
def houseAuthority(authority, typeStr):
    returnBoolean = False
    typeStr = typeStr + ''
    userAuth = dict.objects.filter(type__label='用户权限')
    dicID = []
    for userAuthItem in userAuth:
        if '房屋' in userAuthItem.label and typeStr in userAuthItem.label:
            dicID.append(userAuthItem.id)
    for dicIDItem in dicID:
        dicIDItem = str(dicIDItem)
        if dicIDItem in authority:
            returnBoolean = True
            break
    return returnBoolean
