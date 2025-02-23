from src.model.repositories.interfaces.subsctribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreatorController():
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo
        
    def create(self, http_request: HttpRequest ) -> HttpResponse:
        subs_info = http_request.body["data"]
        subs_email = subs_info["email"]
        subs_event_id = subs_info["evento_id"]

        self.__check_sub(subs_email, subs_event_id)
        self.__insert_sub(subs_info)
        return self.__format_response(subs_info)

    def __check_sub(self, subscriber_email: str, event_id: int) -> None:
            response = self.__subs_repo.select_subscriber(subscriber_email, event_id)
            if  response: raise Exception("Subscriber exists!")

    def __insert_sub(self, subs_info: dict) -> None:
         self.__subs_repo.insert(subs_info)

    def __format_response(self, subs_info: dict) -> HttpResponse:
          return HttpResponse(
                body={
                    "data":{
                          "type": "Subscriber",
                          "cont": 1,
                          "attributes": subs_info
                    }
                },
                status_code=201
          )