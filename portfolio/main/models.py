from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about_me = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resume/', null=True, blank=True)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('tiktok', 'TikTok'),
        ('spotify', 'Spotify'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.profile.name}'s {self.platform}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('data_science', 'Data Science'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)  # Percentage

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50)  # For font-awesome or other icon classes

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.company}"