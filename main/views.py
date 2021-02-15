from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserForm, ProfileForm
from django.contrib.auth import logout


def home_view(request):
    """Render home page and display Login link"""

    return render(request, "home.html", {"page_title": "Home"})


def login_view(request):
    login_form = LoginForm()
    return render(request, "login.html", {'form': login_form})


@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.


def signup_view(request):
    """Render sign up form page """

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _(
                'Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {
        "page_title": "Sign Up",
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'signup.html', context)
