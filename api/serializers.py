from rest_framework import serializers
from .models import Contributions, Contributors
from accounts.models import User
from django.conf import settings


class ContributorSerializers(serializers.ModelSerializer):
    # Contributions = ContributionSerializers(read_only=True)
    full_name = serializers.CharField(source="user.full_name", read_only=True)

    class Meta:
        model = Contributors
        fields = [
            "Contributions",
            "id",
            "user",
            "full_name",
            "amount",
            "created_at",
        ]


class ContributionSerializers(serializers.ModelSerializer):
    contributors = ContributorSerializers(many=True, read_only=True)
    targeted_user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Contributions
        fields = [
            "id",
            "title",
            "description",
            "user",
            "targeted_user",
            "created_at",
            "updated_at",
            "contributors"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "contributors"]

    def create(self, validated_data):
        user = self.context["user"]
        contributions = Contributions.objects.create(user=user, **validated_data)
        return contributions
