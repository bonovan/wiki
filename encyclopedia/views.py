from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util

import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    page = util.get_entry(entry)
    if (page == None):
        return render(request, "encyclopedia/error.html")
    else:
        html = markdown2.markdown_path(f"entries/{entry}.md")

        return render(request, "encyclopedia/entry.html", {
            "html" : html,
            "title" : entry
        })

def new(request):
    return render(request, "encyclopedia/new.html")

def rand(request):
    all_entries = util.list_entries()
    entry = random.choice(all_entries)
    
    html = markdown2.markdown_path(f"entries/{entry}.md")

    return render(request, "encyclopedia/entry.html", {
        "html" : html,
        "title" : entry
    })

def search(request):
    if request.method == "POST":
        query = request.POST['q']
    
        if util.get_entry(query):
            html = markdown2.markdown_path(f"entries/{query}.md")
            return render(request, "encyclopedia/entry.html", {
                "html" : html,
                "title" : query
            })
        else:
            all_entries = util.list_entries()
            valid_entries = []

            for entry in all_entries:
                if query.lower() in entry.lower():
                    valid_entries.append(entry)

            if not valid_entries:
                return render(request, "encyclopedia/error.html", {
                    "message" : "There are no entries that match your search"
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries" : valid_entries
                })
    
def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST['title']
        content = request.POST['content']

        entry = util.get_entry(title)
        if entry is not None:
            return render(request, "encyclopedia/error.html", {
                "message" : "There already exists a file with this title"
            })
        else:
            html = markdown2.markdown(content)
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "html" : html,
                "title" : title
            })