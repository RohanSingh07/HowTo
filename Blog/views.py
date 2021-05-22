from django.shortcuts import render,redirect
from . import forms
from . import models
from datetime import datetime
from django.contrib import messages

# Homepage
def HomeView(request):
    AllBlogs = models.Blog.objects.filter(Mode='Public')
    return render(request,'index.html',{
        'blogs':AllBlogs
    })

# My Blogs
def MyBlogs(request):
    myblogs = models.Blog.objects.filter(user = request.user)
    return render(request,'myblogs.html',{
        'blogs':myblogs
    })

# Add New Blogs
def AddBlog(request):
    if request.method == "GET":
        # Form for model Blog
        form = forms.NewForm()
        return render(request,'AddBlog.html',{
            'form':form
        })
    else:
        form = forms.NewForm(request.POST ,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            Image1 = form.files.get('Image1')
            Description = form.cleaned_data.get('Description')
            Subheading2 = form.cleaned_data.get('Subheading2')
            Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            video = form.files.get('Video')
            Mode = form.files.get('Mode')
            slug = request.user.username+'-Blogs-'+datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            NewBlog = models.Blog(
                user = request.user,
                Name = Name,
                Background_Image = Background_Image,
                Subheading1 = Subheading1,
                Image1 = Image1,
                Description = Description,
                Subheading2 = Subheading2,
                Image2 = Image2,
                Paragraph2 = Paragraph2,
                Subheading3 = Subheading3,
                Image3 = Image3,
                Paragraph3 = Paragraph3,
                Video = video,
                Mode = Mode,
                slug = slug
            )
            NewBlog.save()
        else:
            messages.error(request,'The form is invalid !')
        return redirect("Blog:MyBlogs")

# View for individual Blogs
def BlogView(request,slug):
    if request.method =='GET':
        blog = models.Blog.objects.filter(slug=slug)
        if blog.exists():
            blog = blog[0]
        if blog.user == request.user:
            admin = True
        else:
            admin = False
        return render(request,'blog.html',{
            'blog':blog,
            'is_admin':admin
        })
    else:
        # for post request of comments
        blog = models.Blog.objects.filter(slug=slug)[0]
        # Save comments to the Blog
        comment = request.POST['comment']
        name = request.POST['name']
        com = models.Comments(
            Comment = comment,
            Name = name
        )
        com.save()
        blog.coments.add(com)
        blog.save()
        return render(request, 'blog.html', {
            'blog': blog
        })

# Edit existing blogs
def EditBlog(request,slug):
    blog = models.Blog.objects.get(slug=slug)
    if request.method == 'GET':

        form = forms.NewForm(instance=blog)

        return render(request,'EditBlog.html',{
            'form':form
        })
    else:

        # The user will have to upload the required files again

        form = forms.NewForm(request.POST, request.FILES)
        if form.is_valid():

            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            Image1 = form.files.get('Image1')
            Description = form.cleaned_data.get('Description')
            Subheading2 = form.cleaned_data.get('Subheading2')
            Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            video = form.files.get('Video')
            Mode = form.cleaned_data.get('Mode')
            if Name !=None:
                blog.Name=Name
            if Background_Image != None:
                blog.Background_Image=Background_Image
            if Subheading1 != None:
                blog.Subheading1=Subheading1
            if Image1 != None:
                blog.Image1=Image1
            if Description != None:
                blog.Description=Description
            if Subheading2 != None:
                 blog.Subheading2=Subheading2
            if Image2 != None:
                blog.Image2=Image2
            if Paragraph2 != None:
                blog.Paragraph2=Paragraph2
            if Subheading3 != None:
                blog.Subheading3=Subheading3
            if Image3 != None:
                blog.Image3=Image3
            if Paragraph3 != None:
                blog.Paragraph3=Paragraph3
            if video != None:
                blog.Video=video
            if Mode != None:
                blog.Mode=Mode
            blog.save()
            return redirect('Blog:MyBlogs')
        else:
            messages.error(request,'The form is invalid !')
            return redirect('Blog:MyBlogs')

# For searching blogs using the username
def SearchBlog(request):
     Search = request.GET['Search']
     blogs = models.Blog.objects.filter(user__username = Search,Mode = 'Public')
     return render(request,'SearchPage.html',{
         'blogs':blogs
     })