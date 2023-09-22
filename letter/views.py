from django.shortcuts import render, redirect
from .models import Letter
from .forms import LetterWrite, LetterSend

# Create your views here.
def letter_main2(request):
    letters = Letter.objects.filter()
    return render(request, 'letter/letter_main2.html', {'letters':letters})

def letter_write(request):
    if request.method == "POST":
        form = LetterWrite(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.save()
            return redirect('letter_write')
    else:
        form = LetterWrite()
    return render(request, 'letter/letter_write.html', {'form': form})


def letter_list(request, pk):
    letter = Letter.objects.get(id=pk)
    return render(request, 'letter/letter_list.html', {'letter' : letter})


# def letter_main(request):
#     letters = Letter.objects.filter()
#     return render(request, 'letter/letter_main.html', {'letters':letters})
#
# def letter_send(request):
#     if request.method == "POST":
#         form = LetterSend(request.POST)
#         if form.is_valid():
#             letter = form.save(commit=False)
#             letter.save()
#             return redirect('letter_send')
#     else:
#         form = LetterSend()
#     return render(request, 'letter/letter_send.html', {'form': form})