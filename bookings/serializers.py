from rest_framework.serializers import ModelSerializer
from .models import Appointment

class AppointmentSerializer(ModelSerializer):
    """
    Serializer for the Appointment model.

    Serializes appointment data for use in REST API.

    Inherits from:
    - ModelSerializer
    """
    class Meta:
        model = Appointment
        fields = ['title', 'start_date', 'end_date']
