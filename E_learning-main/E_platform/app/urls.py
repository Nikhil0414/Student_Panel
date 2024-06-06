from django.urls import path
from.views import *


urlpatterns = [
    path('',do_login,name='login'),
    path('student-signup/',student_signup,name='student-signup'),
    path('verify-otp',verify_otp,name='verify_otp'),
    path('logout/', logout_user, name='logout'),

    path('course_catalog', course_catalog, name='course_catalog'),
    path('career_roadmap', career_roadmap, name='career_roadmap'),

    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('course/<int:course_id>/', view_course_details, name='view_course_details'),
    path('enroll-course/<int:course_id>/', enroll_course, name='enroll_course'),
    path('course_payment/<int:course_id>/', course_payment, name='course_payment'),
    path('enrolled-courses/', all_course_progress, name='enrolled_course'),
    path('enrolled-courses/<int:course_id>/start-course', start_course, name='start_course'),
    path('start-course/<int:course_id>/previous_question_papers/', previous_question_papers,
         name='previous_question_papers'),

    path('add-to-cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:course_id>/', remove_from_cart, name='remove_from_cart'),

    path('add_to_wishlist/<int:course_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/remove/<int:course_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    path('support/', support, name='support'),


    path('update_profile/', update_profile, name='update_profile'),
    path('account_security/', account_security, name='account_security'),
    path('educational_details/', educational_details, name='educational_details'),
    path('add_work_experience/', add_work_experience, name='add_work_experience'),
    path('add_education/', add_education, name='add_education'),
    path('add_project/', add_project, name='add_project'),
    path('privacy_settings/', privacy_settings, name='privacy_settings'),
    path('notification_settings/', notification_settings, name='notification_settings'),
    path('referrals/', referrals, name='referrals'),
    path('payment_history/', payment_history, name='payment_history'),


    path('courses/<int:course_id>/add_note/', add_note, name='add_note'),
    path('courses/<int:course_id>/get_notes/', get_notes, name='get_notes'),
    path('courses/<int:course_id>/messages/', get_messages, name='course_messages'),
    path('courses/<int:course_id>/messages/json/', get_course_messages_json, name='get_course_messages_json'),
    path('courses/<int:course_id>/career_guidance/json/', get_career_guidance_json, name='get_career_guidance_json'),
    path('courses/<int:course_id>/resources/json/', get_course_resources_json, name='get_course_resources_json'),
    path('courses/<int:course_id>/discussions/json/', get_discussions, name='get_discussions'),
    path('courses/<int:course_id>/add_discussion/', add_discussion, name='add_discussion'),

    path('certificate/', certificate, name='certificates'),
    path('download-certificate/<int:certificate_id>/', download_certificate, name='download-certificate'),
    path('my_courses', all_course_progress, name='my-courses'),
    path('question-papers', question_papers, name='question_papers'),
    path('question-paper/<int:pk>/', view_question_paper, name='view_question_paper'),
    path('question-paper/<str:pk>/download/', download_question_paper, name='download_question_paper'),
    path('course/<int:course_id>/topic/<int:topic_id>/', watch_topic, name='watch_topic'),
    path('quiz/<int:quiz_id>/', display_quiz, name='display_quiz'),
    path('quiz/<int:quiz_id>/result/', quiz_result, name='quiz_result'),

    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:post_id>/', blog_detail, name='blog_detail'),
    path('blog/new/', blog_create, name='blog_create'),
    path('blog/<int:post_id>/edit/', blog_update, name='blog_update'),
    path('blog/<int:post_id>/delete/', blog_delete, name='blog_delete'),

    path('mentorship/', mentorship_form, name='mentorship_form'),

]