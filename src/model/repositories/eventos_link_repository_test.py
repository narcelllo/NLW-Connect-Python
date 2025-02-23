import pytest
from.eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events_link():
    evento_id = 1
    subs_id = 2
    event_link_repo = EventosLinkRepository()

    event_link_repo.insert(evento_id, subs_id)
    