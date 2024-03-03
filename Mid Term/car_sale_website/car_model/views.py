from django.shortcuts import render, redirect
from . import forms
from . models import CarModel
from user.models import History

from django.views.generic import DetailView
# from django.utils.decorators import method_decorator
# Create your views here.


class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        carmodel = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_model = carmodel
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.object  # post model er object ekhane store krlm
        comments = brand.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def buy_car(reuqest,id):
    car_model = CarModel.objects.get(pk=id)
    user = reuqest.user
    if car_model.car_qty > 0 :
        car_model.car_qty = car_model.car_qty-1
        car_model.save()
        history = History(car_model=car_model,user=user)
        history.save()
    return redirect('car_detail',id = id)
