from rest_framework import serializers

from TLKdb.models import *


class MemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberType
        fields = ('pk', 'name')

class BoardPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardPosition
        fields = ('pk', 'name')

class CommitteeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeType
        fields = ('pk', 'name')

class OfficialTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficialType
        fields = ('pk', 'name')

class MeritTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeritType
        fields = ('pk', 'name')

# Serializers define the API representation.

class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MemberType.objects.all())
    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')

class BoardSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=BoardPosition.objects.all())
    class Meta:
        model = Board
        fields = ('pk', 'person', 'year', 'type')


class OfficialSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=OfficialType.objects.all())
    class Meta:
        model = Official
        fields = ('pk', 'person', 'year', 'type')


class MeritSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MeritType.objects.all())
    class Meta:
        model = Merit
        fields = ('pk', 'person', 'year', 'type')


class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=CommitteeType.objects.all())
    class Meta:
        model = Committee
        fields = ('pk', 'person', 'year', 'type')

class PersonSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, required=False, read_only=True)
    boards = BoardSerializer(many=True, required=False, read_only=True)
    officials = OfficialSerializer(many=True, required=False, read_only=True)
    merits = MeritSerializer(many=True, required=False, read_only=True)
    committees = CommitteeSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Person
        fields = ('pk', 'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')
        #depth = 2

    '''# Untested !!
    def create(self, validated_data):
        #members_data = validated_data.pop('members')
        boards_data = validated_data.pop('boards')
        officials_data = validated_data.pop('officials')
        merits_data = validated_data.pop('merits')
        committees_data = validated_data.pop('committees')
        person = Person.objects.create(**validated_data)
        #Member.objects.create(person=person.pk, **members_data)
        Board.objects.create(person=person.pk, **boards_data)
        Official.objects.create(person=person.pk, **officials_data)
        Merit.objects.create(person=person.pk, **merits_data)
        Committee.objects.create(person=person.pk, **committees_data)
        return person

    def update(self, instance, validated_data):
        pass
    '''