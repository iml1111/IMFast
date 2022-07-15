from fastapi import Request
from starlette_context import context


async def parse_request_body(request: Request):
    """Parse Request Body as JSON"""
    method = str(request.method).upper()
    # only RESTful API support body
    if method in ('GET', 'DELETE', 'POST', 'PUT'):
        context.update(body=await request.body())
