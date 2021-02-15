from django.shortcuts import render
from .forms import SignupForm

def home_page(request):
    """Render home page and display Login link"""

    return render(request, "home.html", {"page_title": "Home"})


def signup_page(request):
    """Render sign up form page."""

    if request.user.is_authenticated:
        return redirect(reverse('login_success'))

    if request.method == "POST":
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your account has been created")

                return redirect(reverse('login_success'))
            else:
                messages.warning(
                    request, "We were unable to register your account")
        else:
            messages.warning(request, "Please correct the error(s) below")

    else:
        signup_form = SignupForm()

    context = {
        "page_title": "Sign Up",
        "form": signup_form
    }
    return render(request, 'signup.html', context)
