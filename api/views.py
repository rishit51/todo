from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('Routes:')



@api_view(['GET','POST'])
def getNotes(request):
    if request.method=="POST":
        data=request.data
        serializer=NoteSerializer(data=data,many=False)
        if serializer.is_valid():
            serializer.save()
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def getNote(request,id):
    if request.method=="DELETE":
        note=Note.objects.get(id=id)
        note.delete()
    if request.method=="PUT":
        data=request.data
        note=Note.objects.get(id=id)
        serializer=NoteSerializer(data=data,instance=note,many=False)
        if serializer.is_valid():
            serializer.save()
  


    note=Note.objects.get(id=id)
    serializer=NoteSerializer(note)

    
    return Response(serializer.data)




  


