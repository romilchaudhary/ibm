from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=30, verbose_name="Question")
    pub_date = models.DateField('Date Published')

    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        db_table = "Questions_new"
    ques = models.Manager()


from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

@receiver([post_save, pre_save], sender=Question)
def my_callback(sender, **kwargs):
    print("Model Saved")

@receiver(pre_delete, sender=Question)
def delete(sender, **kwargs):
    print("are you sure to want to delete!")


