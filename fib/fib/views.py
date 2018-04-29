from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.conf import settings

from django.core.cache import cache

from fib.utils import return_fibonacci_and_time


class ReturnNthFibonacci(View):
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()

        number = data.get('position_n')

        result = cache.get(number)

        if not result:
            if number and number.isdigit():
                number = int(number)
                result_value, result_time = return_fibonacci_and_time(number)
                result = {'status': 'success', 'result': {'value': result_value, 'time': result_time}}
                cache.set(number, result, settings.CACHE_TIMEOUT)
            else:
                result = {'status': 'error', 'error_msg': 'Not a valid number'}
                cache.set(number, result, settings.CACHE_TIMEOUT)

        return JsonResponse(result)


class FibonacciPage(TemplateView):
    template_name = 'fibonacci.jinja'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
