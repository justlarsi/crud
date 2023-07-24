from django.shortcuts import render
from CRUD.models import People
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = People(name=name, email=email, school=school)
        person.save()

        d = People.objects.all()
        return render(request, 'index.html', {"data": d})


def delete(request, id):
    dd = People.objects.get(id=id)
    dd.delete()

    return HttpResponse("Delete successfully")


def update(request, id):
    u = People.objects.get(id=id)

    return render(request, 'update.html', {"u": u})

#         print(name, school, email)
#         return render(request, 'index.html')
#
#
# def people(request):
#     d = People.objects.all()
#     return render(request, 'people.html', {"data": d})
