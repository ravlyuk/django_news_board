from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.urls import reverse

from rest_framework import generics
from rest_framework.response import Response

from .serializers import (
    NewsListSerialazer,
    NewsListDetailSerialazer,
    NewsVoiceSerializer,
    CommentListDetailSerialazer
)
from .models import Bb, Rubric, Comment
from .forms import BbForm


# NEWS API
class NewsListView(generics.ListAPIView):
    """Список новостей"""
    serializer_class = NewsListSerialazer
    queryset = Bb.objects.all()


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод конкретной новости"""
    serializer_class = NewsListDetailSerialazer
    queryset = Bb.objects.all()
 

class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsListDetailSerialazer


class NewsVoiceUpdateView(generics.GenericAPIView):
    serializer_class = NewsVoiceSerializer

    def post(self, request):
        id_news = request.data["id_news"]
        if id_news.isdigit():
            id_news = int(id_news)
            currently_count = Bb.objects.get(pk=id_news).likes
            Bb.objects.filter(pk=id_news).update(likes=currently_count + 1)
            return Response({"voices": Bb.objects.get(pk=id_news).likes})
        else:
            return Response("error: incorrect id")


# COMMENT API
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentListDetailSerialazer


class CommentListView(generics.ListAPIView):
    serializer_class = CommentListDetailSerialazer
    queryset = Comment.objects.all()


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentListDetailSerialazer
    queryset = Comment.objects.all()


# VIEWS FOR SITE
def index(request):
    rubrics = Rubric.objects.all()

    bbs = Bb.objects.all()
    paginator = Paginator(bbs, 5)
    if "page" in request.GET:
        page_num = request.GET["page"]
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {
        "rubrics": rubrics,
        "page": page,
        "bbs": page.object_list,
    }
    return render(request, "bboard/index.html", context)


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["rubrics"] = Rubric.objects.all()
        context["comments"] = Comment.objects.filter(post=self.kwargs["pk"])
        return context


class BbCreateView(CreateView):
    template_name = "bboard/create.html"
    form_class = BbForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context


class BbByRubricView(ListView):
    template_name = "bboard/by_rubric.html"
    context_object_name = "bbs"

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs["rubric_id"])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["rubrics"] = Rubric.objects.all()
        context["current_rubric"] = Rubric.objects.get(pk=self.kwargs["rubric_id"])
        return context


class BbAddView(FormView):
    template_name = "bboard/create.html"
    form_class = BbForm
    initial = {"price": 0.0}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse(
            "bboard:by_rubric",
            kwargs={"rubric_id": self.object.cleaned_data["rubric"].pk},
        )


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context
