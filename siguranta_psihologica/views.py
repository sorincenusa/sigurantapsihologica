from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.conf import settings
import os

def create_initial_superuser(request):
    """
    Temporary endpoint to create an initial superuser on production.
    In a real-world scenario, you should use environment variables and run this
    as a management command or secure it behind an authentication token.
    For MVP purposes, this provides a quick bootstrap on Vercel.
    """
    User = get_user_model()

    # Check if a superuser already exists to prevent abuse or duplicate attempts
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("A superuser already exists. Setup route is disabled for security.", status=403)

    try:
        # Create the superuser requested
        User.objects.create_superuser(
            username='sorin',
            email='sorin@sigurantapsihologica.ro',
            password='Admin123!'
        )
        return HttpResponse("Superuser 'sorin' created successfully. You can now login at /admin/. Please remove this route after use.")
    except Exception as e:
        return HttpResponse(f"Error creating superuser: {str(e)}", status=500)