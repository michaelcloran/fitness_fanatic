from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.decorators import login_required

from .models import TrainerProfile, ContactTrainerRequest
from .forms import (
    TrainerProfileForm,
    AddTrainerUserNameForm,
    ViewTrainerUserNameForm,
    ContactTrainerRequestForm
)
from checkout.models import CustomersEnrolledOnCourse, ClassAttendance
from products.models import WorkoutProgram

from datetime import datetime
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def check_trainer_user_exists(username):
    if TrainerProfile.objects.filter(user=username).exists():
        return True
    return False


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
        trainer_form = TrainerProfileForm(request.POST, request.FILES)
        trainer_username_form = AddTrainerUserNameForm(request.POST)

        if trainer_form.is_valid() and trainer_username_form.is_valid():
            t_uname = trainer_username_form.cleaned_data.get('user_name')
            if not username_exists(t_uname):
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

                messages.success(request, 'Trainer Profile '
                                 'successfully added'
                                 )
                return redirect(reverse('trainer_detail',
                                args=[profile.id])
                                )
            else:
                t_str = f"{trainer_username_form.cleaned_data.get('username')}"
                messages.error(request, f"Username "
                               f"{t_str}"
                               " already exists!."
                               )
        else:
            messages.error(request, 'Add trainer profile failed. '
                           'Please ensure the form is valid.'
                           )
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


def view_trainers(request):
    """ gives a list of all trainers """
    trainers = TrainerProfile.objects.all()

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    context = {
        'trainers': trainers,
        'is_trainer_bool': trainer_bool,
    }

    return render(request, 'trainers/view_trainers.html', context)


@login_required
def edit_trainer(request, trainer_id):
    """ Edit a trainer details
    Note:
    I am using 2 forms her one for the allauth User
    and one for the TrainerProfile
    """
    t_bool = check_trainer_user_exists(request.user)
    if not request.user.is_superuser and not t_bool:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    trainer = get_object_or_404(TrainerProfile, pk=trainer_id)
    user = User.objects.get(username=trainer.user.username)

    if request.method == 'POST':
        trainer_form = TrainerProfileForm(request.POST,
                                          request.FILES, instance=trainer
                                          )
        trainer_username_form = ViewTrainerUserNameForm(request.POST)
        if trainer_form.is_valid() and trainer_username_form.is_valid():

            email = request.POST.get('email')
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')

            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

            profile = trainer_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Successfully updated trainer details!')
            return redirect(reverse('trainer_detail', args=[trainer.id]))
        else:
            messages.error(request, 'Failed to update trainer info. '
                           'Please ensure the form is valid.'
                           )
    else:
        trainer_form = TrainerProfileForm(instance=trainer)
        trainer_username_form = ViewTrainerUserNameForm(instance=user)
        messages.info(request, f'You are editing {trainer.user.first_name}')

    template = 'trainers/edit_trainer.html'
    context = {
        'trainer_username_form': trainer_username_form,
        'trainer_form': trainer_form,

        'trainer': trainer,
    }

    return render(request, template, context)


def trainer_detail(request, trainer_id):
    """ A view to show individual trainer details """

    trainer = get_object_or_404(TrainerProfile, pk=trainer_id)

    contact_form = ContactTrainerRequestForm()

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    context = {
        'trainer': trainer,
        'contact_form': contact_form,
        'is_trainer_bool': trainer_bool,
    }

    return render(request, 'trainers/trainer_details.html', context)


