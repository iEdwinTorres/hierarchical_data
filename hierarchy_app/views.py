from hierarchy_app.models import Tree
from hierarchy_app.forms import LoginForm, AddTreeForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def show_trees(request):
    return render(request, "index.html", {'trees': Tree.objects.all()})


@login_required
def add_tree_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tree.objects.create(
                name=data.get("name"),
                parents=data.get("parent"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddTreeForm()
    return render(request, "treeDetail.html", {'form': form})


def tree_detail(request, tree_id):
    my_tree = Tree.objects.filter(id=tree_id).first()
    return render(request, 'tree_detail.html', {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "genericForm.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
