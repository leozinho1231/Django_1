from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


class UsuariosAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            usuarios = Usuarios.objects.all()
            serializer = UsuariosSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuarios.objects.get(id=pk)
            serializer = UsuariosSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):        
        usuarios = Usuarios.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})




class MateriasAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            materias = Materias.objects.all()
            serializer = MateriasSerializer(materias, many=True)
            return Response(serializer.data)
        else:
            materias = Materias.objects.get(id=pk)
            serializer = MateriasSerializer(materias)
            return Response(serializer.data)

    def post(self, request):
        serializer = MateriasSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        materiais = Materias.objects.get(id=pk)
        serializer = MateriasSerializer(Materias, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):
        materiais = Materias.objects.get(id=pk)
        materiais.delete()
        return Response({"msg": "Apagado com sucesso"})

