from rest_framework.pagination import PageNumberPagination
from . import PaginationHandlerMixin
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class CustomJsonRender(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            response = renderer_context['response']
            msg = "OK"
            code = response.status_code
            error = getattr(response, 'error', None)
            if isinstance(data, dict):
                msg = data.pop('msg', msg)
                code = data.pop('code', code)
                data = data.pop('data', data)
            if isinstance(data, list):
                msg = data[0]
                data = None
            if (code != 200 and code != 201) and data:
                if isinstance(data, dict):
                    msg = data.pop('detail', 'failed')
                if not error:
                    error = [msg]

            # response.status_code = 200
            res = {
                'code': code,
                'msg': msg,
                'data': data,
                'has_error': error is not None,
                'error': error
            }
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    error = []
    if isinstance(response.data, dict):
        for item in response.data:
            error.append(item + " " + str(response.data[item]))
    if isinstance(response.data, list):
        for item in response.data:
            error.append(str(item))
    response.error = error

    return response
