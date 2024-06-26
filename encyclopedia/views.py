from django.shortcuts import render

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
    entries = util.list_entries()
    entry = random.choice(entries)
    
    html = markdown2.markdown_path(f"entries/{entry}.md")

    return render(request, "encyclopedia/entry.html", {
        "html" : html,
        "title" : entry
    })