from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtxt = request.GET.get('text', 'default')
    removepunc = request.GET.get('removpunc', 'default')
    print(removepunc)
    print(djtxt)
    # Analyze the text
    return HttpResponse("Remove punc")


# def capfirst(request):
#     return HttpResponse("capfirst <a href='/'>back</a>")
#
#
# def newlineremove(request):
#     return HttpResponse("newlineremove <a href='/'>back</a>")
#
#
# def spaceremover(request):
#     return HttpResponse("spaceremover <a href='/'>back</a>")
#
#
# def charcount(request):
#     return HttpResponse("charcount <a href='/'>back</a>")

# def index(request):
#     params = {'name': 'Kavita','place':'Moon'}
#     return render(request,'index.html',params)

# def index(request):
#     return HttpResponse( '''
#     <h1>Kavita</h1> <a href="https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD"> Django Course</a>''')
#
# def about(request):
#     return HttpResponse("About Us")

# def index(request):
#     return HttpResponse('''<h1>Home</h1> \n <button type="button">Remove punc</button> \n <button type="button">Capfirst</button> \n <button type="button">Newlineremove</button>
#     \n  <button type="button">Spaceremover</button> \n  <button type="button">Charcount</button>''' )
#
#
