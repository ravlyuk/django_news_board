from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Текст новости")
    name_author = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Имя автора"
    )
    published = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Опубликовано"
    )
    likes = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Понравилось"
    )
    rubric = models.ForeignKey(
        "Rubric", null=True, on_delete=models.PROTECT, verbose_name="Рубрика"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"
        ordering = ["-published"]


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    content = models.TextField(verbose_name="Комментарий")
    published = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Опубликовано"
    )
    post = models.ForeignKey(
        Bb,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Новость",
        related_query_name="entry",
    )

    def __str__(self):
        return self.content[:20] + ".."

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]
