# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin


class DashView(BaseMixin, TemplateView):

    template_name = 'dash/dash.html'


class SettingsView(BaseMixin, TemplateView):

    template_name = 'dash/settings.html'
