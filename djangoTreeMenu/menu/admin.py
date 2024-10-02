from django.contrib import admin

from menu.models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "url",
        "parent",
    ]


class MenuItemTabularAdmin(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [MenuItemTabularAdmin]
