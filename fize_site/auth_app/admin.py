from django.contrib import admin
from auth_app.models import *
# Student, Teacher, CahierDeCours, ResponsableMetier, Enseigner, Planning, Note, Classe,Salle, Matiere, Filiere, Comptable, Administrateur, ResponsableFiliere, ResponsableClasse

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Administrateur)
admin.site.register(ResponsableFiliere)
admin.site.register(ResponsableClasse)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Comptable)
admin.site.register(Filiere)
admin.site.register(Note)
admin.site.register(Planning)
admin.site.register(CahierDeCours)
admin.site.register(Enseigner)
admin.site.register(ResponsableMetier)