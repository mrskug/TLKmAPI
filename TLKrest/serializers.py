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

class MemberAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=MemberType.objects.all())

    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')

class BoardAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=BoardPosition.objects.all())
    class Meta:
        model = Board
        fields = ('pk', 'person', 'year', 'type')


class OfficialAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=OfficialType.objects.all())
    class Meta:
        model = Official
        fields = ('pk', 'person', 'year', 'type')


class MeritAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=MeritType.objects.all())
    class Meta:
        model = Merit
        fields = ('pk', 'person', 'year', 'type')


class CommitteeAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=CommitteeType.objects.all())
    class Meta:
        model = Committee
        fields = ('pk', 'person', 'year', 'type')


# Serializers define the API representation.
    # TODO:  Make separate set for adding with pk instead of "name"
class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MemberType.objects.all())
    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')

    def create(self, validated_data):
        member = Member.objects.create(**validated_data)
        return member

    def update(self, instance, validated_data):
        pass

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
