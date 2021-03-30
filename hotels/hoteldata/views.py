import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hotel


def index(request):
    template = "index.html"
    template1 = "new .html"
    if request.method == "POST":
        State = request.POST.get('state')
        Sort = request.POST.get('sort')
        Level = request.POST.get('level')

        if Sort == 'price' and Level== 'cheapest':
            data = Hotel.objects.filter(state=State, cost__lte=500)
            return  render(request, 'new .html', {'data': data,'state':State, 'sort': Sort, 'level':Level})

        elif Sort == 'price' and Level == 'average':
            data = Hotel.objects.filter(state=State, cost__range=[500, 1000])
            return render(request, 'new .html', {'data': data, 'state': State, 'sort': Sort, 'level': Level})

        elif Sort == 'price' and Level == 'Highest':
            data = Hotel.objects.filter(state=State, cost__gte=1000)
            return render(request, 'new .html', {'data': data, 'state': State, 'sort': Sort, 'level': Level})

        elif Sort == 'Rating' and Level == 'cheapest':
            data = Hotel.objects.filter(state=State, Rating__lte=5)
            return render(request, 'new1.html', {'data': data, 'state': State, 'sort': Sort, 'level': Level})

        elif Sort == 'Rating' and Level == 'average':
            data = Hotel.objects.filter(state=State, Rating__range=[5,6])
            return render(request, 'new1.html', {'data': data, 'state': State, 'sort': Sort, 'level': Level})

        elif Sort == 'Rating' and Level == 'Highest':
            data = Hotel.objects.filter(state=State, Rating__gte=7)
            return render(request, 'new1.html', {'data': data, 'state': State, 'sort': Sort, 'level': Level})

    context = {}
    return render(request, template, context)


def hotel(request):
    template = "upload.html"
    data = Hotel.objects.all()

    prompt = {
               'Hotel': data
              }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        print(column)
        _, created = Hotel.objects.update_or_create(
            SR_NO=column[0],
            hotel_code=column[1],
            state=column[2],
            cost=column[3],
            Rating=column[4],

               )

    context = {}
    return render(request, template, context)


