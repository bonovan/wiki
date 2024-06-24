from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    page = util.get_entry(name)
    if (page == None):
        return
    else:
        html = markdown2.markdown_path(f"entries/{name}.md")

        return render(request, "encyclopedia/entry.html", {
            "html" : html
        })

