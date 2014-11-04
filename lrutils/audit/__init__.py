from flask import request_started, request, session

TEMPLATE = 'Audit: user=[%s], request=[%s], session=[%s], ip_address=[%s], request_url=[%s]'

class Audit(object):

    def __init__(self, app):
        try:
            # check if the client has Flask-Login
            from flask.ext.login import current_user
            request_started.connect(audit_user, app)
        except:
            request_started.connect(audit_anon, app)


def audit_user(sender, **extra):
    from flask.ext.login import current_user
    id = current_user.get_id()

    if id:
        log(sender, current_user, request, session)
    else:
        log(sender, 'anon', request, session)


def audit_anon(sender, **extra):
    log(sender, 'anon', request, session)


def log(sender, who, request, session):
    proxied_remote_addr = _get_remote_addr(request)
    sender.logger.info(TEMPLATE % (who, request, session, proxied_remote_addr, request.url))


def _get_remote_addr(request):
    forwarded_for_ips = request.access_route
    if len(forwarded_for_ips) > 0:
        return forwarded_for_ips[0]
    else:
        return request.remote_addr
