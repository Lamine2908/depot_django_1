from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from django.utils import timezone

from django.contrib.auth.decorators import login_required, user_passes_test

def navigation(request):
    return render(request, 'navigation.html')

  
def espaceeleve(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'espaceeleve.html', {'student': student})

  
def espaceadmin(request, admin_id):
    administrateur = get_object_or_404(Administrateur, id=admin_id)
    return render(request, 'espaceadmin.html', {'administrateur': administrateur})

  
def espaceadmins(request):
    administrateur = Administrateur.objects.all()
    return render(request, 'espaceadmin.html', {'administrateur': administrateur})

def responsable_filiere(request, responsable_id):
    responsableFiliere = get_object_or_404(ResponsableFiliere, id=responsable_id)
    return render(request, 'responsable_filiere.html', {'responsableFiliere': responsableFiliere})

  
def responsable_metier(request, responsable_id):
    responsableMetier = get_object_or_404(ResponsableMetier, id=responsable_id)
    return render(request, 'responsable_metier.html', {'responsableMetier': responsableMetier})

  
def espaceprof(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'espaceprof.html', {'teacher': teacher})

  
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

  
def espaceresponsableclasse(request):
    return render(request, 'responsableClasse.html')

  
def responsableclasse(request, responsable_id):
    responsableClasse = get_object_or_404(ResponsableClasse, id=responsable_id)
    return render(request, 'responsableClasse.html', {'responsableClasse': responsableClasse})

  
def espacecomptable(request, comptable_id):
    comptables = get_object_or_404(Comptable, id=comptable_id)
    return render(request, 'espacecomptable.html', {'comptables': comptables})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)

        if form.is_valid():
            matricule = form.cleaned_data.get('matricule')
            email = form.cleaned_data.get('email')
            
            user_found = False

            try:
                
                student = Student.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'espaceeleve.html', {'student': student})
            except Student.DoesNotExist:
                pass

            try:
                teacher = Teacher.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'espaceprof.html', {'teacher': teacher})
            except Teacher.DoesNotExist:
                pass

            try:
                administrateur = Administrateur.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'espaceadmin.html', {'administrateur': administrateur})
            except Administrateur.DoesNotExist:
                pass

            try:
                responsableFiliere = ResponsableFiliere.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'responsable_filiere.html', {'responsable_filiere': responsableFiliere})
            except ResponsableFiliere.DoesNotExist:
                pass 
            
            try:
                responsableMetier = ResponsableMetier.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'responsable_metier.html', {'responsable_metier': responsableMetier})
            except ResponsableMetier.DoesNotExist:
                pass

            try:
                comptable = Comptable.objects.get(matricule=matricule, email=email)
                user_found = True
                return render(request, 'espacecomptable.html', {'comptable': comptable})
            except Comptable.DoesNotExist:
                pass

            if not user_found:
                messages.error(request, "Informations incorrectes. Veuillez vérifier votre matricule et votre email.")
        else:
            messages.error(request, "Formulaire invalide, veuillez vérifier les informations.")
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', {'form': form})



def index(request):
    return render(request, 'index.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

  
def teacher_list(request, admin_id):
    administrateur = get_object_or_404(Administrateur, id=admin_id)
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'administrateur':administrateur, 'teachers': teachers})

  
def responsableFiliere_list(request):
    responsables = ResponsableFiliere.objects.all()
    return render(request, 'responsableFiliere_list.html', {'responsables': responsables})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


  
def delete_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "L'élève a été supprimé avec succès.")
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


from .form import ResponsableFiliereForm, ResponsableUpdateForm

def ajouter_responsable(request):
    if request.method == 'POST':
        form = ResponsableFiliereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('responsableFiliere_list')
    else:
        form = ResponsableFiliereForm()
    return render(request, 'ajouter_responsable_filiere.html', {'form': form})

def delete_teacher_by_id(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        messages.success(request, "Le professeur a été supprimé avec succès.")
        return redirect('teacher_list')

    return render(request, 'delete_teachers.html', {'teacher': teacher})

def delete_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "L eleve a été supprimé avec succès.")
        return redirect('student_list')

    return render(request, 'delete_students.html', {'student': student})

def filter_students_view(request):
    students = Student.objects.all()

    id = request.GET.get('id')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    if id:
        students = students.filter(id=id)
    elif first_name:
        students = students.filter(first_name__icontains=first_name)
    elif last_name:
        students = students.filter(last_name__icontains=last_name)

    return render(request, 'filter_students.html', {'students': students})

