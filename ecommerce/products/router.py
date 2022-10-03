from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


