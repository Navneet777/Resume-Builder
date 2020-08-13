from django.shortcuts import render ,redirect
from myapp.models import Resumedata
# Create your views here.
def index(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Occupation = request.POST['Occupation']
        Objective = request.POST['Objective']
        Image = request.POST['Image']
        Email = request.POST['Email']
        Phone = str(request.POST['Phone'])
        Country = request.POST['Country']
        State = request.POST['State']
        Address = request.POST['Address']
        School = request.POST['School']
        School2 = request.POST['School2']
        College = request.POST['College']
        Board = request.POST['Board']
        Board2 = request.POST['Board2']
        UG = request.POST['UG']
        Branch = request.POST['Branch']
        Startdate = str(request.POST['Startdate'])
        Enddate = str(request.POST['Enddate'])
        CGPA = str(request.POST['CGPA'])
        Location = request.POST['Location']
        Employer = request.POST['Employer']
        Jobtitle = request.POST['Jobtitle']
        JobDescription = request.POST['JobDescription']
        Jobcity = request.POST['Jobcity']
        Jobstate = request.POST['Jobstate']
        Jobstartdate = str(request.POST['Jobstartdate'])
        Jobenddate = str(request.POST['Jobenddate'])

        Employer2 = request.POST['Employer2']
        Jobtitle2 = request.POST['Jobtitle2']
        JobDescription2 = request.POST['JobDescription2']
        Jobcity2 = request.POST['Jobcity2']
        Jobstate2 = request.POST['Jobstate2']
        Jobstartdate2 = str(request.POST['Jobstartdate2'])
        Jobenddate2 = str(request.POST['Jobenddate2'])


        Certification = request.POST['Certification']
        Certificationlink = str(request.POST['Certificationlink'])
        Certification2 = request.POST['Certification2']
        Certificationlink2 = str(request.POST['Certificationlink2'])
        Skill1 = request.POST['Skill1']
        Skill2 = request.POST['Skill2']
        Skill3 = request.POST['Skill3']
        Skill4 = request.POST['Skill4']
        Socialname1 = request.POST['Socialname1']
        Sociallink = str(request.POST['Sociallink'])
        Socialname2 = request.POST['Socialname2']
        Sociallink2 = str(request.POST['Sociallink2'])
        Softskill1 = request.POST['Softskill1']
        Softskill2 = request.POST['Softskill2']
        Softskill3 = request.POST['Softskill3']
        Softskill4 = request.POST['Softskill4']

        About = request.POST['About']
        resume_data=Resumedata.objects.create(Name=Name,Occupation=Occupation,Objective=Objective,Image=Image,Email=Email,Phone=Phone,Country=Country,State=State,Address=Address,School=School,School2=School2,Board2=Board2,UG=UG,Branch=Branch,College=College,Board=Board,Startdate=Startdate,Enddate=Enddate,CGPA=CGPA,Location=Location,Employer=Employer,Jobtitle=Jobtitle,JobDescription=JobDescription,Jobcity=Jobcity,Jobstate=Jobstate,Jobstartdate=Jobstartdate,Jobenddate=Jobenddate,Employer2=Employer2,Jobtitle2=Jobtitle2,JobDescription2=JobDescription2,Jobcity2=Jobcity2,Jobstate2=Jobstate2,Jobstartdate2=Jobstartdate2,Jobenddate2=Jobenddate2,Certification=Certification,Certificationlink=Certificationlink,Certification2=Certification2,Certificationlink2=Certificationlink2,Skill1=Skill1,Skill2=Skill2,Skill3=Skill3,Skill4=Skill4,Socialname1=Socialname1,Sociallink=Sociallink,Socialname2=Socialname2,Sociallink2=Sociallink2,Softskill1=Softskill1,Softskill2=Softskill2,Softskill3=Softskill3,Softskill4=Softskill4,About=About)
        resume_data.save()
        print(resume_data)
        return redirect('myresume')
    return render(request,'index.html')

def myresume(request):
    rs = Resumedata.objects.latest('created_on')

    return render(request,'eps.html',{'rs':rs})

def myresume2(request):
    rs = Resumedata.objects.latest('created_on')

    return render(request,'psd.html',{'rs':rs})
