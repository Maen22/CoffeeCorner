from datetime import datetime
from enum import Enum
from typing import Annotated, Optional, List
from uuid import UUID

from pydantic import BaseModel, Field, conlist, validator


class Size(Enum):
    small = 'small'
    medium = 'meduim'
    big = 'big'
    
class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'
    
class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[Annotated[int, Field(strict=True, ge=1)]] = 1
    
    @validator('quantity')
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value
    
class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)
    
        
class GetOrderSchema(BaseModel):
    id: UUID
    created: datetime
    status: Status
    order: conlist(OrderItemSchema, min_length=1)

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]