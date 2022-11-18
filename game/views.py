from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line3 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<img src="https://w.wallhaven.cc/full/3l/wallhaven-3l93ky.jpg" width=1000>'
    return HttpResponse(line1 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主页面</a>'
    line2 = '<img src="https://w.wallhaven.cc/full/rr/wallhaven-rr222w.jpg" width=1000>'
    return HttpResponse(line1 + line3 + line2)
