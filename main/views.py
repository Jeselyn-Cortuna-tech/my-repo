from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    # replace the placeholders with your real name & student id
    context = {'name': 'Jeselyn Ann P. Cortuna', 'student_id': '2023-08196'}
    return render(request, 'about.html', context)