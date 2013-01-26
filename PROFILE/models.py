#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from datetime import date

class UserProfile(models.Model):

    COUNTRIES = (
        ('US', 'United States'),
        ('UA', 'Ukraine'),
        ('RU', 'Russia'),
        ('IL', 'Israel'),
        ('AU', 'Australia'),
        ('NZ', 'New Zealand'),
        ('NL', 'Netherlands'),
        ('IT', 'Italy'),
    )

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    date_of_birth = models.DateField(default="1980-02-14", auto_now=False, auto_now_add=False, null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES, default="US", verbose_name="Страна", null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=100, null=True, blank=True)
    date_added_to_db = models.DateField(auto_now_add=True, verbose_name="Зарегистрирован")

    def age(self):
 
        """ Calculates person age as for Admin panel"""
        today = date.today()
        #   self.short_description = "Возраст" # does not work

        try: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            birthday = self.date_of_birth.replace(year=today.year, day=self.date_of_birth.day-1)

        if birthday > today:
            return today.year - self.date_of_birth.year - 1
        else:
            return today.year - self.date_of_birth.year

    class Meta:
        verbose_name = 'Arpaso.com User Profile'

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def admin_representation(self):
        """ Identical to __unicode__ but not magic word - meaning it CAN BE ORDERED in AdminPanel, since plain __unicode__ can not """
        return "%s %s" % (self.first_name, self.last_name)

    age.short_description = "Возраст" 
    age.admin_order_field = 'date_of_birth'

    admin_representation.short_description = "Пользователь"
    admin_representation.admin_order_field = 'first_name'


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('admin_representation', 'age', 'country', 'date_added_to_db')

    ordering = ("-date_of_birth", 'first_name')
    
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Дополнительная информация (необязательные)', {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'country')
        }),
        ('Биография и контакты (необязятельные)', {
            'classes': ('collapse',),
            'fields': ('biography', 'contacts')
        }),

    )


admin.site.register(UserProfile, UserProfileAdmin)


# Here for validation reasons only
""" 
>>>./manage.py sqlall PROFILE

BEGIN;
CREATE TABLE "PROFILE_userprofile" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "date_of_birth" date,
    "country" varchar(2),
    "biography" text,
    "contacts" varchar(100),
    "date_added_to_db" date NOT NULL
)
;
COMMIT;
"""