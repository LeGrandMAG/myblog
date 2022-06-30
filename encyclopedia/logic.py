import re
import os
from datetime import datetime, tzinfo 
from zoneinfo import ZoneInfo
from .models import Post



#return the list of all the entry stored in the data base
def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    posts = Post.objects.all()
    return posts


#Save a new entry in the database
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

#edit an entry stored in the database
def edit_entry(pk, content):
    entry = Post.objects.get(id=pk)
    entry.content = content
    entry.save()


#delete entry from the database
def delete_entry(pk):
    """To delete instance directly from the data base"""
    entry = get_entry(pk)
    entry.delete()


# search for entries containing 'q'  in the database and return them as a list
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


#check if a specific entry is in the database and return it
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


#convert the period into the appropriate time of the class
def classHour(time):
    list = [ {
        "hour": 9, 
        "time":1}
            ]
    i = 0
    while(i<14):
        #append time into the imaginary clock
        i+=1 
        a = list[i-1]['hour'] + 1
        b = list[i-1]['time'] + 1

        c = { 'hour':a, 'time': b}
        list.append(c)

    #convert the input into integer            
    v = int(time)

    #verify if the integer is greater than 
    if (v<=0):
        print("Please insert a number above 0")
    else:
        e = list[v-1]['hour']
        f = list[v-1]['time']
        ##print(f'For the period {f} the time is {e}:00')
        
        #return the time
        return e
