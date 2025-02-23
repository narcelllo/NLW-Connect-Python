from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventCreatorController():
    def __init__(self, events_repo: EventosRepositoryInterface):
        self.__events_repo = events_repo
        
    def create(self, http_request: HttpRequest ) -> HttpResponse:
            event_info = http_request.body["data"]
            event_name = event_info["name"]
            
            self.__check_event(event_name)
            self.__insert_events(event_name)
            return self.__format_response(event_name)

    def __check_event(self, event_name: str) -> None:
        response = self.__events_repo.select_events(event_name)
        if  response: raise Exception("Event exists!")

    def __insert_events(self, event_name: str) -> None:
            self.__events_repo.insert(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
          return HttpResponse(
                body={
                    "data":{
                          "type": "Event",
                          "cont": 1,
                          "attributes": {
                                    "event_name": event_name
                          }

                    }
                },
                status_code=201
          )