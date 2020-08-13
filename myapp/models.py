from django.db import models


# Create your models here.
class Resumedata(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    Name = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Objective = models.CharField(max_length=100)
    Image = models.ImageField(upload_to ='image/')
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=20)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    School = models.CharField(max_length=100)
    # School Added
    School2 = models.CharField(max_length=100,null=True)
    #HSS = models.CharField(max_length=100)
    Board = models.CharField(max_length=100)
    Board2 = models.CharField(max_length=100,null=True)
    # End School
    UG = models.CharField(max_length=20,null=True)
    Branch = models.CharField(max_length=40,null=True)
    College = models.CharField(max_length=100)

    Startdate = models.CharField(max_length=30)
    Enddate = models.CharField(max_length=30)
    CGPA = models.CharField(max_length=30)
    Location = models.CharField(max_length=100)
    Employer = models.CharField(max_length=100,blank=True)
    Jobtitle = models.CharField(max_length=100,blank=True)
    JobDescription = models.CharField(max_length=250,blank=True,null=True)
    Jobcity = models.CharField(max_length=100,blank=True)
    Jobstate = models.CharField(max_length=100,blank=True,null=True)
    Jobstartdate = models.CharField(max_length=100,blank=True)
    Jobenddate = models.CharField(max_length=100,blank=True)
    #Employer 2
    Employer2 = models.CharField(max_length=100,blank=True)
    Jobtitle2 = models.CharField(max_length=100,blank=True)
    JobDescription2= models.CharField(max_length=250,blank=True,null=True)
    Jobcity2 = models.CharField(max_length=100,blank=True)
    Jobstate2 = models.CharField(max_length=100,blank=True)
    Jobstartdate2 = models.CharField(max_length=100,blank=True)
    Jobenddate2 = models.CharField(max_length=100,blank=True)
    #End Employer2
    Certification = models.CharField(max_length=100,blank=True)
    Certificationlink = models.CharField(max_length=100,blank=True)
    Certification2 = models.CharField(max_length=100,blank=True,null=True)
    Certificationlink2 = models.CharField(max_length=100,blank=True,null=True)

    Skill1 = models.CharField(max_length=100,blank=True)
    Skill2 = models.CharField(max_length=100,blank=True)
    Skill3 = models.CharField(max_length=100,blank=True)
    Skill4 = models.CharField(max_length=100,blank=True,null=True)

    Socialname1 = models.CharField(max_length=100,blank=True)
    Sociallink = models.CharField(max_length=100,blank=True)
    Socialname2 = models.CharField(max_length=100,blank=True)
    Sociallink2 = models.CharField(max_length=100,blank=True)

    Softskill1 = models.CharField(max_length=100,blank=True,null=True)
    Softskill2 = models.CharField(max_length=100,blank=True,null=True)
    Softskill3 = models.CharField(max_length=100,blank=True,null=True)
    Softskill4 = models.CharField(max_length=100,blank=True,null=True)

    About = models.CharField(max_length=500,blank=True,null=True)
    
    def __str__(self):
        return self.Name
