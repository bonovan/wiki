from django.shortcuts import render

from . import util

import markdown2


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
            "html" : html
        })

def new(request):
    return render(request, "encyclopedia/new.html")

