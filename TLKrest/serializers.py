from rest_framework import serializers

from TLKdb.models import *


# Serializers define the API representation.

class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MemberType.objects.all())
    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')
        depth = 0

class BoardSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=BoardPosition.objects.all())
    class Meta:
        model = Board
        fields = ('pk', 'person', 'year', 'type')
        depth = 0


class OfficialSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=OfficialType.objects.all())
    class Meta:
        model = Official
        fields = ('pk', 'person', 'year', 'type')
        depth = 0


class MeritSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MeritType.objects.all())
    class Meta:
        model = Merit
        fields = ('pk', 'person', 'year', 'type')
        depth = 0


class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=CommitteeType.objects.all())
    class Meta:
        model = Committee
        fields = ('pk', 'person', 'year', 'type')
        depth = 0

class PersonSerializer(serializers.ModelSerializer):
    #members = MemberSerializer(many=True, required=False)
    #boards = BoardSerializer(many=True, required=False)
    #officials = OfficialSerializer(many=True, required=False)
    #merits = MeritSerializer(many=True, required=False)
    #committees = CommitteeSerializer(many=True, required=False)

    class Meta:
        model = Person
        fields = ('pk', 'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')
        depth = 1

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