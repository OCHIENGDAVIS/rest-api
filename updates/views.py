from django.views.generic import View
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Update


def updateTest(request):
    data = {
        'message': 'Welcome to the world of django'
    }
    return JsonResponse(data)


class JsonResponseMixin(object):

    def render_json(self, context, *args, **kwargs):
        return JsonResponse(self.get_data(context), **kwargs)

    def get_data(self, context):
        return context


class UpdateView(JsonResponseMixin, View):

    def get(self, request, *args, **kwargs ):
        data = {
            'message': 'Welcome to the world of django'
        }
        return self.render_json(data)


class SerialisedDetailAPIView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.get(id=1).serialize()
        # data = serialize('json', [qs], fields=('id', 'content'))
        return JsonResponse(qs, safe=False)


class SerialisedListAPIView(View):

    def get(self, request):
        qs = Update.objects.all().serialize()
        # data = serialize('json', qs, fields=('id', 'content'))
        # print(data)
        return JsonResponse(qs, safe=False)




