from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext

from notifications.signals import notify

from pinax.notifications.backends.base import BaseBackend


class DesktopBackend(BaseBackend):
    spam_sensitivity = 2

    def can_send(self, user, notice_type, scoping):
        can_send = super(DesktopBackend, self).can_send(
            user, notice_type, scoping)
        if can_send:
            return True
        return False

    def deliver(self, recipient, sender, notice_type, extra_context):

        print(recipient)
        print(sender)
        print(notice_type)
        print(extra_context)

        notify.send(actor=sender,
                    recipient=[recipient],
                    verb=notice_type.display)
