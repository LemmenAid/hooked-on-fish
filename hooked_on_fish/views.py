from django.shortcuts import render
from django.core.exceptions import BadRequest, PermissionDenied
from django.http import HttpResponseServerError


def test_error(request):
    raise Exception("Testing 500 error page")  # test 500 error
    # raise BadRequest  # test 400 error
    # raise PermissionDenied  # test 403 error


def bad_request(request, exception):
    """
    Handle 400 Bad Request errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 400 error.

    Returns:
        HttpResponse: A rendered 400 error page with a 400 status code.
    """
    return render(request, 'errors/400.html', status=400)


def permission_denied(request, exception):
    """
    Handle 403 Permission Denied errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 403 error.

    Returns:
        HttpResponse: A rendered 403 error page with a 403 status code.
    """

    return render(request, 'errors/403.html', status=403)


def page_not_found(request, exception):
    """
    Handle 404 Page Not Found errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: A rendered 404 error page with a 404 status code.
    """
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    """
    Handle 500 Internal Server Error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered 500 error page with a 500 status code.
    """
    return render(request, 'erros/500.html', status=500)
