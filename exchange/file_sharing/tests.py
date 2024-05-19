# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Teacher, Group, Discipline, DisciplineTeacher, Record, File
# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from .views import RecordHome, about, LoginUser, logout_user, contact, ShowPost, RecordDiscipline
# #Обновленный тестовый файл
# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Teacher, Group, Discipline, DisciplineTeacher, Record, File
#
# class ModelsTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345',
#                                              first_name='John', last_name='Doe', is_staff=True)
#         self.teacher = Teacher.objects.create(user=self.user, father_name='Ivanovich')
#         self.group_user = User.objects.create_user(username='groupuser',
#                                                    password='12345', is_staff=False)
#         self.group = Group.objects.create(number=self.group_user)
#         self.discipline = Discipline.objects.create(name='Mathematics', slug='mathematics')
#         self.record = Record.objects.create(discipline=self.discipline, description='Math class',
#                                             teacher=self.teacher, slug='math-class')
#
#     def test_teacher_str(self):
#         self.assertEqual(str(self.teacher), 'Doe John Ivanovich')
#
#     def test_group_str(self):
#         self.assertEqual(str(self.group), 'groupuser')
#
#     def test_discipline_str(self):
#         self.assertEqual(str(self.discipline), 'Mathematics')
#
#     def test_record_str(self):
#         self.assertIn('Mathematics', str(self.record))
#         self.assertIn(self.record.formatted_date(), str(self.record))
#
#     def test_discipline_teacher_creation(self):
#         discipline_teacher = DisciplineTeacher.objects.create(teacher=self.teacher, discipline=self.discipline)
#         self.assertEqual(str(discipline_teacher), 'Doe John Ivanovich - Mathematics')
#
#     def test_file_creation(self):
#         file = File.objects.create(record=self.record, file='path/to/file')
#         self.assertEqual(str(file), 'path/to/file')
#
#
# # url
# class UrlsTestCase(SimpleTestCase):
#     def test_home_url_is_resolved(self):
#         url = reverse('home')
#         self.assertEqual(resolve(url).func.view_class, RecordHome)
#
#     def test_about_url_is_resolved(self):
#         url = reverse('about')
#         self.assertEqual(resolve(url).func, about)
#
#     def test_login_url_is_resolved(self):
#         url = reverse('login')
#         self.assertEqual(resolve(url).func.view_class, LoginUser)
#
#     def test_logout_url_is_resolved(self):
#         url = reverse('logout')
#         self.assertEqual(resolve(url).func, logout_user)
#
#     def test_contact_url_is_resolved(self):
#         url = reverse('contact')
#         self.assertEqual(resolve(url).func, contact)
#
#     def test_post_url_is_resolved(self):
#         url = reverse('post', args=['sample-post'])
#         self.assertEqual(resolve(url).func.view_class, ShowPost)
#
#     def test_discipline_url_is_resolved(self):
#         url = reverse('discipline', args=['sample-discipline'])
#         self.assertEqual(resolve(url).func.view_class, RecordDiscipline)
#
#
# # views
#
# class ViewsTestCase(TestCase):
#     def setUp(self):
#         # Создание пользователей
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.group_user = User.objects.create_user(username='groupuser', password='12345')
#         # Создание группы
#         self.group = Group.objects.create(number=self.group_user)
#         # Создание преподавателя и дисциплины для записи
#         self.teacher = Teacher.objects.create(user=self.user, father_name='Ivanovich')
#         self.discipline = Discipline.objects.create(name='Mathematics', slug='mathematics')
#         # Создание записи
#         self.record = Record.objects.create(
#             discipline=self.discipline,
#             description='Math class',
#             teacher=self.teacher,
#             slug='math-class',
#         )
#         self.record.group.set([self.group])
#
#     # def test_home_view(self):
#     #     self.client.login(username='groupuser', password='12345')
#     #     response = self.client.get(reverse('home'))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'home.html')
#
#     def test_about_view(self):
#         response = self.client.get(reverse('about'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'file_sharing/about.html')
#
#     def test_login_view(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'file_sharing/login.html')