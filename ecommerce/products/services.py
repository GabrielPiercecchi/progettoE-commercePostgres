from typing import List

from fastapi import HTTPException, status
from . import models


async def create_new_category(request, database) -> models.Category:
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def get_all_categories(database) -> List[models.Category]:
    categories = database.query(models.Category).all()
    return categories
