from django.contrib import admin
from .models import Faculties
from .models import Latestnews
from .models import Departments
from .models import Courses
from .models import Materials
from .models import UserProfile

# Register your models here.

admin.site.register(Faculties)
admin.site.register(Latestnews)
admin.site.register(Departments)
admin.site.register(Courses)
admin.site.register(Materials)
admin.site.register(UserProfile)





