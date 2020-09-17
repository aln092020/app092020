from django.db import models
from quiz.models import Question

ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    # ('none', 'None'),
    # ('random', 'Random')
)


class MCQQuestion(Question):

    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="Порядок, в котором отображаются варианты ответов пользователю",
        verbose_name="Порядок ответов")

    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        # if self.answer_order == 'random':
        #     return queryset.order_by('Random')
        if self.answer_order == 'none':
            return queryset.order_by('None')

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(Answer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    class Meta:
        verbose_name = "Вопрос с вариантами ответов"
        verbose_name_plural = "Вопрос с вариантами ответов"


class Answer(models.Model):
    question = models.ForeignKey(MCQQuestion, verbose_name='Вопрос', on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Введите текст ответа который хотите отобразить",
                               verbose_name="Content")

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Правильный ответ?",
                                  verbose_name="Правильный")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"





