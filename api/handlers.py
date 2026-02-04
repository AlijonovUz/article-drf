from django.http import JsonResponse
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        error_data = response.data

        if isinstance(error_data, dict):
            error_msg = error_data.get('detail', error_data)
        elif isinstance(error_data, str):
            error_msg = error_data
        else:
            error_msg = "Unexpected error"

        return Response({
            "data": None,
            "error": {
                "errorId": response.status_code,
                "isFriendly": True,
                "errorMsg": error_msg,
            },
            "success": False
        }, status=response.status_code)

    return Response({
        "data": None,
        "error": {
            "errorId": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "isFriendly": False,
            "errorMsg": "Internal Server Error",
        },
        "success": False
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def handler404(request, exception, *args, **kwargs):
    return JsonResponse({
        "data": None,
        "error": {
            "errorId": status.HTTP_404_NOT_FOUND,
            "isFriendly": True,
            "errorMsg": "Not Found",
        },
        "success": False
    }, status=status.HTTP_404_NOT_FOUND)


def handler500(request, *args, **kwargs):
    return JsonResponse({
        "data": None,
        "error": {
            "errorId": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "isFriendly": False,
            "errorMsg": "Internal Server Error",
        },
        "success": False
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)