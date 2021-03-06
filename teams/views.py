from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy

from . import models


#def team_list(request):
#    teams = models.Team.objects.all()
#    return render(request, 'teams/team_list.html', {'teams': teams})
#
#
#def team_detail(request, pk):
#    team = get_object_or_404(models.Team, pk=pk)
#    return render(request, 'teams/team_detail.html', {'team': team})


class TeamListView(CreateView, ListView):
    fields = ("name", "practice_location", "coach")
    context_object_name = "teams"
    model = models.Team
    template_name = "teams/team_list.html"

class HomeView(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games_today"] = 6
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games_today"] = 6
        return context

class TeamDetailView(DetailView, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    template_name = "teams/team_detail.html"

class TeamCreateView(CreateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    template_name = "teams/team_form.html"

class TeamUpdateView(UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team


class TeamDeleteView(DeleteView):
    model = models.Team
    success_url = reverse_lazy("teams:list")

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()