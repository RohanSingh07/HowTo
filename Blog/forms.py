from django.forms import forms,ModelForm
from .models import Blog

# Creating form for Blog
class NewForm(ModelForm):
    class Meta:
        model = Blog
        fields =[
            'Name','Background_Image','Image1','Description','Subheading1','Image2','Subheading2','Paragraph2','Image3','Subheading3'
            ,'Paragraph3','Video','Mode'
        ]
