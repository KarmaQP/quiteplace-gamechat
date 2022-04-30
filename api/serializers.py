from dataclasses import field
from rest_framework import serializers
from blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    exclude = ['post']

  def to_representation(self, instance):
    rep = super(CommentSerializer, self).to_representation(instance)
    rep['user'] = instance.user.username
    return rep
