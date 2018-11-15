# Generated by Django 2.1.1 on 2018-11-14 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0015_auto_20181114_2204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('sale_stu_enrollment', '是否能够给学员报名'), ('sale_enrollment_links', '是否能够获取报名链接'), ('sale_file_upload', '是否能够上传身份证附件'), ('sale_contract_approve', '是否能够同意报名'), ('sale_enrollment_success', '是否能够去到报名成功页面'), ('student_my_course', '是否能够去我的课程展示页面'), ('student_my_class', '是否能够去到课程展示页面'), ('student_homework', '是否能够去到我的作业'), ('student_submit_homework', '是否能够提交作业'), ('student_course_record', '是否能够查看我的上课记录'))},
        ),
    ]
