from django.shortcuts import render
from django.shortcuts import redirect


from core.form import TodoForm

from core.models import Todo


def home(req):
	
	form = TodoForm()
	todos = Todo.objects.all()
	if req.method == 'POST':
		form = TodoForm(req.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(req, 'home.html',{'form': form, 'todos': todos})
	
	
	
def update(req, todo):
    todo = Todo.objects.get(id=todo)
    form = TodoForm(instance=todo)
    if req.method == 'POST':
        form = TodoForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'update.html',{'form': form})


    
	
	
	
def delete(req, todo):
	
	if req.method == 'POST':
		todo = Todo.objects.get(id=todo).delete()
		return redirect('home') 
