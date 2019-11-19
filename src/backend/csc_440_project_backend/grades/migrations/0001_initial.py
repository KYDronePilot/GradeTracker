# Generated by Django 2.2.4 on 2019-11-18 13:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import grades.models.semester


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('weight', models.FloatField(null=True, verbose_name='Weight')),
                ('max_points', models.FloatField(null=True, verbose_name='Max Points')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Concentration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('code', models.CharField(max_length=20, verbose_name='Course Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('credit_hours', models.FloatField(verbose_name='Credit Hours')),
                ('is_deprecated', models.BooleanField(default=False, verbose_name='Is Deprecated')),
                ('is_gen_ed', models.BooleanField(help_text='Whether the course is a general education requirement', verbose_name='Gen Ed')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('year', models.SmallIntegerField(verbose_name='Year')),
                ('season', models.CharField(choices=[('fall', 'Fall'), ('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer')], max_length=20, validators=[grades.models.semester.validate_season], verbose_name='Season')),
                ('colleges', models.ManyToManyField(related_name='semesters', to='grades.College')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('course_count', models.PositiveSmallIntegerField(help_text='Number of directly related courses that must be completed to fulfill the requirement', null=True, verbose_name='Course Count')),
                ('sub_requirement_count', models.PositiveSmallIntegerField(help_text='Number of sub-requirements which must be completed to fulfill the requirement', null=True, verbose_name='Sub Requirement Count')),
                ('sub_requirement_course_count', models.PositiveSmallIntegerField(help_text='Number of courses in directly related sub-requirements that must be completed to fulfill the requirement (including courses in sub-requirements that must be fulfilled)', null=True, verbose_name='Sub Requirement Course Count')),
                ('is_required', models.BooleanField(help_text='Set to false when requirement is one of many sub-requirements which do not all need to be completed', verbose_name='Required')),
                ('concentration', models.ForeignKey(help_text='Concentration the requirement is for (if not a sub-requirement)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='grades.Concentration', verbose_name='Concentration')),
                ('super_requirement', models.ForeignKey(help_text='Parent requirement which this requirement is a sub-requirement of (if sub-requirement)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_requirements', to='grades.Requirement', verbose_name='Parent Requirement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='grades.College', verbose_name='College')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GradeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('points', models.FloatField(help_text='Number of points obtained', verbose_name='Points')),
                ('max_points', models.FloatField(help_text='Maximum number of points possible', verbose_name='Max Points')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_entries', to='grades.Category', verbose_name='Category')),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='grade_entries', to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('grading_strategy', models.CharField(choices=[('point_based', 'Point Based'), ('weight_based', 'Weight Based')], max_length=20, verbose_name='Grading Strategy')),
                ('min_a', models.FloatField(help_text="Minimum score to get an 'A'", verbose_name="Minimum 'A' Score")),
                ('min_b', models.FloatField(help_text="Minimum score to get a 'B'", verbose_name="Minimum 'B' Score")),
                ('min_c', models.FloatField(help_text="Minimum score to get a 'C'", verbose_name="Minimum 'C' Score")),
                ('min_d', models.FloatField(help_text="Minimum score to get a 'D'", verbose_name="Minimum 'D' Score")),
                ('max_points', models.FloatField(null=True, verbose_name='Maximum number of points attainable')),
                ('section', models.PositiveSmallIntegerField(verbose_name='Section Number')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instances', to='grades.Course', verbose_name='Course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instances', to='grades.Semester', verbose_name='Semester')),
                ('students', models.ManyToManyField(related_name='course_instances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='requirements',
            field=models.ManyToManyField(blank=True, related_name='courses', to='grades.Requirement'),
        ),
        migrations.AddField(
            model_name='concentration',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concentrations', to='grades.Major', verbose_name='Major'),
        ),
        migrations.CreateModel(
            name='CategoryScoreRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('min_a', models.FloatField(help_text="Minimum score in each category to get an 'A'", verbose_name="Minimum 'A' Score")),
                ('min_b', models.FloatField(help_text="Minimum score in each category to get a 'B'", verbose_name="Minimum 'B' Score")),
                ('min_c', models.FloatField(help_text="Minimum score in each category to get a 'C'", verbose_name="Minimum 'C' Score")),
                ('min_d', models.FloatField(help_text="Minimum score in each category to get a 'D'", verbose_name="Minimum 'D' Score")),
                ('course_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_score_requirements', to='grades.CourseInstance', verbose_name='Course Instance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='category_score_requirements',
            field=models.ManyToManyField(related_name='categories', to='grades.CategoryScoreRequirement'),
        ),
        migrations.AddField(
            model_name='category',
            name='course_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='grades.CourseInstance'),
        ),
        migrations.AddField(
            model_name='user',
            name='colleges',
            field=models.ManyToManyField(related_name='students', to='grades.College'),
        ),
        migrations.AddField(
            model_name='user',
            name='concentrations',
            field=models.ManyToManyField(related_name='students', to='grades.Concentration'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='majors',
            field=models.ManyToManyField(related_name='students', to='grades.Major'),
        ),
        migrations.AddField(
            model_name='user',
            name='semesters',
            field=models.ManyToManyField(related_name='students', to='grades.Semester'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]