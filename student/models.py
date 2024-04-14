from django.db import models

# Create your models here.
from django.utils.html import format_html


class Student(models.Model):
    '''学员信息[表的定义，相关操作]'''
    studentName = models.CharField('学员姓名', max_length=255)
    studentAge = models.IntegerField('学员年龄', null=True, blank=True)

    class Meta:
        verbose_name = '学员信息管理'
        verbose_name_plural = '学员信息列表'

    def __str__(self):
        return self.studentName


class Contact(models.Model):
    '''联系方式'''
    info = models.CharField('联系方式', max_length=16)
    Student = models.ForeignKey("Student", on_delete=models.CASCADE, verbose_name='学生信息')

    class Meta:
        verbose_name = '联系方式'
        verbose_name_plural = '联系方式列表'  # 复数--展示多个

    # 行级按钮
    def alert(self):
        btn = '<input type = "button" value = "点我弹出" onclick="javascript:alert(\'' + self.studentName + '\');" >'
        return format_html(btn)

    alert.short_description = '操作'

    def __str__(self):
        return ''


class ExamInfo(models.Model):
    '''考试信息'''
    score = models.IntegerField('分数')
    remark = models.CharField('备注', max_length=100)
    Student = models.ForeignKey("Student", on_delete=models.CASCADE, verbose_name='考试信息')

    class Meta:
        verbose_name = '考试信息1'
        verbose_name_plural = '考试信息1列表'  # 复数--展示多个

    def __str__(self):
        return ''


class ExamDetailInfo(models.Model):
    '''考试信息'''
    account = models.CharField('科目', max_length=10)
    score = models.IntegerField('分数')
    remark = models.CharField('备注', max_length=100)
    ExamInfo = models.ForeignKey("ExamInfo", on_delete=models.CASCADE, verbose_name='考试详情')

    class Meta:
        verbose_name = '考试详情1'
        verbose_name_plural = '考试详情1列表'  # 复数--展示多个

    def __str__(self):
        return ''
