from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


@api_view()
def home(request):
    return Response(
        {
            'message': 'Hallo Leute'
        }
    )


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'Botschaft: Erfolgreich erschaffen'
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_detail(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'Botschaft: Erfolgreich aktualisiert'
        }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({
        "message": "Erfolgreich gelöscht",
    }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    else:
        serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'Botschaft: Erfolgreich erschaffen'
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    match request.method:
        case 'GET':
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)

        case 'PUT':
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Botschaft: Erfolgreich aktualisiert'
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    "message": "Data not validated",
                    "data": serializer.data
                }, status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            student.delete()
            return Response({
                "message": "Erfolgreich gelöscht",
            }, status=status.HTTP_204_NO_CONTENT)
