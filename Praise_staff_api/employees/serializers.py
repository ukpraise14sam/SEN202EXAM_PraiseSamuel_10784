from rest_framework import serializers
from .models import Manager, Intern, Address


class StaffBaseSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'role']
        
    def get_role(self, obj):
        return obj.get_role()
class ManagerSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Manager
        fields = StaffBaseSerializer.Meta.fields + ['department']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Protect sensitive field
        if not self.context.get('show_company_card', False):
            data.pop('has_company_card', None)
        return data

class InternSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Intern
        fields = StaffBaseSerializer.Meta.fields + ['mentor', 'internship_end']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

