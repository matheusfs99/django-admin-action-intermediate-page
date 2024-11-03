from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mass_mail

from event.forms import EmailContentForm
from .models import Event, Participant


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "date"]
    actions = ["send_confirmation_email"]

    @admin.action(description="Enviar emails de confirmação")
    def send_confirmation_email(self, request, queryset):
        form = EmailContentForm(request.POST)
        if request.method == "POST" and form.is_valid():
            if "apply" in request.POST:
                data = form.cleaned_data
                emails = []
                for event in queryset:
                    emails += event.participants.values_list("email", flat=True)
                send_mass_mail(
                    ((
                        data["subject"],
                        data["content"],
                        None, # o gmail não permite `from_email` customizado.
                        emails
                    ),)
                )
                self.message_user(request, "Emails enviados com sucesso")
                return HttpResponseRedirect(request.get_full_path())

        return render(request, "custom_email.html", {"form": form})

admin.site.register(Event, EventAdmin)
admin.site.register(Participant)
