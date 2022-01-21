from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import user_login, user_register, user_dashboard, user_logout, update_profile, enroll_the_course, release_the_course
from courses.views import course_list,course_detail, search, add_course, add_category, add
from pages.views import IndexView, AboutView, ContactView

# For URL Tests:
class TestUrls(SimpleTestCase):

    def test_user_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, user_login)

    def test_user_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, user_register)

    def test_user_dashboard(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, user_dashboard)
    
    def test_user_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, user_logout)

    def test_user_update_profile(self):
        url = reverse('update_profile')
        self.assertEqual(resolve(url).func, update_profile)

    def test_user_enroll_course(self):
        url = reverse('enroll_the_course')
        self.assertEqual(resolve(url).func, enroll_the_course)

    def test_user_release_course(self):
        url = reverse('release_the_course')
        self.assertEqual(resolve(url).func, release_the_course)
        
    def test_view_course_list(self):
        url = reverse('courses')
        self.assertEqual(resolve(url).func, course_list)
        
    def test_course_detail(self):
        url = reverse('course_detail', args=[1])
        self.assertEqual(resolve(url).func, course_detail)
        
    def test_course_detail_fail(self):
        url = reverse('course_detail')
        self.assertEqual(resolve(url).func, course_detail)
        
    def test_course_category_list(self):
        url = reverse('courses_by_category', args=['technology'])
        self.assertEqual(resolve(url).func, course_list)
    
    def test_course_category_list_fail(self):
        url = reverse('courses_by_category', args=[''])
        self.assertEqual(resolve(url).func, course_list)
    
    def test_course_search(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)
    
    def test_add_course(self):
        url = reverse('add_course')
        self.assertEqual(resolve(url).func, add_course)
    
    def test_add_category(self):
        url = reverse('add_category')
        self.assertEqual(resolve(url).func, add_category)
    
    def test_add(self):
        url = reverse('add_courses_post')
        self.assertEqual(resolve(url).func, add)
    
    def test_index(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)
    
    def test_about(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, AboutView)
    
    def test_contact(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)
    
    
    
