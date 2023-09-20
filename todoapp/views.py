from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import TodoModel

# todo list
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == "GET":
        todo = TodoModel.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=202)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# get individual todo 
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    if request.method == "GET":
        todo = TodoModel.objects.get(id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == "POST":
        todo = TodoModel.objects.get(id=pk)
        serializer = TodoSerializer(instance = todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)    
    elif request.method == "DELETE":
        todo = TodoModel.objects.get(id=pk)
        todo.delete()
        return Response('Deleted successfully')
