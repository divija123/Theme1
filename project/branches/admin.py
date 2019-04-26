from django.contrib import admin

# Register your models here.


from .models import Departments,companies,college

admin.site.register(Departments)
admin.site.register(companies)
admin.site.register(college)

