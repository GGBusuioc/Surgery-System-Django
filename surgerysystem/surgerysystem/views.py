from django.http import HttpResponse
import datetime
import requests


patient_queue = []
rooms = [1,2,3,4,5,6,7,8,9,10]
doctors_avail = []
rooms_busy = []


def position(request, patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        raise Http404()
    if request.method == "GET":
        return HttpResponse("Your(id %d) are number %d in the queue" % (patient_id, patient_queue.index(patient_id)+1))

def checkin(request, patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        raise Http404()

    if request.method == "POST":
        patient_queue.append(patient_id)

        if doctors_avail:
            doctors_avail.pop(0)
            room_number = rooms[0]
            rooms.pop(0)
            return HttpResponse("Please proceed to room %d" %  (room_number))
        else:
            return HttpResponse("All doctors are busy right now, please relax in the waiting area. You are number %d in the queue." % (patient_queue.index(patient_id)+1))

def delete(request, patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        raise Http404()

    if request.method == "DELETE":
        patient_queue.remove(patient_id)
        return HttpResponse("You(id %d) have been removed from the queue. New queue is %s" % (patient_id, patient_queue))


def doctors(request):
    if request.method == "GET":
        return HttpResponse("There are currently %d doctors available in the surgery. They are in rooms %s" % (len(doctors_avail), rooms_busy))

def help_view(request):
    if request.method == "GET":
        return HttpResponse("Command list instruction")

def login(request, doctor_id):
    password = "password"
    # ask the user for a password and check if the third argument is the correct password
    # if it is, send an ok which will be checked atthe client side 

    try:
        doctor_id = int(doctor_id)
    except ValueError:
        raise Http404()

    if request.method == "POST":
        doctors_avail.append(doctor_id)
        if patient_queue:
            first_patient = patient_queue[0]
            patient_queue.pop(0)
            doctors_avail.remove(doctor_id)

            return HttpResponse("DOCTOR %d joined and had taken PATIENT %d to a room." % (doctor_id, first_patient))
        else:
            return HttpResponse("There are no patients waiting!")
