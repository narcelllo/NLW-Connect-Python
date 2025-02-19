import pytest
from .subsctribers_repository import SubscribersRepository

@pytest.mark.skip("insert in DB")
def test_insert():
    subscriber_info = {
        "nome": "Name 1",
        "email": "email1@email.com",
        "evento_id": 3
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "email1@email.com"
    evento_id = 3

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)
    print(resp.email)
