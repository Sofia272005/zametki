from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm, AuthUserForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

def index(request):
    note = Note.objects.filter(user=request.user.id)
    return render(request, 'main/index.html', {'note' : note})

class NoteDetailView(DetailView):
    model = Note
    template_name = 'main/details_view.html'
    context_object_name = 'note'

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'main/note.html'
    form_class = NoteForm

class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/'
    template_name = 'main/note-delete.html'

class LoginUser(LoginView):
    template_name = 'main/login.html'
    form_class = AuthUserForm
    success_url = '/'
    def get_success_url(self):
        return self.success_url

class RegisterUser(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LogoutUser(LogoutView):
    next_page = '/'

def note(request):
    form = NoteForm()
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    data= {
        'form' : form,
        'error' : error
    }

    return render(request, 'main/note.html', data)
