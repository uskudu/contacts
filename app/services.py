from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app import schemas
from sqlalchemy import select


async def create_contact(
    contact: schemas.CreateContact, db: AsyncSession
) -> schemas.Contact:
    contact = models.Contact(**contact.model_dump())
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return schemas.Contact.model_validate(contact)


async def get_all_contacts(db: AsyncSession) -> list[schemas.Contact]:
    result = await db.execute(select(models.Contact))
    contacts = result.scalars().all()
    return [schemas.Contact.model_validate(contact) for contact in contacts]


async def get_contact(contact_id: int, db: AsyncSession) -> models.Contact:
    result = await db.execute(
        select(models.Contact).where(models.Contact.id == contact_id)
    )
    contact = result.scalar_one_or_none()
    return contact


async def delete_contact(contact: models.Contact, db: AsyncSession):
    await db.delete(contact)
    await db.commit()


async def update_contact(
    contact_data: schemas.CreateContact, contact: models.Contact, db: AsyncSession
) -> schemas.Contact:
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number

    await db.commit()
    await db.refresh(contact)
    return schemas.Contact.model_validate(contact)
