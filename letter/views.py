from django.shortcuts import render, redirect
from .models import Letter
from .forms import LetterWrite
from django.views.generic import CreateView, ListView


# Create your views here.
def letter_log(request):
    letters = Letter.objects.filter()
    return render(request, 'letter/letter_main2.html', {'letters': letters})


# def letter_write(request):
#     if request.method == "POST":
#         form = LetterWrite(request.POST)
#         if form.is_valid():
#             letters = form.save(commit=False)
#             letters.save()
#             return redirect('letter_write')
#
#         print(request.POST)
#         form = LetterWrite(request.POST)
#         print(form.is_valid())
#
#     else:
#         form = LetterWrite()
#     return render(request, 'letter/letter_write.html', {'form': form})

def letter_write(request):
    if request.method == 'GET':
        return redirect('letter_write')
    elif request.method == 'POST':
        title = request.POST['title']
        write = request.POST['write']
        contents = request.POST['contents']
        board = Letter(title=title, contents=contents, write=write)
        board.save()

        return redirect('letter_list')


def main(request):
    if request.method == "GET":
        return render(request, 'letter/letter_main2.html')

    elif request.method == "POST":
        username = request.POST['userName']
        password = request.POST['userPassword']
        user = authenticate(request, username=userName, password=userPassword)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:write'))
        else:
            return render(request, 'letter/letter_main2.html')


def letter_list(request):
    all_write = Write.objects.all()
    return render(request,'letter_list',{'all_write': all_write})