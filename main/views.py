from django.shortcuts import render

def home(request):
    context = {'title': 'Home', 'greeting': 'Welcome to My Portfolio!'}
    return render(request,'home/home.html', context)\
    
def about(request):
    context = {'title': 'About', 'description': 'I am learning Django and building a mini project!'}
    return render(request,'home/about.html',context)

def skills(request):
    context = {'title': 'Skills', 'skills': ['Python','SQL','Machine Learning', 'Big Data','Django', 'Git', 'HTML', 'CSS']}
    return render(request, 'home/skills.html', context)

def projects(request):
    context = {'title': 'Projects', 'projects': ['Personal Portfolio Site using Django','CDAC placement prediction','Image Caption Generator','Blinkit Sales Analysis using PostgreSQL','Sentiment Analysis of Amazon Reviews']}
    return render(request, 'home/projects.html', context)