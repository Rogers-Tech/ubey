from django.shortcuts import render
import pafy

# Create your views here.

def video(request):
    try:
        if request.method == 'POST':
            url = request.POST.get('videoLink')
            video = pafy.new(url)
            embedlink = url.replace("watch?v=", "embed/")
            context = {
                'vid': video,
                'embedlink': embedlink,
            }
            return render(request, 'index.html', context)
        else:
            context = {
                'info': 'Paste youtube video link.',
            }
            return render(request, 'index.html', context)
    except:
        context = {
            'info': 'Check internet connection and have a correct youtube video link.',
        }
        return render(request, 'index.html', context)


def audio(request):
    try:
        if request.method == 'POST':
            url = request.POST.get('audioLink')
            video = pafy.new(url)
            vr = video.getbestaudio()

            context = {
                'vid': video,
                'aud': vr,
            }
            return render(request, 'aud.html', context)
        else:
            context = {
                'info': 'Paste youtube video link.',
            }
            return render(request, 'aud.html', context)
    except:
        context = {
            'info': 'Check internet connection and have a correct youtube video link.',
        }
        return render(request, 'aud.html', context)