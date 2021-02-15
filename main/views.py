from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserForm, ProfileForm

def home_page(request):
    """Render home page and display Login link"""

    return render(request, "home.html", {"page_title": "Home"})


def signup_page(request):
    """Render sign up form page """

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            # return redirect('settings:profile')
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
