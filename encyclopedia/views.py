from django.shortcuts import render

from . import util

import markdown2
import random

#create a class that accepts a search input

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
                return render(request, "encyclopedia/error.html")
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries" : valid_entries
                })
    