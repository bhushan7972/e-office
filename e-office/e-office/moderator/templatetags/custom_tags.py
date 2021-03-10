from django import template
from ..models import notifications, store, store_msg

register = template.Library()

@register.simple_tag
def unread_notifications(uid):

    storedmsg = []
    stored = store.objects.filter(sn=uid)   
    for i in stored:
        storedmsg.append(i.notification_id)    

    return len(storedmsg)    

@register.simple_tag
def unread_msg(uid):

    umsg = []
    smsg = store_msg.objects.filter(sn=uid)
    for i in smsg:
        umsg.append(i.msg_id)
    return len(umsg)

# @register.simple_tag
# def toast_notify(uid):

#     unread = []    
#     un = store.objects.filter(sn=uid)

