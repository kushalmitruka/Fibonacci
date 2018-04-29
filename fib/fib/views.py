from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from fib.utils import return_fibonacci_and_time


class ReturnNthFibonacci(View):
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()

        number = data.get('position_n')

        if number and number.isdigit():
            number = int(number)
            result_value, result_time = return_fibonacci_and_time(number)
            return JsonResponse({'status': 'success', 'result': {'value': result_value, 'time': result_time}})
        return JsonResponse({'status': 'error', 'error_msg': 'Not a valid number'})


class FibonacciPage(TemplateView):
    template_name = 'fibonacci.jinja'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
