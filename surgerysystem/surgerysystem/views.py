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

    return HttpResponse("Your(id %d) are number %d in the queue" % (patient_id, patient_queue.index(patient_id)+1))

def checkin(request, patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        raise Http404()

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

    patient_queue.remove(patient_id)

    return HttpResponse("You(id %d) have been removed from the queue. New queue is %s" % (patient_id, patient_queue))


def doctors(request):
    return HttpResponse("There are currently %d doctors in the surgery. They are in rooms %s" % (len(doctors_busy),rooms_busy))

def help_view(request):
    return HttpResponse("Command list instruction")

def login(request, doctor_id):
    try:
        doctor_id = int(doctor_id)
    except ValueError:
        raise Http404()
    doctors_avail.append(doctor_id)
    print(doctors_avail)
    return HttpResponse("Doctor %d joined." % (doctor_id))
