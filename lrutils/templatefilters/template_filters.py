from dateutil import parser, tz


def _tz(dt):
    to_zone = tz.gettz('Europe/London')
    dt.replace(tzinfo=to_zone)
    return dt.astimezone(to_zone)


def dateformat(value, format='%-d %B %Y'):
    new_date = parser.parse(value, dayfirst=True)
    return new_date.strftime(format)

def datetimeformat(value, format='%-d %B %Y at %H:%M:%S'):
    norm = parser.parse(value, dayfirst=True)
    bst = _tz(norm)
    return bst.strftime(format)

def currency(value):
    """Format a comma separated  currency to 2 decimal places."""
    return "{:,.2f}".format(float(value))