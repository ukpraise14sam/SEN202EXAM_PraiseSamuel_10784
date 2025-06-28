from rest_framework import viewsets
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class StaffBaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.queryset
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Add role information to each item
        for item in response.data:
            obj = self.get_queryset().get(pk=item['id'])
            item['role'] = obj.get_role()
        return response

class ManagerViewSet(StaffBaseViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(StaffBaseViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

