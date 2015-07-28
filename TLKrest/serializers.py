from rest_framework import serializers

from TLKdb.models import *

class MemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberType
        fields = ('pk', 'url',  'name')

class BoardPositionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BoardPosition
        fields = ('pk', 'url',  'name')

class CommitteeTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommitteeType
        fields = ('pk', 'url',  'name')

class OfficialTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OfficialType
        fields = ('pk', 'url',  'name')

class MeritTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MeritType
        fields = ('pk', 'url',  'name')


# Serializers define the API representation.
class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ('pk', 'url',  'person', 'year', 'type')

    def create(self, validated_data):
        #member = Member.objects.create(**validated_data)
        #return member
        return Member(**validated_data)

    def update(self, instance, validated_data):
        pass

class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Board
        fields = ('pk', 'url',  'person', 'year', 'type')


class OfficialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Official
        fields = ('pk', 'url',  'person', 'year', 'type')


class MeritSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Merit
        fields = ('pk', 'url', 'person', 'year', 'type')


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Committee
        fields = ('pk', 'url',  'person', 'year', 'type')

class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('pk', 'url',  'firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'phone', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')
