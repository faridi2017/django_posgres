from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Document, Company, Users, Leads
from .serializers import DocumentSerializer, CompanySerializer, UsersSerializer, LeadsSerializer
from django.http import Http404
from rest_framework import status
import psycopg2
import json
from psycopg2.extras import RealDictCursor
con = psycopg2.connect(dbname='leadpoliceb', user='postgres', host='localhost', password='Bismillah@123')
def open():
    global con
    #cur = con.cursor()
    con = psycopg2.connect(dbname='leadpoliceb', user='postgres', host='localhost', password='Bismillah@123')
    cur = con.cursor(cursor_factory=RealDictCursor)
    return cur


def close(cur):
    global con
    con.commit()
    cur.close()
    con.close()
    return True


class DocumentList(APIView):
    def get(self,request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents,many=True)
        return  Response(serializer.data)


    def post(self):
        pass


class CompanyList(APIView):
    def get(self,request):
        documents = Company.objects.all()
        serializer = CompanySerializer(documents,many=True)
        return  Response(serializer.data)


    def post(self):
        pass


class UsersList(APIView):
    def get(self,request):
        documents = Users.objects.all()
        serializer = UsersSerializer(documents,many=True)
        return  Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid() and len(request.data) == 5:
            print(len(request.data))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersJoinList(APIView):
    def get(self,request):
        cursor = open()
        query = "SELECT documents.projectid FROM documents INNER JOIN project on documents.projectid = project.projectid"
        cursor.execute(query)
        records = cursor.fetchall()
        r = json.dumps(records)
        loaded_r = json.loads(r)
        return Response(loaded_r)


class LeadsList(APIView):
    def get(self,request):
        documents = Leads.objects.all()
        serializer = LeadsSerializer(documents,many=True)
        return  Response(serializer.data)


    def post(self):
        pass
# Create your views here.


