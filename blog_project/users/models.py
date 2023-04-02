from django.db import models
from django.contrib.auth.models import User
# To resize the image while uploading, we install pillow package from pip and import PIL module
from PIL import Image

# Create your models here.
class User_Profile(models.Model):
    # "OneToOneField() since "One User must have only one ProfilePic at a time".
    # CASCADE means that "When the User is deleted, Also deletes his "Profile".
    # so if we want to update "User_Profile" then we must do it using "user"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        # To change <User_Profile object1> to appropriate username of the User while displaying.
        return f'{self.user.username} Profile'

    # This save() method gets run everytime our model is saved. save() method is already existed in our parent class,
    # but Here, we are creating our own save() method to add some functionalities to our model class.
    def save(self):
        # taking the save() method from parent class.
        super().save()
        image = Image.open(self.profile_pic.path)

        if image.width > 300 or image.height > 300:
            resized_img = (300, 200)
            image.thumbnail(resized_img)
            # HERE WE ARE OVERRIDING THE SAVE() METHOD OF PARENT CLASS
            image.save(self.profile_pic.path)
