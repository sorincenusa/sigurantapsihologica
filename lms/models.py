from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ScormPackage(models.Model):
    course = models.ForeignKey(Course, related_name='scorm_packages', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # package_file = models.FileField(upload_to='scorm_packages/') # Commented for MVP, un-comment in production
    version = models.CharField(max_length=50, help_text="SCORM version, e.g., 1.2 or 2004")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (SCORM {self.version})"

class UserCourseProgress(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    completion_status = models.CharField(
        max_length=50,
        choices=[
            ('not_attempted', 'Not Attempted'),
            ('incomplete', 'Incomplete'),
            ('completed', 'Completed'),
            ('passed', 'Passed'),
            ('failed', 'Failed')
        ],
        default='not_attempted'
    )
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Progress for Course: {self.course.title}"
