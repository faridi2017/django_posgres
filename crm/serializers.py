from rest_framework import serializers
from .models import Document, Company, Users, Leads


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        #fields = '__all__'
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'user_name',
            'user_id',
            'password',
            'cid'
        ]


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'