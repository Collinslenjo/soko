from rest_framework.permissions import BasePermission
from .models import *

class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if isinstance(obj, Book):
			return obj.owner == request.user
		return obj.owner == request.user