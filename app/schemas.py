import pydantic


class _BaseContact(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

    model_config = {"from_attributes": True}


class Contact(_BaseContact):
    id: int
    # date_created: _dt.datetime


class CreateContact(_BaseContact):
    pass
