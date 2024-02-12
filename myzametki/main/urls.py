from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('note', views.note, name='note'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
    path('register', views.RegisterUser.as_view(), name='register-user'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.LogoutUser.as_view(), name='logout')
]
