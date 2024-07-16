from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import include, path
from datetime import datetime
from .models import Txn
from .csv2txns import csv2txns
from .query import query as q


def index(request):
    return render(request, "index.html")


def load(request):
    if request.method == "POST":
        rows = csv2txns(request.POST["csv"])

        for row in rows:
            t = Txn(
                description=row["description"],
                category=row["category"],
                type=row["type"],
                amount=row["amount"],
                memo=row["memo"],
                post_date=datetime.strptime(
                    row["post_date"] + " 00:00:00", "%m/%d/%Y %H:%M:%S"
                ),
                txn_date=datetime.strptime(
                    row["txn_date"] + " 00:00:00", "%m/%d/%Y %H:%M:%S"
                ),
                user_category="",
                user_subcategory="",
            )
            t.save()
        return redirect("index")
    else:
        return render(request, "load_form.html")


def categorize(request):
    if request.method == "POST":
        print(csv2txns(request.POST["selections"]))
    else:
        return render(request, "categorize_form.html")


def query(request):
    ctx = {}
    if request.method == "POST":
        ctx["answer"] = q(request.POST["query"])
        ctx["query"] = request.POST["query"]

    return render(request, "query.html", ctx)
