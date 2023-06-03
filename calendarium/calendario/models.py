from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural="usuarios"
        ordering=['-created']

    def str(self):
        return self.name

class Evento(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='evento'
        verbose_name_plural="eventos"
        ordering=['-created']

    def str(self):
        return self.title

class Tarea(models.Model):
    id_task = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    exp_date = models.DateField()
    priority = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='tarea'
        verbose_name_plural="tareas"
        ordering=['-created']

    def str(self):
        return self.title

class Cumpleano(models.Model):
    id_bday = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='cumpleano'
        verbose_name_plural="cumpleanos"
        ordering=['-created']

    def str(self):
        return self.name

class Tracker(models.Model):
    id_tracker = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    track_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='tracker'
        verbose_name_plural="trackers"
        ordering=['-created']

    def str(self):
        return self.title

