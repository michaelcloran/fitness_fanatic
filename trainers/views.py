from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.decorators import login_required

from .models import TrainerProfile
from .forms import TrainerProfileForm, AddTrainerUserNameForm

# Create your views here.
@login_required
def add_trainer(request):
    """ used by admin to add a trainer to the system 
    
    Note: I have broken the form into 2 forms
    1. for the allauth User info
    2. for the phone and bio of a trainer linked to the user
        this is for the TrainerProfile
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin Users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        trainer_form = TrainerProfileForm(request.POST)
        trainer_username_form = AddTrainerUserNameForm(request.POST)

        if trainer_form.is_valid() and trainer_username_form.is_valid():
            if username_exists(trainer_username_form.cleaned_data.get('user_name')) == False:
                    username = request.POST.get('user_name')
                    password = request.POST.get('password1')
                    email = request.POST.get('email')
                    firstname = request.POST.get('firstname')
                    lastname = request.POST.get('lastname')
                                        
                    # create user
                    user = User.objects.create_user(username, email, password)
                    user.first_name = firstname
                    user.last_name = lastname
                    user.save()

                    # save the trainer profile form 
                    # remembering to get the user
                    profile = trainer_form.save(commit=False)
                    profile.user = user
                    profile.save()
                    
                    messages.success(request, 'Trainer Profile successfully added')
            else:
                messages.error(request, f"Username {trainer_username_form.cleaned_data.get('username')} already exists!.")
        else:
            messages.error(request, 'Add trainer profile failed. Please ensure the form is valid.')
    else:
        trainer_form = TrainerProfileForm()
        trainer_username_form = AddTrainerUserNameForm()

    template = 'trainers/add_trainer.html'
    context = {
        'trainer_form': trainer_form,
        'trainer_username_form': trainer_username_form,
    }

    return render(request, template, context)

def username_exists(username):
    if User.objects.filter(username=username).exists():
        return True
    
    return False