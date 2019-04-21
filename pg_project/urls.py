from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from pgmanager.views import Room, RoomsView, CreateRooms, RoomDetailsView, AddPeople, ViewPeople, People

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.main_page, name = 'main_page'),

    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),


    path('rooms/new', CreateRooms.as_view(template_name = 'manager/new_room.html'), name='create-room'),
    path('rooms/', RoomsView.as_view(), name='rooms-view'),


    path('people/add', AddPeople.as_view(template_name = 'manager/add_people.html'), name='add-people'),
    path('people/', ViewPeople.as_view(), name='people-view'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)