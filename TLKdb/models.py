from django.db import models


# Medlemstyper
class MemberType(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# Styrelseposter
class BoardPosition(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# Utskott
class CommitteeType(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# Funktionärer
class OfficialType(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# Förtjänsttecken (Guld, Silver, SGRS, Årets Werkeit, Storwerket, Hedersmedlem)
class MeritType(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

# Personer
class Person(models.Model):
    firstname = models.CharField(max_length=45)
    middlenames = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=45)
    dob = models.DateField(null=True, blank=True)
    dod = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=180, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=45, blank=True)
    joined = models.DateField(null=True, blank=True)
    graduated = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=45, blank=True)
    company_email = models.CharField(max_length=120, blank=True)
    company_phone = models.CharField(max_length=45, blank=True)
    notes = models.TextField(max_length=1000, blank=True)

#    member = models.ManyToManyField(MemberType)
#    board = models.ManyToManyField(BoardPosition)
#    committee = models.ManyToManyField(CommitteeType)
#    official = models.ManyToManyField(OfficialType)
#    merit = models.ManyToManyField(MeritType)

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)


class Member(models.Model):
    year = models.IntegerField()
    type = models.ForeignKey(MemberType, related_name='members')
    person = models.ForeignKey(Person, related_name='members')

    def __str__(self):
        return '%s %s %s' % (self.year, self.type, self.person)


class Board(models.Model):
    year = models.IntegerField()
    type = models.ForeignKey(BoardPosition, related_name='boards')
    person = models.ForeignKey(Person, related_name='boards')

    def __str__(self):
        return '%s %s %s' % (self.year, self.type, self.person)


class Official(models.Model):
    year = models.IntegerField()
    type = models.ForeignKey(OfficialType, related_name='officials')
    person = models.ForeignKey(Person, related_name='officials')

    def __str__(self):
        return '%s %s %s' % (self.year, self.type, self.person)


class Merit(models.Model):
    year = models.IntegerField()
    type = models.ForeignKey(MeritType, related_name='merits')
    person = models.ForeignKey(Person, related_name='merits')

    def __str__(self):
        return '%s %s %s' % (self.year, self.type, self.person)


class Committee(models.Model):
    year = models.IntegerField(max_length=4)
    type = models.ForeignKey(CommitteeType, related_name='committees')
    person = models.ForeignKey(Person, related_name='committees')

    def __str__(self):
        return '%s %s %s' % (self.year, self.type, self.person)
