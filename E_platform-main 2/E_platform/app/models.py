from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type_choices = ((1, 'ADMIN'),
                         (2, 'STUDENT'),
                         (3, 'COURSE PROVIDER'))
    user_type = models.IntegerField(choices=user_type_choices, default=1)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Course(models.Model):
    TECH_COURSE = 'Tech Courses'
    CBSE_COURSE = 'CBSE Courses'
    CATEGORY_CHOICES = [
        (TECH_COURSE, 'Tech Courses'),
        (CBSE_COURSE, 'CBSE Courses'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    what_you_will_learn = models.TextField(null=True, blank=True, verbose_name="What You Will Learn")
    this_course_includes = models.TextField(null=True, blank=True, verbose_name="This Course Includes")

    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=TECH_COURSE)
    image = models.ImageField(upload_to='staticfiles/course_images/', null=True, blank=True)
    demo_video = models.FileField(upload_to='staticfiles/demo_videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=20, null=True, blank=True)
    Mobile_no = models.CharField(max_length=10, null=True, blank=True)
    EmailID = models.EmailField(max_length=255, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    Gender = models.CharField(max_length=10, choices=Gender_choices, default='M')
    cart = models.ManyToManyField('Course', related_name='students_in_cart')
    wishlist = models.ManyToManyField('Course', related_name='students_in_wishlist')

    def __str__(self) -> str:
        return self.Full_Name

class Week(models.Model):
    course = models.ForeignKey(Course, related_name='weeks', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Week {self.number}: {self.title}"


class Topic(models.Model):
    week = models.ForeignKey(Week, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='staticfiles/topic_videos/', null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def has_video(self):
        return bool(self.video_file or self.video_link)

    def get_video_url(self):
        if self.video_file:
            return self.video_file.url
        elif self.video_link:
            return self.video_link
        else:
            return None





class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.user} enrolled in {self.course.title}"


class Mentorship(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    reason = models.TextField()
    phone_number = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Assuming each mentorship is associated with a course
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mentorship for {self.user.username}"


class QuestionPaper(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='question_papers/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Ticket(models.Model):
    REASON_CHOICES = [
        ('Payment Methods', 'Payment Methods'),
        ('Refund a Course', 'Refund a Course'),
        ('Troubleshoot Payment Failure', 'Troubleshoot Payment Failure'),
        ('Download Course Resources', 'Download Course Resources'),
        ('Enrollment', 'Enrollment'),
        ('Grades & Assignments', 'Grades & Assignments'),
        ('Video Library', 'Video Library'),
        ('Trust & Safety', 'Trust & Safety'),
        ('Find a missing course', 'Find a missing course'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='staticfiles/tickets/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Open')

    def __str__(self):
        return f"Ticket #{self.id} - {self.user.email}"
