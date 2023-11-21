from typing import Optional
from pydantic import BaseModel

# This is the base class for representing a customer.
class CustomerBase(BaseModel):
    customer_name: str
    phone_number: Optional[int]
    address: str
    payment_info: str

#  This class inherits from OrderDetailBase and is used specifically for creating new order details.
class CustomerCreate(CustomerBase):
    pass

# This class is used for updating existing order details. Unlike the create class, all fields here are optiona
class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_number: Optional[int]
    address: Optional[str]
    payment_info: Optional[str]


class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True
