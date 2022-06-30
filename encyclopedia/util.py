import re
import os
from datetime import datetime, tzinfo 
from zoneinfo import ZoneInfo
import requests 
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename!="" and filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def delete_entry(title):
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)

def search_entry(q):
    relist = []
    for r in list_entries():
        if (q.upper() in r.upper()):
            relist.append(r)
    
    if(relist != None):
        return relist
    else:
        return None


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

#get the time
def get_time(title):
   ko= os.path.getmtime(f"entries/{title}.md")
   dt = datetime.fromtimestamp(ko)
   seoul = ZoneInfo('Asia/Seoul')
   seoultime=dt.replace(tzinfo=seoul)
   fulldateS = seoultime.strftime('%Y %b %d | %H:%M')
   return seoultime



def convert(title):

    try:
        f = default_storage.open(f"entries/{title}.md")

        x = f.read().decode("utf-8")

        return 
        
    except FileNotFoundError:
        return "nothing to say"



#downloading N pictures with the keyword inputed
def downUnsplash(keyword, num):
    num = int(num)
    url = "https://unsplash.com/napi/search?query=" + keyword + "&per_page="+ num + "&xp=search-multi-word%3A"
    r = requests.get(url)

    data = r.json()
    for item in data['photos']['results']:
        name = item['id']
        urls = item['urls']['regular']
        with open('media/'+ name +'.jpg','wb') as f:
            f.write(requests.get(urls).content)