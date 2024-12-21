from rest_framework.serializers import ModelSerializer
from .models import Todos


class TodosSerializer(ModelSerializer):
    class Meta:
        model = Todos
        fields = ['id', 'title', 'description', 'isCompleted', 'createdAt', 'updatedAt', 'user']

        extra_kwargs = {
            'createdAt': {
                'read_only': True
            },
            'updatedAt': {
                'read_only': True
            },
            'user': {
                'write_only': True
            }
        }

    