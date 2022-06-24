import re
import os
from datetime import datetime, tzinfo 
from zoneinfo import ZoneInfo
from .models import Post



def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    posts = Post.objects.all()
    return posts

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    new = Post()
    new.title = title
    new.content = content
    new.save()

def edit_entry(pk, content):
    entry = Post.objects.get(id=pk)
    entry.content = content
    entry.save()

def delete_entry(pk):
    """To delete instance directly from the data base"""
    entry = get_entry(pk)
    entry.delete()


def search_entry(q):
    posts = list_entries()
    relist = []
    for r in posts:
        if (q.upper() in r.upper()):
            relist.append(r)
    
    if(relist != None):
        return relist
    else:
        return None


def get_entry(pk):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        post = Post.objects.get(id=pk)
        return post
    except:
        return None

