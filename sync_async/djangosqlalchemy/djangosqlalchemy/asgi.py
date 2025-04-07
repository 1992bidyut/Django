
# djangosqlalchemy/asgi.py
import os
import django

from django.core.asgi import get_asgi_application
from django.urls import path
from django.conf.urls import include

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosqlalchemy.settings')

# Initialize Django
django.setup()

# Import your async views here
from core.views import async_view

# Create the ASGI application
django_asgi_app = get_asgi_application()


# Define routes that should be handled by the ASGI application
async def application(scope, receive, send):
    if scope["type"] == "http":
        # Use path-based routing to direct requests
        path = scope["path"]

        # If the path is for an async view, handle it directly
        if path.startswith("/async/"):
            # Create a small ASGI app just for the async route
            async def async_app(scope, receive, send):
                # This wrapper allows our async views to be called correctly
                request = await django_asgi_app.__call__(scope, receive, send)
                return request

            return await async_app(scope, receive, send)

        # For all other paths, use the Django ASGI application
        return await django_asgi_app(scope, receive, send)

    # Handle WebSocket and lifespan protocols (if needed)
    return await django_asgi_app(scope, receive, send)