@login_required
def delete_trainer(request, trainer_id):
    """ Delete a trainer from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    trainer = get_object_or_404(TrainerProfile, pk=trainer_id)
    try:
        user = User.objects.get(username=trainer.user.username)
        user.delete()
        messages.success(request, "The user is deleted")
    except User.DoesNotExist:
        messages.error(request, "The user not found")
    trainer.delete()
    messages.success(request, 'Trainer deleted!')
    return redirect(reverse('view_trainers'))


def contact_trainer(request, trainer_id):
    """ A view for the contact trainer """

    trainer = get_object_or_404(TrainerProfile, id=trainer_id)

    contact_form = ContactTrainerRequestForm()

    if request.method == "POST":
        contact_form = ContactTrainerRequestForm(data=request.POST)

        if contact_form.is_valid():

            ctreq = ContactTrainerRequest()
            ctreq.trainer = trainer
            ctreq.name = request.POST.get('name')
            ctreq.phone = request.POST.get('phone')
            ctreq.email = request.POST.get('email')
            ctreq.message = request.POST.get('message')
            ctreq.save()

            messages.success(request,
                             'Contact request received! '
                             f'{trainer.user.first_name}'
                             ' will respond within 2 working days.'
                             )

            trainers = TrainerProfile.objects.all()

            context = {
                'trainers': trainers,
                'is_trainer_bool': check_trainer_user_exists(request.user),
            }

            return render(request, 'trainers/view_trainers.html', context)

        else:
            messages.error(request, "The form is not valid "
                           "please check it and resubmit!! Thank you"
                           )

    context = {
        'trainer': trainer,
        'contact_form': contact_form,
    }

    return render(request, 'trainers/trainer_details.html', context)


@login_required
def view_trainer_email(request, trainer_id):
    """ based on trainer id get mail that is unread """
    t_bool = check_trainer_user_exists(request.user)
    if not request.user.is_superuser and not t_bool:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    trainer = get_object_or_404(TrainerProfile, id=trainer_id)

    contact_mails = ContactTrainerRequest.objects.filter(trainer=trainer,
                                                         read=False
                                                         )

    context = {
        'trainer': trainer,
        'contact_mails': contact_mails,
        'is_trainer_bool': trainer_bool,
    }

    return render(request, 'trainers/view_trainer_email.html', context)


@login_required
def update_trainer_email(request, email_id):
    """ sets the read flag to true if set """
    t_bool = check_trainer_user_exists(request.user)
    if not request.user.is_superuser and not t_bool:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    trainer = None
    if request.method == "POST":
        print("here")
        contact_mail = get_object_or_404(ContactTrainerRequest, pk=email_id)
        trainer = contact_mail.trainer
        print(request.POST)

        if request.POST.get('contact_email_read') == 'read':
            contact_mail.read = True
            contact_mail.save()

            messages.success(request, "The email status was changed to read!!")

            contact_mails = ContactTrainerRequest.objects.filter(trainer=trainer,
                                                                 read=False
                                                                 )

            context = {
                'trainer': trainer,
                'contact_mails': contact_mails,
                'is_trainer_bool': trainer_bool,
            }

            return render(request, 'trainers/view_trainer_email.html', context)
        else:
            messages.error(request, "You must click the checkbox "
                           "to mark a mail as read"
                           )

    contact_mails = ContactTrainerRequest.objects.filter(trainer=trainer,
                                                         read=False
                                                         )
    context = {
        'trainer': trainer,
        'contact_mails': contact_mails,
        'is_trainer_bool': trainer_bool,
    }

    return render(request, 'trainers/view_trainer_email.html', context)


@login_required
def view_trainer_courses(request):
    """ view the courses for trainers """
    t_bool = check_trainer_user_exists(request.user)
    if not request.user.is_superuser and not t_bool:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    wo_programs = WorkoutProgram.objects.all()
    print(wo_programs)

    context = {
        'wo_programs': wo_programs,
        'is_trainer_bool': trainer_bool,
    }

    return render(request, 'trainers/view_trainer_courses.html', context)


def check_update_needed(lst1, lst2):
    """ checks if student not in list """
    updateit = list(set(lst2) - set(lst1))
    
    return updateit


@login_required
def view_class_attendance(request, wo_program_id):
    """ view class attendances """
    t_bool = check_trainer_user_exists(request.user)
    if not request.user.is_superuser and not t_bool:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        trainer_bool = check_trainer_user_exists(request.user)
    else:
        trainer_bool = False

    students = CustomersEnrolledOnCourse.objects.all().filter(wo_program=wo_program_id)

    wo_program = get_object_or_404(WorkoutProgram, pk=wo_program_id)

    if request.method == "POST":
        todays_date = datetime.now()

        today_min = (todays_date - timedelta(hours=6))
        
        check_for_up = check_update_needed(request.POST.getlist('student'), request.POST.getlist('student.hidden'))
        for item_id in check_for_up:
            ClassAttendance.objects.filter(student=item_id,
                                           workout_program=wo_program,
                                           date__range=(today_min, todays_date)
                                           ).delete()

        for student_id in request.POST.getlist('student'):
            
            stud = get_object_or_404(CustomersEnrolledOnCourse, id=student_id)

            class_already_taken = ClassAttendance.objects.filter(student=student_id,
                                                                 workout_program=wo_program,
                                                                 date__range=(today_min, todays_date)
                                                                 )
            
            if not class_already_taken:
                class_attendee = ClassAttendance()
                class_attendee.workout_program = wo_program

                class_attendee.student = stud
                class_attendee.save()

        messages.success(request, "You class attendances have been"
                         " logged thank you!"
                         )

        wo_programs = WorkoutProgram.objects.all()

        context = {
            'wo_programs': wo_programs,
            'is_trainer_bool': trainer_bool,
        }
        return render(request, 'trainers/view_trainer_courses.html', context)

    todays_date = datetime.now()

    today_min = (todays_date - timedelta(hours=6))
    class_already_taken = ClassAttendance.objects.all().filter(workout_program=wo_program,
                                                               date__range=(today_min, todays_date)
                                                               )
    context = {
        'students': students,
        'wo_program': wo_program,
        'is_trainer_bool': trainer_bool,
        'class_already_taken': class_already_taken,
    }

    return render(request, 'trainers/class_attendance.html', context)
