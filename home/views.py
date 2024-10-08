from django.shortcuts import render
from trainers.models import TrainerProfile


# Create your views here.
def check_trainer_user_exists(username):
    if TrainerProfile.objects.filter(user=username).exists():
        return True
    return False


def index(request):
    """ A view to retuen the index page """
    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    context = {
       'is_trainer_bool': trainer_bool,
    }
    return render(request, 'home/index.html', context)
