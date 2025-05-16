from typing import Annotated
import fastapi as _fastapi
from fastapi import Depends

from app import schemas
from app import services
from app.database import get_session

app = _fastapi.FastAPI()


@app.post("/api/contacts/", response_model=schemas.Contact)
async def create_contact(
    contact: schemas.CreateContact,
    db: Annotated[get_session, Depends()],
):
    return await services.create_contact(contact, db)


@app.get("/api/contacts/", response_model=list[schemas.Contact])
async def get_contacts(
    db: Annotated[get_session, Depends()],
):
    return await services.get_all_contacts(db)


@app.get("/api/contacts/{contact_id}/", response_model=schemas.Contact)
async def get_contact(
    contact_id: int,
    db: Annotated[get_session, Depends()],
):
    contact = await services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(
            status_code=_fastapi.status.HTTP_404_NOT_FOUND,
            detail="Contact does not exist",
        )
    return contact


@app.delete("/api/contacts/{contact_id}/")
async def delete_contact(
    contact_id: int,
    db: Annotated[get_session, Depends()],
):
    contact = await services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(
            status_code=_fastapi.status.HTTP_404_NOT_FOUND,
            detail="Contact does not exist",
        )
    await services.delete_contact(contact, db)

    return {True: "Successfully deleted user"}


@app.put("/api/contacts/{contact_id}/", response_model=schemas.Contact)
async def update_contact(
    contact_id: int,
    contact_data: schemas.CreateContact,
    db: Annotated[get_session, Depends()],
):
    contact = await services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(
            status_code=_fastapi.status.HTTP_404_NOT_FOUND,
            detail="Contact does not exist",
        )
    return await services.update_contact(contact_data, contact, db)
