from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers



User = get_user_model()


class UpdateProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                         style={'input_type': 'password'})
    new_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                         style={'input_type': 'password'})
    confirm_new_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                                 style={'input_type': 'password'})

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({
                'password': "New password fields didn't match."
            })
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({
                'password': "New password must be different from the old one."
            })

        try:
            validate_password(attrs['new_password'], user=self.context['request'].user)
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
