from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from hierarchy_app.models import Tree


admin.site.register(Tree, DraggableMPTTAdmin)
