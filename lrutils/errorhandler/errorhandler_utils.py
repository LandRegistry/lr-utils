from flask import Markup, request, render_template, Response
from werkzeug.exceptions import default_exceptions, HTTPException


class ErrorHandler(object):

    def __init__(self, app=None, tasks=None):
        self.tasks = tasks if tasks is not None else [setup_errors]

        if app is not None:
            self.init_app(app)
            
        def __str__(self):
            return repr(self.code)

    def init_app(self, app):
        """Runs each of the tasks added via the :meth:`task` decorator."""

        for task in self.tasks:
            task(app)

    def task(self, func, *args, **kwargs):
        def decorator(f):
            @wraps(f)
            def inner(app):
                return f(app, *args, **kwargs)
            return inner

        if not callable(func) or len(args) > 0 or len(kwargs) > 0:
            def wrapper(func):
                task = decorator(func)
                self.tasks.append(task)
                return task
            return wrapper
        else:
            task = decorator(func)
            self.tasks.append(task)
            return task

def setup_errors(app, error_template="error.html"):
    """Add a handler for each of the available HTTP error responses."""
    def error_handler(error):
        if isinstance(error, HTTPException):
            description = error.get_description(request.environ)
            code = error.code
            name = error.name
        else:
            description = error
            code = 500
            name = "Internal Server Error"
        return render_template(error_template,
                               error=error,
                               code=code,
                               name=Markup(name),
                               description=Markup(description))

    for exception in default_exceptions:
        app.register_error_handler(exception, error_handler)

# Some useful headers to set to beef up the robustness of the app
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
def eh_after_request(response):
    response.headers.add('Content-Security-Policy',
                         "default-src 'self' 'unsafe-inline' data: http://maxcdn.bootstrapcdn.com")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
