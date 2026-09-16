from django.db import models
from django_cryptography.fields import encrypt

class EvaluationForm(models.Model):
    """
    Model that handles the psychological safety evaluation forms submitted by users.
    Best in class GDPR compliance is achieved by encrypting sensitive Personal Identifiable Information (PII).
    """

    # Encrypted fields to ensure privacy for sensitive user data
    first_name = encrypt(models.CharField(max_length=100))
    last_name = encrypt(models.CharField(max_length=100))
    email = encrypt(models.EmailField())

    # Non-sensitive / Anonymized response data
    department = models.CharField(max_length=150, help_text="Department within the organization")
    team_size = models.IntegerField(help_text="Size of the team")

    # Psychological Safety Metrics (e.g., scale 1-5)
    score_trust = models.IntegerField(help_text="Trust in team members (1-5)")
    score_speaking_up = models.IntegerField(help_text="Comfort in speaking up without fear of retaliation (1-5)")
    score_inclusion = models.IntegerField(help_text="Feeling of inclusion and belonging (1-5)")

    # Qualitative feedback - optionally encrypted if it could contain sensitive data
    additional_feedback = encrypt(models.TextField(blank=True, null=True))

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation submitted at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Psychological Safety Evaluation"
        verbose_name_plural = "Psychological Safety Evaluations"
