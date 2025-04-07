# core/views.py
import asyncio
import time
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
import json

from sqlalchemy.orm import Session
from .system.sqlalchemy_models import engine, SQLAUser
from .models import User

# Simple synchronous index view with template
def index(request):
    return render(request, 'core/index.html')


# Synchronous view using SQLAlchemy
def sync_view(request):
    start_time = time.time()

    # Using SQLAlchemy session
    session = Session(engine)
    try:
        users = session.query(SQLAUser).all()
        user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    finally:
        session.close()

    duration = time.time() - start_time

    return JsonResponse({
        "message": "Data fetched synchronously",
        "processing_time": f"{duration:.4f}s",
        "users": user_list
    })


# Asynchronous view
async def async_view(request):
    start_time = time.time()

    # Simulate async operation
    await asyncio.sleep(0.1)

    # Using SQLAlchemy through sync_to_async
    @sync_to_async
    def get_users():
        session = Session(engine)
        try:
            users = session.query(SQLAUser).all()
            return [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        finally:
            session.close()

    user_list = await get_users()

    duration = time.time() - start_time

    return JsonResponse({
        "message": "Data fetched asynchronously",
        "processing_time": f"{duration:.4f}s",
        "users": user_list
    })


# User CRUD operations using Django ORM
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        return JsonResponse({"users": data})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                username=data.get('username'),
                email=data.get('email')
            )
            return JsonResponse({
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'GET':
        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.save()
            return JsonResponse({
                "id": user.id,
                "username": user.username,
                "email": user.email
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=204)

    return JsonResponse({"error": "Method not allowed"}, status=405)