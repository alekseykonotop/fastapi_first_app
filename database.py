from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass

# добавим саму таблицу для task
# Добавляем к названию таблицы окончание 'Orm'- чтобы понимать что это класс таблицы!!

class TaskOrm(Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


# Users
class UserOrm(Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    login: Mapped[str]
    age: Mapped[int]
    phone: Mapped[Optional[str]]



# функция для создания таблиц из документации асинхронная
# так как ранее мы импортировали и используем асинхронный драйвер aiosqlite
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# функция для удаления всех таблиц ( на тестовом проекте)
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)