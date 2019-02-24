from sitetree.utils import tree, item

sitetrees = (
    tree('topnavbar', items=[
        item('Notifications <span class"badge live_notify_badge"></span>',
             'notifications:unread',
             access_loggedin=True,
             hint="icon-envelope"),
        item('API Docs',
             'https://developers.archerysec.info',
             url_as_pattern=False,
             hint="icon-link"),
        item('Settings',
             'webscanners:setting',
             access_loggedin=True,
             hint="icon-cog"),
        item('Log Out',
             'webscanners:logout',
             access_loggedin=True,
             hint="icon-share-alt")]),
)
