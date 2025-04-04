from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),  # All library URLs under /library/
    path('', RedirectView.as_view(url='/library/')),  # Redirect root to /library/
]