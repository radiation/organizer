from django.db import models


class Course(models.Model):
    FORMAT_CHOICES = [
        ('Lecture', 'Lecture'),
        ('Recitation', 'Recitation'),
    ]
    code = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    format = models.CharField(max_length=12, choices=FORMAT_CHOICES, default='Lecture')
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['code', 'format']
        ordering = ['code']

    def __str__(self):
        return f'{self.code}' if self.format == 'Lecture' else f'{self.code} {self.format[0:3]}'

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    total_weight = models.IntegerField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'course']
        ordering = ['due_date']

    def __str__(self):
        return f'{self.course}: {self.name}'
