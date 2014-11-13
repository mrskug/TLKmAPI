from rest_framework import serializers

from TLKdb.models import *


# Serializers define the API representation.
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone', 'notes')


class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Member
        fields = ('year', 'type')


class BoardSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Board
        fields = ('year', 'type')


class OfficialSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Official
        fields = ('year', 'type')


class MeritSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Merit
        fields = ('year', 'type')


class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Committee
        fields = ('year', 'type')


class EverythingSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    boards = BoardSerializer(many=True)
    officials = OfficialSerializer(many=True)
    merits = MeritSerializer(many=True)
    committees = CommitteeSerializer(many=True)

    class Meta:
        model = Person
        fields = ('firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')