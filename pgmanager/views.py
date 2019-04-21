from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Rooms, Peoples

class CreateRooms(LoginRequiredMixin, CreateView):
    model = Rooms
    fields = ['room_no', 'floor', 'beds', 'free_beds','rent', 'room_details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def Room(request):
    context = {
        'rooms': Rooms.objects.all()
    }
    return render(request, 'manager/room_view.html', context)

class RoomsView(ListView):
    model = Rooms
    template_name = 'manager/room_view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rooms'


class RoomDetailsView():
    model = Rooms



#People Functions.................
class AddPeople(LoginRequiredMixin, CreateView):
    model = Peoples
    fields = ['room_no', 'floor', 'rent', 'advanced_payment', 'name', 'address', 'date_joined']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
def People(request):
    context = {
        'people': Peoples.objects.all()
    }
    return render(request, 'manager/people_view.html', context)

class ViewPeople(ListView):
    model = Peoples
    template_name = 'manager/people_view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'people'

