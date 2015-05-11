from django.contrib import admin

from TLKdb.models import *

# Registrera URLs för admin sidan
admin.site.register(Person)
admin.site.register(Member)
admin.site.register(MemberType)
admin.site.register(Merit)
admin.site.register(MeritType)
admin.site.register(Committee)
admin.site.register(CommitteeType)
admin.site.register(Official)
admin.site.register(OfficialType)
admin.site.register(Board)
admin.site.register(BoardPosition)
