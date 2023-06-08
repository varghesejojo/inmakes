from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from . models import Crud

# Create your views here.
def home(request):
    obj=Crud.objects.all()
    if request.method=="POST":
        slnumber=request.POST.get('slnumber')
        itemname=request.POST.get('itemname')
        description=request.POST.get('description')
        items=Crud(slnumber=slnumber,itemname=itemname,description=description)
        items.save()

    return render(request, 'home.html',{'result':obj})
def delete(request,taskid):
    items=Crud.objects.get(id=taskid)
    if request.method == "POST":
        items.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    
    task1=Crud.objects.get(id=id)
    if request.method=="POST":
        slnumber=request.POST.get('slnumber','')
        itemname=request.POST.get('itemname','')
        description=request.POST.get('description','')
        task1.slnumber=slnumber
        task1.itemname=itemname
        task1.description=description
        task1.save()
        return redirect('/')
    return render(request,'update.html',{"task1":task1})





 
class ItemList(ListView):
 
    # specify the model for list view
    model = Crud
    template_name='itemlist.html'