def filter_teacher(request):
    teachers = Teacher.objects.all()
    
    id=request.GET.get('id')
    first_name= request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    
    if id:
        teachers = teachers.filter(id=id)
    elif first_name:
        teachers = teachers.filter(first_name__icontains=first_name)
    elif last_name:
        teachers = teachers.filter(last_name__icontains = last_name)
        
    return render(request, 'filter_teachers.html', {'teachers': teachers})

  
def update_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherUpdateForm(instance=teacher)
    
    return render(request, 'modifier_prof.html', {'form': form, 'teacher': teacher})

def update_responsable(request, admin_id):
    admin = get_object_or_404(ResponsableFiliere, id=admin_id)
    
    if request.method == 'POST':
        form = ResponsableUpdateForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('responsableFiliere_list')
    else:
        form = ResponsableUpdateForm(instance=admin)
    
    return render(request, 'modifier_responsable.html', {'form': form, 'admin': admin})

 
def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else: 
        student = get_object_or_404(Student, id=student_id)
        form = StudentUpdateForm(request.POST, instance=student)
        
    return render(request, 'update_student.html', {'form': form, 'student': student})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def detail_prof(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def ajouter_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matière ajoutée avec succès.')
            return redirect('liste_matieres')
        else:
            messages.error(request, 'Erreur lors de l\'ajout de la matière. Veuillez vérifier les informations.')
    else:
        form = MatiereForm()
    
    return render(request, 'ajouter_matiere.html', {'form': form})

def modifier_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'modifier_matiere.html', {'form': form})

def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'liste_matieres.html', {'matieres': matieres})

from .models import Filiere

def liste_filieres(request):
    filieres = Filiere.objects.all()
    return render(request, 'liste_filieres.html', {'filieres': filieres})

def supprimer_matiere(request, matiere_id):
    matiere = Matiere.objects.get(id=matiere_id)
    if request.method == 'POST':
        matiere.delete()
        return redirect('liste_matieres')

    return render(request, 'supprimer_matiere.html', {'matiere': matiere})

from .form import FiliereForm

def ajouter_filiere(request):
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filiere ajoutée avec succès.')
            return redirect('liste_filieres')
        else:
            messages.error(request, 'Erreur lors de l\'ajout de la filiere. Veuillez vérifier les informations.')
    else:
        form = FiliereForm()
    
    return render(request, 'ajouter_filiere.html', {'form': form})

def parametre_filiere(request, responsable_id):
    responsable = get_object_or_404(ResponsableFiliere, id=responsable_id)
    
    context = {
        'responsable': responsable,
    }
    
    return render(request, 'parametre_filiere.html', context)

def ajouter_responsable_metier(request, responsable_id):
    responsable = get_object_or_404(ResponsableFiliere, id=responsable_id)
    if request.method == 'POST':
        form = ResponsableMetierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('responsableMetier_list')
    else:
        form = ResponsableMetierForm()
    return render(request, 'ajouter_responsable_metier.html', {'form': form, 'responsable':responsable})

def responsableMetier_list(request, responsable_id):
    responsable = get_object_or_404(ResponsableFiliere, id=responsable_id)
    responsableMetieRs = ResponsableMetier.objects.filter(responsable=responsable)
    
    return render(request, 'responsable_metier.html', {'responsable':responsable, })

from .form import MediaForm

from django.shortcuts import render, redirect, get_object_or_404
from .form import MediaForm
from .models import Teacher, Enseigner, Classe, Matiere

def ajouter_ressource(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    enseignements = Enseigner.objects.filter(matiere__teacher=teacher)

    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, teacher=teacher)
        if form.is_valid():
            media = form.save(commit=False)
            media.teacher = teacher

            classe_id = request.POST.get('classe')
            matiere_id = request.POST.get('matiere')

            try:
                classe = Classe.objects.get(id=classe_id)
                matiere = Matiere.objects.get(id=matiere_id)

                enseignement = enseignements.filter(classe=classe, matiere=matiere).first()
                
                if enseignement:
                    media.save()
                    return redirect('liste_ressource')
                else:
                    form.add_error(None, "Cette classe ou matière ne vous est pas affectée.")
            except (Classe.DoesNotExist, Matiere.DoesNotExist):
                form.add_error(None, "Classe ou matière invalide.")

    else:
        form = MediaForm(teacher=teacher)

    return render(request, 'ajouter_ressource.html', {'form': form, 'teacher': teacher})

