from django.db import models
from django.utils.text import slugify

class Owner(models.Model):
    name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to='owner_img')
    resume = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    kaggle_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    other_url = models.URLField(null=True, blank=True)

    marital_status = models.CharField(max_length=20, blank=True)
    languages = models.CharField(max_length=200, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    favorite_tools = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    twitter_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default='Uzbekistan')

    def __str__(self) -> str:
        return self.name

class Certificate(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=4, decimal_places=1, null= True, blank= True)
    out_of = models.DecimalField(max_digits=4, decimal_places=1, null= True, blank= True)
    given_by = models.CharField(max_length=100)
    date_achieved = models.DateField(null=True, blank=True)
    date_expire = models.DateField(null=True, blank=True)
    paper = models.FileField(upload_to='certificates', null=True, blank=True)
    image = models.ImageField(upload_to='certificate_img', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    
    def __str__(self) -> str:
        return self.title 

class Skill(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    certificate = models.ForeignKey(Certificate, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

class Tool(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='tools')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    used_years = models.DecimalField(max_digits=4, decimal_places=1)
    
    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=400)
    skills = models.ManyToManyField(Skill)
    tools = models.ManyToManyField(Tool)
    project_links = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Education(models.Model):
    EDUCATION_TYPES = [
        ('high_school', 'High School'),
        ('bachelor', 'Bachelor'),
        ('associate', 'Associate'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    ]
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='education')
    major = models.CharField(max_length=50)
    institute = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=EDUCATION_TYPES)
    start_year = models.DateField()
    end_year = models.DateField()
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    edu_languages = models.CharField(max_length=100)
    main_courses = models.TextField(max_length=300)
    focus = models.CharField(max_length=400)
    diploma = models.FileField(upload_to='diplomas')
    diploma_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='diploma_img')
    projects = models.ManyToManyField(Project, blank=True)
    
    def __str__(self) -> str:
        return self.institute


class Experience(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default='Key Achievents')
    country = models.CharField(max_length=100)
    company_links = models.URLField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tools = models.ManyToManyField(Tool)
    skills = models.ManyToManyField(Skill)
    salary = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.company}-{self.position}")
        super().save(*args, **kwargs)

class Interest(models.Model):
    INTEREST_TYPES = [
        ('hobby', 'Hobby'),
        ('professional', 'Professional'),
        ('academic', 'Academic'),
    ]
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='interests')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    link = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=INTEREST_TYPES)

    def __str__(self) -> str:
        return self.title


class Volunteer(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='volunteer_work')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)     
    end_date = models.DateField(null=True, blank=True)
    tools = models.ManyToManyField(Tool)
    skills = models.ManyToManyField(Skill)
    def __str__(self) -> str:
        return self.title


class Awards(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='awards')
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=500)
    given_by = models.CharField(max_length=100)
    given_date = models.DateField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='awards')
    link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class Cando(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cando')
    action = models.CharField(max_length=100)
    tool_to_use = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.action

class Languages(models.Model):
    title = models.CharField(max_length=100)
    
