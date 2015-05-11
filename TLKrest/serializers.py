from rest_framework import serializers

from TLKdb.models import *

# "Serializers" definierar hur API:n representeras

# Medlemstyper
class MemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberType
        fields = ('pk', 'name')

# Styrelseposter
class BoardPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardPosition
        fields = ('pk', 'name')

# Utskottstyper
class CommitteeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeType
        fields = ('pk', 'name')

# Funktionärstyper
class OfficialTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficialType
        fields = ('pk', 'name')

# Förtjänstteckentyper
class MeritTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeritType
        fields = ('pk', 'name')

# Lägg till medlemmar
class MemberAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=MemberType.objects.all())

    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')

# Lägg till styrelseår
class BoardAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=BoardPosition.objects.all())
    class Meta:
        model = Board
        fields = ('pk', 'person', 'year', 'type')

# Lägg till funktionärer
class OfficialAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=OfficialType.objects.all())
    class Meta:
        model = Official
        fields = ('pk', 'person', 'year', 'type')


# Lägg till förtjänsttecken
class MeritAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=MeritType.objects.all())
    class Meta:
        model = Merit
        fields = ('pk', 'person', 'year', 'type')

# Lägg till utskott
class CommitteeAddSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='pk',
                                        queryset=CommitteeType.objects.all())
    class Meta:
        model = Committee
        fields = ('pk', 'person', 'year', 'type')

# Medlemmar
class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MemberType.objects.all())
    class Meta:
        model = Member
        fields = ('pk', 'person', 'year', 'type')
'''
    def create(self, validated_data):
        member = Member.objects.create(**validated_data)
        return member

    def update(self, instance, validated_data):
        pass
'''
# Styrelseposter
class BoardSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=BoardPosition.objects.all())
    class Meta:
        model = Board
        fields = ('pk', 'person', 'year', 'type')

# Funktionärer
class OfficialSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=OfficialType.objects.all())
    class Meta:
        model = Official
        fields = ('pk', 'person', 'year', 'type')

# Förtjänsttecken
class MeritSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=MeritType.objects.all())
    class Meta:
        model = Merit
        fields = ('pk', 'person', 'year', 'type')

# Utskott
class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=False, slug_field='name',
                                        queryset=CommitteeType.objects.all())
    class Meta:
        model = Committee
        fields = ('pk', 'person', 'year', 'type')

# Personer med undertabeller
class PersonSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, required=False, read_only=False)
    boards = BoardSerializer(many=True, required=False, read_only=False)
    officials = OfficialSerializer(many=True, required=False, read_only=False)
    merits = MeritSerializer(many=True, required=False, read_only=False)
    committees = CommitteeSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = Person
        fields = ('pk', 'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'phone', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')

# Lägg till personer
class PersonAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('pk', 'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'phone', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes',)
