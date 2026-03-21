from django.db import models

class ContactMessage(models.Model):
    """Represents a contact message submitted by users."""
    name = models.CharField(max_length=100, verbose_name="Your Name")
    contact_number = models.CharField(max_length=20, verbose_name="Contact Number")
    message = models.TextField(verbose_name="Your Message")
    submission_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Submission Time")

    class Meta:
        db_table = 'ContactMessage'  # Explicitly set the table name
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-submission_datetime']

    def __str__(self):
        return f"{self.name} - {self.submission_datetime.strftime('%Y-%m-%d %H:%M:%S')}"# # In your app's models.py file
