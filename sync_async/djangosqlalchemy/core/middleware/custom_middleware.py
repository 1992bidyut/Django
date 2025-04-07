# core/middleware/custom_middleware.py
import time
import logging

logger = logging.getLogger(__name__)


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time
        logger.info(f"Request to {request.path} took {duration:.2f}s")

        # Add processing time to response headers
        response['X-Processing-Time'] = f"{duration:.4f}s"

        return response