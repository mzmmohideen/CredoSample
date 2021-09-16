from django.db import models

# Create your models here.
# Django model, provides ORM (Object Relational Mapping). an object mapped with DB. Can helps to create / alter DDL
# field Types - https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
class StudentDetails(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=100, null=False)
	dob = models.DateField()
	dept = models.CharField(max_length=4, choices=(('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH')), null=False)
	course = models.CharField(max_length=6, choices=(('BE', 'BE'), ('MCA', 'MCA'), ('B.Tech', 'B.Tech'), ('BCA', 'BCA')), null=False)
	year = models.CharField(max_length=4, null=False)

	class Meta:
		db_table = "student_details"

	def __str__(self):
		return self.student_name
