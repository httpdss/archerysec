from django.db.models import signals
from django.conf import settings
from django.utils.translation import ugettext_noop as _

if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications.models import NoticeType

    NoticeType.create("scan_started", _(
        "Scan Started"), _("Enable notification when scan has started"))
    NoticeType.create("scan_completed", _(
        "Scan Completed"), _("Enable notification when scan has been completed"))
else:
    print("Skipping creation of NoticeTypes as notification app not found")
