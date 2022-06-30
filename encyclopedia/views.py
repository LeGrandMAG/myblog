from django.shortcuts import redirect, render

from . import logic
import re
import random
from markdown2 import Markdown 
from .models import Post 
import requests 
from deep_translator import PapagoTranslator
from . import classHour as cl

client = 'LXt8cXRom35yoCXW4Q_4'
secret = 'kF7mI8sMgN'
#Homepage
def home(request):
    
    txt =random.choice(logic.list_entries())
    return render(request, "encyclopedia/home.html", {"random":txt.id, 'search': si })

def renders(request):
    txt =random.choice(logic.list_entries())

    if(request.POST.get('time')):
        time = request.POST.get('time')    
        go = cl.classHour(time)
        return render(request, "encyclopedia/render.html", {"random":txt.id, "time":go})

    else:
        return render(request, "encyclopedia/render.html", {"random":txt.id})



def unsplash(request):
    if(request.POST.get('time')):

        time = request.GET.get('search')    
    if(si):
        url = "https://unsplash.com/napi/search?query=" + si + "&per_page=3&xp=search-multi-word%3A"
        r = requests.get(url)

        data = r.json()


    for item in data['photos']['results']:
        name = item['id']
        urls = item['urls']['regular']
        with open(name +'.jpg','wb') as f:
            f.write(requests.get(urls).content)
    txt =random.choice(logic.list_entries())
    return render(request, "encyclopedia/render.html", {"random":txt.id, "search":si})


#Blog
def blog(request):
    ##x = random.randrange(0,len(logic.list_entries))
    posts = logic.list_entries()
    print(posts)
    txt =random.choice(posts)
    t = request.GET.get('q') if request.GET.get('q') != None else 'There is not topic with that name'
    context = {"posts":posts, "random":txt.id}
    return render(request, "encyclopedia/blog.html", context)

def notfound(request):
    posts = logic.list_entries()
    txt =random.choice(posts)

    return render(request, 'encyclopedia/notfound.html', {"random":txt.id})

def search(request):
    posts = Post.objects.all()

    #This is the view for looking for posts
    txt =random.choice(posts)
    f = request.GET.get('q')
    t=request.GET.get('q')
    if(logic.get_entry(f)):
        return redirect( 'detail', f)
    elif(f):
        c = logic.search_entry(f)
        print(c)
    else:
        c ="Nothing to display"
    context = {"random":txt.id, "q":t, "f":f, "result": c}
    return render(request, "encyclopedia/search.html", context)

def layout(request):
    txt =random.choice(logic.list_entries())
    
    context = {"random":txt.id}
    return render(request, "encyclopedia/layout.html", context)

def post(request, pk):
    txt =random.choice(logic.list_entries())    
    el = Markdown()
    post = logic.get_entry()
    print(post)
    if(post):
        xx = el.convert(post.content)
        print(post)
        ###conv = el.convert(post)
    else:
        return redirect('notfound')
    context = {"post":xx, "random":txt.id}
    return render(request, "encyclopedia/post.html", context)



def entries(request, pk):
    posts = logic.list_entries()
    txt =random.choice(posts)
    entry = logic.get_entry(pk)    
    el = Markdown()
    if (entry):
        e = el.convert(entry.content)
        print(e)
    else:
        return redirect( 'notfound')
    context = {"title":pk, "content":e,"entry":entry, "random":txt.id}
    return render(request, "encyclopedia/entry.html", context)


def create(request):
    txt =random.choice(logic.list_entries())    

    if (request.method == 'POST'):
        if (request.POST.get('title') =='' and request.POST.get('content') == ""):
            return redirect ('empty')
            
        else:
            titles = request.POST.get('title')
            content = request.POST.get('content')
            entry = Post()
            entry
        if (logic.get_entry(titles)==None):
            logic.save_entry(titles, content)
            x = Post.objects.get(title=titles)
            return redirect("detail", x.id)
        else:
            return redirect("duplicate")
        
    return render(request, "encyclopedia/create.html", {"random":txt.id})

def password(request):
    txt =random.choice(logic.list_entries())    
    passs = "Pourquoipasnous?@"
    if (request.method == 'POST'):
        if (request.POST.get('password') == passs):
            return redirect ('create')
            
        else:
            return redirect('home')
        
    return render(request, "encyclopedia/password.html", {"random":txt.id})
    
def empty(request):
    txt =random.choice(logic.list_entries())

    return render(request, 'encyclopedia/empty.html', {"random":txt.id})
def duplicate(request):
    txt =random.choice(logic.list_entries())    

    return render(request,"encyclopedia/exist.html", {"random":txt.id})

def edit(request, pk):
    txt =random.choice(logic.list_entries())    
    post = logic.get_entry(pk)
    if (request.method == "POST"):
        content = request.POST.get('content')
        logic.edit_entry(pk, content)
        return redirect("detail", pk)
    return render(request, "encyclopedia/edit.html", {"post":post,"random":txt.id})


def delete(request, pk):
    if(request.method == "POST"):
        logic.delete_entry(pk)
    return redirect("blog")





