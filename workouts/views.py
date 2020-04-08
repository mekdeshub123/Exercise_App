# View.py file handles requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise
from .forms import ExerciseForm, SearchForm
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def workout_home(request):
    return render(request, 'workouts/home.html')

def workout_list(request):
    search_form = SearchForm(request.GET)
    search_term = ''
    print(search_form.is_valid())
    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']
        all_exercises = Exercise.objects.filter(name_icontains=search_term)
    else:
        all_exercises = Exercise.objects.all()
    search_form = SearchForm()
    return render(request, 'workouts/workout_list.html', {'exercises': all_exercises, 'search_term': search_term, 'search_form': search_form})

def workout_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        edited_exercise_form = ExerciseForm(request.POST, instance=exercise)
        if edited_exercise_form.is_valid():
            edited_exercise_form.save()
            return redirect('workout_list')
        else:
            messages.error(request, edited_exercise_form.errors)
            return redirect('workout_detail', pk=pk)
    else:
        exercise = get_object_or_404(Exercise, pk=pk)
        form = ExerciseFrom(instance=exercise)
        return render(request, 'workouts/workout_detail.html', {'form':form, 'exercise': exercise})  

def workout_delete(request, pk):
    if request.method == 'POST':
        exercise = get_object_or_404(Exercise, pk=pk)
        exercise.delete()
        return redirect('workout_list')
    else:
        return HttpResponseNotAllowed('Nope')

def workout_add(request):
    if request.method == 'POST':
        new_exercise_form = ExerciseForm(request.POST)
        if new_exercise_form.is_valid():
            new_exercise_form.save()#is it suppose to declare var?
            return redirect('workout_list')
        else:
            messages.error(request, new_exercise_form.errors)
            return redirect('workout_add')
    else:
        new_exercise_form = ExerciseForm()
        return render(request, 'workout_add.html', {'form':new_exercise_form})

