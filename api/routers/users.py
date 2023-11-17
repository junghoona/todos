from queries.users import UserQueries, UserListOut, UserIn, UserOut
from fastapi import APIRouter, Depends, HTTPException
from Typing import Optional


router = APIRouter()


# 1. get a user with a specific id
@router.get('/api/users/{user_id}', response_model=Optional[UserOut])
def get_user(
    user_id: int,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(user_id)
    if record is None:
        raise HTTPException(status_code=404, detail="No user found with id {}".format(user_id))
    else:
        return record


# 2. get all users
@router.get('/api/users/', response_model=UserListOut)
def get_all_users(
    queries: UserQueries = Depends(),
):
    return {"users": queries.get_all_users()}


# 3. create a user
@router.post('/api/users/', response_model=UserOut)
def create_user(
    user: UserIn,
    queries: UserQueries = Depends(),
):
    try:
        return queries.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}: Failed to create user")


# 4. delete a user
@router.delete('/api/users/{user_id}', response_model=bool)
def delete_user(
    user_id: int,
    queries: UserQueries = Depends(),
):
    queries.delete_user(user_id)
    return True
