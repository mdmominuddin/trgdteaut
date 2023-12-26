from django.db import models

class Svcs(models.Model):
    ARMY = 'Army'
    NAVY = 'Navy'
    AIR_FORCE = 'Air Force'
    JT_TRG = 'Jt Trg'
    AFD = 'AFD'



    SERVICE_CHOICES = [
        (ARMY, 'Army'),
        (NAVY, 'Navy'),
        (AIR_FORCE, 'Air Force'),
        (JT_TRG, 'Jt Trg'),
        (AFD, 'AFD'),
    ]

    name = models.CharField(max_length=20, choices=SERVICE_CHOICES)

    def __str__(self):
        return self.name

from django.db import models

class Sections(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='section_images/')
    # Other fields...

    def __str__(self):
        return self.name

class Indl(models.Model):
    RANK_CHOICES = [
        ('General', 'General'),
        ('Lt General', 'Lt General'),
        ('Maj General', 'Maj General'),
        ('Brig General', 'Brig General'),
        ('Colonel', 'Colonel'),
        ('Lt Colonel', 'Lt Colonel'),
        ('Major', 'Major'),
        ('Captain', 'Captain'),
        ('Lt', 'Lt'),
        ('2 Lt', '2 Lt'),
        ('MWO', 'MWO'),
        ('SWO', 'SWO'),
        ('WO', 'WO'),
        ('Sgt', 'Sgt'),
        ('Cpl', 'Cpl'),
        ('L Cpl', 'L Cpl'),
        ('Snk', 'Snk'),
        ('Civ', 'Civ'),
    ]

    Service_Number = models.CharField(max_length=200)
    Rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GovtOrder(models.Model):
    event_name = models.CharField(max_length=100, unique=True)
    svcs = models.ForeignKey(Svcs, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.event_name

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    institute_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    course_duration = models.IntegerField()
    participants = models.ManyToManyField(Indl)

    def __str__(self):
        return self.name


class CourseOffer(models.Model):
    svcs = models.ForeignKey(Svcs, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Offered: {self.course} to {self.country} by {self.svcs}"

class CourseAcceptance(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Accepted: {self.course} by {self.country}"

class Visit(models.Model):
    svcs = models.ForeignKey(Svcs, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"Visit to {self.country} by {self.svcs}"

class YearlyState(models.Model):
    pass
