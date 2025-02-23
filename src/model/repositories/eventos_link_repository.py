import random
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.event_link_repository import EventosLinkRepositoryInterface

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, event_id: int, subscriber_id: id) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices('023456789', k=7))
                formated_link = f'evento-{event_id}-{subscriber_id}-{link_final}'

                new_events_link = EventosLink(
                        evento_id=event_id,
                        inscrito_id=subscriber_id,
                        link=formated_link
                    )
                
                db.session.add(new_events_link)
                db.session.commit()

                return formated_link
            except Exception as exception:
                raise exception
            
    def select_events_link(self, evento_id: int, subscriber_id: id) -> EventosLink:
        with DBConnectionHandler() as db:
            data = (
                db.session.query(EventosLink)
                .filter(
                    EventosLink.event_id == evento_id,
                    EventosLink.inscrito_id == subscriber_id,                    
                    )
                .one_or_none()
            )
            return data