
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from timeline.forms import loginForm,addPost,DocumentForm
from timeline.models import posts,Document,Like




from django.contrib.auth.decorators import login_required


# Create your views here.


def Signup(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    form= UserCreationForm()
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=User()
            user.username=form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request,'Signup.html',{'form':form,'msg':'Registration done successfully'})
    return render(request,'Signup.html',{'form':form ,'msg':''})

def Signin(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    form=loginForm()
    if request.method == 'POST':
        form=loginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user =authenticate(username=username ,password=password)
            if user is None:
                return render(request, 'Signin.html', {'form': form, 'msg': 'No user Found'})
            else:
                login(request,user)
                # request.session['city'] = 'Bangalore'
                request.session['id']='user.id'
                return redirect('dashBoard')
    return render(request,'Signin.html',{'form':form ,'msg':''})




#@login_required(login_url='/signin')
def dashBoard(request):
    if request.user.is_authenticated:
        documents = Document.objects.all()
        return render(request, 'Dashboard.html', {'documents': documents})
    else:
        return redirect('Signin')


def Signout(request):
    logout(request)
    #del request.session['city']
    for k in request.session.keys():
        del request.session[k]
    return redirect('Signin')



#Create posts form

#@login_required(login_url='/signin')
def addPosts(request):
    if request.user.is_authenticated:
        form = addPost()
        if request.method == "POST":
            form = addPost(request.POST)
            if form.is_valid():
                #form.save()
                add = posts()
                add.title = form.cleaned_data['title']
                add.description = form.cleaned_data['description']
                add.image_url = form.cleaned_data['image_url']
                add.save()
                return redirect('dashBoard')
        return render(request,'Dashboard.html',{'form':form , 'msg': 'Post Added Suceesfully'})
    else:
        return redirect('Signin')




@login_required(login_url='/signin')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm\
            (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashBoard')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form ,'msg': 'Post Added Suceesfully'
    })



def like(request, pk):
    return redirect('Signin')