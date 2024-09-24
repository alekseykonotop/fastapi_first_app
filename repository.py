from database import new_session, TaskOrm, UserOrm
from schemas import STaskAdd, SUserAdd, STask, SUser
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush() # вернет перед коммитом id записываемого в базу экземпляра объекта task
            await session.commit()

            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]

            return task_schemas

class UserRepository:
    @classmethod
    async def add_user(cls, data: SUserAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()

            return user.id

    @classmethod
    async def find_all(cls) -> list[SUser]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()
            user_schemas = [SUser.model_validate(user_model) for user_model in user_models]

            return user_schemas

    @classmethod
    async def find_user(cls, id: int) -> SUser:
        """
        Получает id пользователя и возвращает
        данные по нему. Если такого пользвателя нет,
        то сообщение "Пользователь не найден"

        :return:
        """
        async with new_session() as session:
            query = select(UserOrm).where(UserOrm.id == id)
            result = await session.execute(query)
            user_data = result.scalars().first()
            user_schema = SUser.model_validate(user_data)

            return user_schema
