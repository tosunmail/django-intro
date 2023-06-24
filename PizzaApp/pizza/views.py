from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request):
    from .models import Pizza
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'home.html', context)


# ------------------------------------
# Class Based Views
# ------------------------------------
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import (
    Order, OrderForm
)

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# ------------------------------
# FixView
# ------------------------------
class FixView:
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    # def get_queryset(self):
    #     return Order.objects.filter(user=self.request.user)
    


# ------------------------------
# Views
# ------------------------------

# List:
class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders'
    order = ['-id']


# Create:
class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        # Mesaj göster:
        messages.success(request, 'Kaydedildi.')
        return super().post(request, *args, **kwargs)


# Detail:
class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'order'


# Update:
class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        # Mesaj göster:
        messages.success(request, 'Güncellendi.')
        return super().post(request, *args, **kwargs)


# Delete:
class OrderDeleteView(FixView, DeleteView):
    
    # template dosyasına gitmeden direkt sil:
    def get(self, request, *args, **kwargs):
        # Mesaj göster:
        messages.success(request, 'Silindi.')
        return super().delete(request, *args, **kwargs)
