from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'account_name', 'date', 'post']
        read_only_fields = ['id', 'account_name', 'date']

    def get_account_name(self, obj):
        return obj.account.name