from .models import Media, Teacher, Enseigner

def liste_ressource(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    enseignements = Enseigner.objects.filter(matiere__teacher=teacher)

    ressources = Media.objects.filter(classe__in=enseignements.values_list('classe_id', flat=True),
                                      matiere__in=enseignements.values_list('matiere_id', flat=True),
                                      teacher=teacher)

    return render(request, 'liste_ressource.html', {'ressources': ressources, 'teacher': teacher})


# def paiement_liste(request):
#     paiements = Paiement.objects.all()
#     return render(request, 'paiement_liste.html', {'paiements': paiements}


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Teacher, Enseigner, Classe, Matiere, Student, Note
from .form import NoteForm

def ajouter_notes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    enseignements = Enseigner.objects.filter(teacher=teacher)
    classes = Classe.objects.filter(id__in=enseignements.values_list('classe_id', flat=True))
    matieres = Matiere.objects.filter(id__in=enseignements.values_list('matiere_id', flat=True))
    students = Student.objects.filter(classe__in=classes)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.fields['classe'].queryset = classes
        form.fields['student'].queryset = students
        form.fields['matiere'].queryset = matieres

        if form.is_valid():
            note = form.save(commit=False)

            existence_note = Note.objects.filter(student=note.student, matiere=note.matiere, teacher=teacher).first()
            if existence_note:
                messages.error(request, f"Une note existe déjà pour {note.student} dans {note.matiere}. Veuillez accéder à la liste pour la modifier.")
                return redirect('ajouter_notes', teacher_id=teacher_id)
            
            note.teacher = teacher
            note.save()
            messages.success(request, 'Note ajoutée avec succès.')
            return redirect('afficher_notes', teacher_id=teacher_id)
        else:
            messages.error(request, 'Erreur lors de l\'ajout de la note. Veuillez vérifier les informations.')
    else:
        form = NoteForm()
        form.fields['classe'].queryset = classes
        form.fields['student'].queryset = students
        form.fields['matiere'].queryset = matieres
    
    context = {
        'teacher': teacher,
        'form': form
    }
    return render(request, 'ajouter_notes.html', context)


def afficher_notes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    enseignements = Enseigner.objects.filter(teacher=teacher)
    classes = Classe.objects.filter(id__in=enseignements.values_list('classe_id', flat=True))
    students = Student.objects.filter(classe__in=classes).distinct()
    notes = Note.objects.filter(student__in=students, teacher=teacher)

    filter_student = request.GET.get('student', '')
    filter_lastname = request.GET.get('lastname', '')
    filter_class = request.GET.get('classe', '')

    if filter_student:
        notes = notes.filter(student__first_name__icontains=filter_student)
    if filter_lastname:
        notes = notes.filter(student__last_name__icontains=filter_lastname)
    if filter_class:
        notes = notes.filter(student__classe__name__icontains=filter_class)

    context = {
        'teacher': teacher,
        'classes': classes,
        'students': students,
        'notes': notes,
    }
    return render(request, 'afficher_notes.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Teacher, Note, Enseigner

def filtrer_notes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    enseignements = Enseigner.objects.filter(matiere__teacher=teacher)
    notes = Note.objects.filter(teacher=teacher, student__classe__in=enseignements.values_list('classe_id', flat=True))

    student_id = request.GET.get('student_id')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    if student_id:
        notes = notes.filter(student__id=student_id)
    elif first_name:
        notes = notes.filter(student__first_name__icontains=first_name)
    elif last_name:
        notes = notes.filter(student__last_name__icontains=last_name)

    context = {
        'notes': notes,
        'teacher': teacher,
    }
    
    return render(request, 'filtrer_notes.html', context)

def note_eleve(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    notes = Note.objects.filter(student=student)
    context = {'student':student, 'notes':notes}
    
    return render(request, 'note_eleve.html', context)

from .form import ModifierNoteForm

def modifier_notes(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        form = ModifierNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('afficher_notes', teacher_id=note.teacher.id)
    else:
        form = ModifierNoteForm(instance=note)
    
    context = {
        'form': form,
        'note': note,
        'student_name': f"{note.student.first_name} {note.student.last_name}",
        'matiere_name': note.matiere.nom_matiere,
        'classe_name': note.student.classe.name,
    }
    return render(request, 'modifier_notes.html', context)

def ajouter_classe(request, administrateur_id):
    administrateur = get_object_or_404(Administrateur, id=administrateur_id)
    
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            classe = form.save(commit=False)
            classe.administrateur = administrateur
            classe.save()
            return redirect('liste_classes') 
    else:
        form = ClasseForm()  

    return render(request, 'ajouter_classe.html', {'form': form, 'administrateur': administrateur})

def liste_classes(request):
    classes = Classe.objects.all()
    return render(request, 'liste_classe.html', {'classes': classes})

from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Teacher, Student, Enseigner, Classe

  
def prof_etudiant_list(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    enseignements = Enseigner.objects.filter(teacher=teacher)
    classes = Classe.objects.filter(id__in=enseignements.values_list('classe_id', flat=True))
    students_by_class = {classe: Student.objects.filter(classe=classe) for classe in classes}

    context = {
        'teacher': teacher,
        'classes': classes,
        'students_by_class': students_by_class,
    }
    return render(request, 'prof_etudiant_list.html', context)

  
def classes(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    students = Student.objects.filter(classe=classe)
    context = {
        'classe': classe,
        'students': students
    }
    
    return render(request, 'classes.html', context)


def details_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)

    students = classe.students.all()

    context = {
        'classe': classe,
        'students': students,
    }

    return render(request, 'details_classe.html', context)

def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'liste_salles.html', {'salles': salles})

def ajouter_salle(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salle ajoutée avec succès.')
            return redirect('ajouter_salle')
    else:
        form = SalleForm()
    
    return render(request, 'ajouter_salle.html', {'form': form})

def modifier_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('liste_classes') 
    else:
        form = ClasseForm(instance=classe)
    
    return render(request, 'modifier_classe.html', {'form': form, 'classe': classe})

def supprimer_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        classe.delete()
        return redirect('liste_classes')
    
    return render(request, 'supprimer_classe.html', {'classe': classe})

def ajouter_salle(request):
    if request.method == "POST":
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = SalleForm()
    
    return render(request, 'ajouter_salle.html', {'form': form})

def modifier_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    if request.method == "POST":
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = SalleForm(instance=salle)
    
    return render(request, 'modifier_salle.html', {'form': form, 'salle': salle})

def supprimer_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    if request.method == "POST":
        salle.delete()
        return redirect('liste_salles')
    
    return render(request, 'supprimer_salle.html', {'salle': salle})


def class_info(request):
    classes = Classe.objects.all()
    teachers = Classe.objects.all()
    students = Classe.objects.all()
    return render(request, 'class_info.html', {
        'classes': classes,
        'teachers': teachers,
        'students':students
    })

def class_list(request):
    classes = Classe.objects.all()
    return render(request, 'class_info.html', {'classes': classes})

def notes_filiere(request, responsable_id):
    responsableFiliere = get_object_or_404(ResponsableFiliere, id=responsable_id)
    classes = Classe.objects.filter(filiere__responsable=responsableFiliere)
    students = Student.objects.filter(classe__in=classes)
    notes = Note.objects.filter(student__in=students)
    
    filter_student = request.GET.get('student', '')
    filter_lastname = request.GET.get('lastname', '')
    filter_classe = request.GET.get('classe', '')

    if filter_student:
        notes = notes.filter(student__first_name__icontains=filter_student)
    if filter_lastname:
        notes = notes.filter(student__last_name__icontains=filter_lastname)
    if filter_classe:
        notes = notes.filter(student__classe__name__icontains=filter_classe)

    context = {
        'responsableFiliere': responsableFiliere,
        'classes': classes,
        'students': students,
        'notes': notes,
    }
    return render(request, 'notes_filiere.html', context)


from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import ResponsableFiliere, Classe, Note, Student

def moyenne_par_classe(request, responsable_id):
    responsable = get_object_or_404(ResponsableFiliere, id=responsable_id)
    classes = Classe.objects.filter(filiere__responsable=responsable)

    moyennes = []
    for classe in classes:
        students = Student.objects.filter(classe=classe)
        notes = Note.objects.filter(student__in=students)
        moyenne_generale = notes.aggregate(moyenne=Avg('moyen_semes'))['moyenne']
        moyennes.append({
            'classe': classe,
            'moyenne_generale': moyenne_generale,
        })

    context = {
        'responsable': responsable,
        'moyennes': moyennes,
    }
    return render(request, 'moyenne_par_classe.html', context)


# def affecter_prof(request, responsable_id):
#     responsable = get_object_or_404(ResponsableFiliere, id=responsable_id)
    
#     if request.method == 'POST':
#         form = AffecterProfForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_class') 
#     else:

#         form = AffecterProfForm()
    
#     return render(request, 'affecter_prof.html', {'form': form, 'responsable': responsable})

def teacher_class(request):

    teachers = Teacher.objects.prefetch_related('classes').all()
    return render(request, 'teacher_classe.html', {'teachers': teachers})


def Affecter_eleve(request, admin_id):
    administrateur = get_object_or_404(Administrateur, id=admin_id)
    if request.method == 'POST':
        form = AffecterEleveForm(request.POST)
        if form.is_valid():
            return redirect('liste_classe')
        else:
            form.save()
            return redirect('liste_classe')
    else:
        form = AffecterEleveForm()
        
    return render(request, 'affecter_eleve.html', {'form':form, 'administrateur':administrateur})

from .form import AffecterProfesseurForm
from .models import Administrateur, Enseigner

def affecter_professeur(request, responsable_id):
    responsable = get_object_or_404(ResponsableMetier, id=responsable_id)
    if request.method == 'POST':
        form = AffecterProfesseurForm(request.POST)
        if form.is_valid():
            return redirect('teacher_class')
    else:
        form = AffecterProfesseurForm()
    return render(request, 'affecter_professeur.html', {'form': form, 'responsable': responsable})

def teacher_class(request):
    teachers = Teacher.objects.prefetch_related('enseignements__classe').all()
    return render(request, 'teacher_classe.html', {'teachers': teachers})


def liste_classe(request):
    students = Student.objects.filter(classe__isnull=False)
    classes = Classe.objects.prefetch_related('student_set').all()
    return render(request, 'liste_classe.html', {'students': students, 'classes':classes})


def remplir_cahier(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    enseignements = Enseigner.objects.filter(teacher=teacher)
    classes = Classe.objects.filter(id__in=enseignements.values_list('classe_id', flat=True))
    
    if request.method == 'POST':
        form = CahierDeCoursForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            classe = form.cleaned_data['classe']

            if CahierDeCours.objects.filter(teacher=teacher, classe=classe, date=date).exists():
                form.add_error(None, "Vous avez déjà rempli un cahier de cours pour cette classe à cette date.")
            else:
                cahier = form.save(commit=False)
                cahier.teacher = teacher
                cahier.save()
                return redirect('liste_cahiers', teacher_id=teacher.id)
        else:
            print(form.errors)
    else:
        form = CahierDeCoursForm()

    return render(request, 'remplir_cahier.html', {'form': form, 'teacher': teacher, 'classes': classes})


def liste_cahiers(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    date_filter = request.GET.get('date', '')
    competence_filter = request.GET.get('competence', '')
    cahiers = CahierDeCours.objects.filter(teacher=teacher)
    
    if date_filter:
        cahiers = cahiers.filter(date=date_filter)
    
    if competence_filter:
        cahiers = cahiers.filter(competence__icontains=competence_filter)
    
    context = {
        'cahiers': cahiers,
        'teacher': teacher
    }
    return render(request, 'liste_cahier.html', context)

def listes_cahiers(request):
    responsable = ResponsableFiliere.objects.all()
    date_filter = request.GET.get('date', '')
    competence_filter = request.GET.get('competence', '')
    teacher_filter = request.GET.get('teacher', '')
    cahiers = CahierDeCours.objects.all()
    
    if date_filter:
        cahiers = cahiers.filter(date=date_filter)
    
    if competence_filter:
        cahiers = cahiers.filter(competence__icontains=competence_filter)
    
    if teacher_filter:
        cahiers = cahiers.filter(teacher__first_name__icontains=teacher_filter) | cahiers.filter(teacher__last_name__icontains=teacher_filter)
    
    context = {
        'cahiers': cahiers,
        'teacher': responsable
    }
    return render(request, 'cahiers_responsable.html', context)


def create_planning(request):
    resp = ResponsableFiliere.objects.all()
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            planning = form.save(commit=False)
            Planning.objects.create(
                    date=planning.date,
                    premiere_heure=planning.premiere_heure,
                    deuxieme_heure=planning.deuxieme_heure,
                    troisieme_heure=planning.troisieme_heure,
                    activite1=planning.activite1,
                    activite2=planning.activite2,
                    activite3=planning.activite3,
                    salle=planning.salle,
                    professeur=planning.professeur,
                    responsable = planning.responsable
                )
            return redirect('planning_list') 
    else:
        form = PlanningForm()
    return render(request, 'creer_planning.html', {'form': form, 'resp':resp})

def planning_list(request):
    responsable = ResponsableFiliere.objects.all()
    plannings = Planning.objects.all().order_by('-date')
    return render(request, 'planning_list.html', {
        'plannings': plannings,
        'responsable': responsable
    })

def planning_eleve(request):
    plannings = Planning.objects.all().order_by('-date')
    return render(request, 'planning_eleve.html', {
        'plannings': plannings,
    })

def edit_planning(request, pk):
    planning = get_object_or_404(Planning, id=pk)
    if request.method == 'POST':
        form = EditPlanningForm(request.POST, instance=planning)
        if form.is_valid():
            form.save()
            return redirect('planning_list')
    else:
        form = EditPlanningForm(instance=planning)
    return render(request, 'edit_planning.html', {'form': form, 'planning':planning})

def delete_planning(request, pk):
    planning = get_object_or_404(Planning, id=pk)
    if request.method == 'POST':
        planning.delete()
        return redirect('planning_list')
    return render(request, 'supprimer_planning.html', {'planning': planning})

def filter_planning(request):
    plannings = Planning.objects.all().order_by('-date')
    date = request.GET.get('date')
    
    if date:
        plannings = plannings.filter(date__icontains=date)
    return render(request, 'filter_planning.html' , {'plannings':plannings})



def success_page(request):
    return render(request, 'success.html')


from django.shortcuts import render, redirect
from PIL import Image
from .form import ImageUploadForm
from django.conf import settings
import os

def upload_and_resize_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            img = Image.open(image)

            if img.mode == 'RGBA':
                img = img.convert('RGB')
                
            img_resized = img.resize((600, 600))

            file_name = os.path.splitext(image.name)[0] + ".jpeg"
            save_path = os.path.join(settings.MEDIA_ROOT, 'student_photos', file_name)

            img_resized.save(save_path, format="JPEG") 

            return redirect('success_page')
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def envoyer_email(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        data = {
            'nom': nom,
            'email': email,
            'subject': subject,
            'message': message
        }
        
        corps = f"""
        Nouveau message de {data['nom']} :
        
        Message : {data['message']}
        
        Depuis l'email : {data['email']}
        """
        
        send_mail(
            data['subject'],
            corps,               
            '',                    
            ['laminfal29@gmail.com'] 
        )
        
        return HttpResponse("Email envoyé avec succès!")
    
    return render(request, 'mail.html', {})

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Student, Pointage

def pointage_view(request, teacher_id):
    teacher =get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        qr_data = request.POST.get('qr_data')  

        if not qr_data:
           
            messages.error(request, "QR code invalide ou non scanné.")
            return render(request, 'pointage.html')

        try:
            student_id = qr_data.split('-')[0]

            if not student_id.isdigit():
                raise ValueError("ID étudiant non valide")

            student = get_object_or_404(Student, id=int(student_id))
            
            pointage, created = Pointage.objects.get_or_create(
                student=student,
                date=timezone.now().date(),
                defaults={'arrivee': timezone.now()}
            )
            
            if not created:
                current_time = timezone.now()
                time_diff_seconds = (current_time - pointage.arrivee).total_seconds()
                
                if time_diff_seconds > 5: 
                    messages.warning(request, "Temps de pointage dépassé !")
                    return redirect('confirmation_pointage')
                
                pointage.sortie = current_time
                pointage.total = time_diff_seconds // 3600  # En heures
                pointage.save()
                messages.success(request, "Pointage de sortie enregistré avec succès.")
            else:
                messages.success(request, "Pointage d'arrivée enregistré avec succès.")
            
            return redirect('confirmation_pointage')
        except (IndexError, ValueError, Student.DoesNotExist):
            return render(request, 'error.html', {'message': 'QR code invalide ou étudiant non trouvé'})

    return render(request, 'pointage.html', {'teacher':teacher})

def confirmation_pointage(request):
    return render(request, 'confirmation_pointage.html')


