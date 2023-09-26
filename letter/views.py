from django.shortcuts import render, redirect
from .models import Letter
from .forms import LetterWrite

# Create your views here.
def letter_log(request):
    letters = Letter.objects.filter()
    return render(request, 'letter/letter_main2.html', {'letters':letters})

def letter_write(request):
    if request.method == "POST":
        form = LetterWrite(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('letter_write')
    else:
        form = LetterWrite()
    return render(request, 'letter/letter_write.html', {'form': form})


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