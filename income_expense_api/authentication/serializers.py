from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 100, min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')


        # check if username is alphanumeric
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphabet and number characters only'
            )
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)