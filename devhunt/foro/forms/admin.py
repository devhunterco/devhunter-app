# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from djconfig.forms import ConfigForm

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from foro.models.category import Category
from foro.models.comment_flag import CommentFlag


User = get_user_model()


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "location",
                  "timezone", "is_administrator", "is_moderator", "is_active",
                  "es_destacado")


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("parent", "title", "description", "is_closed", "is_removed")

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        queryset = Category.objects.for_parent()

        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        self.fields['parent'] = forms.ModelChoiceField(queryset=queryset, required=False)

    def clean_parent(self):
        parent = self.cleaned_data["parent"]

        if self.instance.pk:
            has_childrens = self.instance.category_set.all().exists()

            if parent and has_childrens:
                raise forms.ValidationError(_("The category you are updating "
                                              "can not have a parent since it has childrens"))

        return parent


class CommentFlagForm(forms.ModelForm):

    class Meta:
        model = CommentFlag
        fields = ("is_closed", )

    def __init__(self, user=None, *args, **kwargs):
        super(CommentFlagForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        self.instance.moderator = self.user
        return super(CommentFlagForm, self).save(commit)


class BasicConfigForm(ConfigForm):

    site_name = forms.CharField(initial="Tu comunidad",
                                label=_("Nombre del sitio"))
    site_description = forms.CharField(initial="Descripción de tu comunidad..",
                                       label=_("Descripción"),
                                       max_length=160, required=False)
    site_landing_title = forms.CharField(initial="Bienvenido a la comunidad !",
                                         label=_("Titulo del landing"),
                                         max_length=60, required=False)
    show_alert_menssage = forms.BooleanField(initial=True,
                                             label=_("Mostrar alerta"),
                                             required=False)
    alert_menssage = forms.CharField(initial="alert_menssage",
                                     label="Mensaje de alerta", max_length=180,
                                     required=False)
