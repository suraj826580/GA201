from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse
# Create your views here.


def read_data_from_json():
    with open("./crud/data.json", "r") as File:
        data = json.load(File)
    return data


def Home(request):
    data = read_data_from_json()
    return JsonResponse({"data": data})


def ReadFun(request):
    data = read_data_from_json
    return render(request, "read.html", {"data": data})


def createFun(request):
    if request.method == "POST":
        user_data = request.POST
        user = {
            "id": len(read_data_from_json())+1,
            "name": user_data.get('name'),
            "age": user_data.get('age'),
            "city": user_data.get('city')
        }
        data = read_data_from_json()
        data.append(user)

        with open("./crud/data.json", "w") as File:
            json.dump(data, File, indent=4)
        return redirect('/read')
    return render(request, "create.html")


def deleteUser(request, user_id):
    user_id = int(user_id)
    data = read_data_from_json()
    data[:] = [task for task in data if task['id'] != user_id]
    with open('./crud/data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return redirect('/read')


def updateUser(request, user_id):
    print(id)
    user = read_data_from_json()

    contextUser = None
    for x in user:
        if x['id'] == user_id:
            contextUser = x

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        for updateUser in user:
            if updateUser['id'] == user_id:
                updateUser['name'] = name
                updateUser['age'] = age
                updateUser['city'] = city
        with open("./crud/data.json", "w")as File:
            json.dump(user, File, indent=4)
            return redirect("/read")
    return render(request, "update.html", {"user": contextUser})

# End Routes