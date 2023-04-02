from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AbstractUserForm, UserUpdateForm, ProfileUpdateForm
# To see the profile only when logged in
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    #If we try to "post" the data, then it will instantiate our data with our UserCreationForm
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) is now changed to
        form = AbstractUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Here we are accessing username just to send a success message.
            username = form.cleaned_data['username']
            messages.success(request, f'{username} has created account successfully!')
            return redirect('blog-home')
    else:
        # If we don't try to "post" our form data it will return an empty form.
        form = AbstractUserForm()
    return render(request, 'users/register.html', {'form': form})


# IF WE ONLY WANT TO ACCESS OUR PROFILE AFTER LOGGED IN
# for that purpose "@login_required" decorator is used for our profile view.
@login_required
def profile(request):
    if request.method == 'POST':
        # Since we update a single "User Instance"
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Since we update a single "User_Profile Instance", here we update only image
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.user_profile)

        if u_form.is_valid() or p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)