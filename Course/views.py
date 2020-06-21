from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_index(req: HttpRequest) -> HttpResponse:
	url_b = str.encode(req.get_full_path())
	
	return HttpResponse(b'Hello, World! := ' + url_b)
