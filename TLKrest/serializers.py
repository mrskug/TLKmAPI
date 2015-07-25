from rest_framework import serializers

from TLKdb.models import *

class MemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberType
        fields = ('url', 'pk', 'name')

class BoardPositionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BoardPosition
        fields = ('url', 'pk', 'name')

class CommitteeTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommitteeType
        fields = ('url', 'pk', 'name')

class OfficialTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OfficialType
        fields = ('url', 'pk', 'name')

class MeritTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MeritType
        fields = ('url', 'pk', 'name')


# Serializers define the API representation.
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Member
        fields = ('url', 'pk', 'person', 'year', 'type')

    def create(self, validated_data):
        member = Member.objects.create(**validated_data)
        return member

    def update(self, instance, validated_data):
        pass

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Board
        fields = ('url', 'pk', 'person', 'year', 'type')


class OfficialSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Official
        fields = ('url', 'pk', 'person', 'year', 'type')


class MeritSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Merit
        fields = ('url', 'pk', 'person', 'year', 'type')


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Committee
        fields = ('url', 'pk', 'person', 'year', 'type')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    members = MemberSerializer(many=True, required=False, read_only=True)
    boards = BoardSerializer(many=True, required=False, read_only=True)
    officials = OfficialSerializer(many=True, required=False, read_only=True)
    merits = MeritSerializer(many=True, required=False, read_only=True)
    committees = CommitteeSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Person
        fields = ('url', 'pk', 'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'phone', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')
