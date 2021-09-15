from django.db import models

# Create your models here.
class StudentDetails(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=100, null=False)
	dob = models.DateField()
	dept = models.CharField(max_length=4, choices=(('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH')), null=False)
	course = models.CharField(max_length=6, choices=(('BE', 'BE'), ('MCA', 'MCA'), ('B.Tech', 'B.Tech'), ('BCA', 'BCA')), null=False)
	year = models.CharField(max_length=4, null=False)

	class Meta:
		db_table = "student_details"
