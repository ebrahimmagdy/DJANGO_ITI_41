from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from products.models import Department
from products.models import Item
from products.models import *

def index(request):
    # list all items from databas
    items = Item.objects.all()
    # all_items = items
    # for index in items:
    #     all_items[index]['department'] = Department.objects.values('title')
    # render template to view the items
    return render(request, 'item/index.html', {'all_items': items})

# function to read data about one item
def read(request, item_id):
    # query to get data about specific item
    # item = Item.objects.get(id=item_id)
    item = get_object_or_404(Item, id=item_id)
    # render template to display the data 
    return render(request, 'item/read.html' , {'item_data' : item})

def category(request, category_id):
    # list all items from databas
    items = Item.objects.filter(department=category_id)
    # all_items = items
    # for index in items:
    #     all_items[index]['department'] = Department.objects.values('title')
    # render template to view the items
    return render(request, 'item/index.html', {'all_items': items})    
# def add(request):
#     # list departments
#     departments = Department.objects.all()
#     return render(request, 'item/add.html', {'all_departments' : departments})

# def save(request):
#     # read data from request
#     # get from request the x variable
#     # print(request.GET.get('description'))
#     # return HttpResponse(request.GET)
#     selected_department = Department.objects.get(id = request.POST.get('department_id'))
#     Item.objects.create(
#         name= request.POST.get('name'), description= request.POST.get('description') ,
#         price=request.POST.get('price') , department= selected_department)
#     # return HttpResponse('data saved')
#     return redirect('item_list')



def create(request):
    if request.method == "GET":
        # list departments
        departments = Department.objects.all()
        return render(request, 'item/add.html', {'all_departments' : departments})
    else:
        selected_department = Department.objects.get(id = request.POST.get('department_id'))
        Item.objects.create(
            name= request.POST.get('name'), description= request.POST.get('description') ,
            price=request.POST.get('price') , department= selected_department , 
            photo=request.POST.get('photo'))
        # return HttpResponse('data saved')
        return redirect('item_list')

def delete(request, item_id):
    # return HttpResponse ('hello from delete')
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('item_list')

















