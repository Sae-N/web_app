from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from app1.models import *


class WorkerListView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context =super(WokerListView, self).get_context_date(**kwargs)
        return render(self.request, self.template_name, context)
