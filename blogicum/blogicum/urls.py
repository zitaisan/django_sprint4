from django.contrib import admin
from django.urls import include, path, reverse_lazy
from users.forms import MyUserForm
from django.views.generic.edit import CreateView

handler403 = "pages.views.csrf_failure"
handler404 = "pages.views.page_not_found"
handler500 = "pages.views.server_error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('posts/', include('blog.urls')),
    path('category/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('profile/', include('blog.urls')),
    path("auth/", include("django.contrib.auth.urls")),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=MyUserForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
    path("", include("users.urls", namespace="users")),
]
