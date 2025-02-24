from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subsctribers_repository import SubscribersRepositoryInterface


class SubscriberManagerController:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def det_subscribers_by_link(self, http_request: HttpRequest ) -> HttpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"] 
        subscribers = self.__subscribers_repo.select_subscribers_by_link(link, event_id)
        return self.__fromat_subscribers_by_link(subscribers)
    
    def get_event_ranking(self, http_request: HttpRequest ) -> HttpResponse:
        event_id = http_request.param["event_id"] 
        event_ranking = self.__subscribers_repo.get_reanking(event_id)
        return self.__fromat_event_ranking(event_ranking)

    def __fromat_subscribers_by_link(self, subscribers: list) ->HttpResponse:
        formated_subscribet = []

        for subscriber in subscribers:
            formated_subscribet.append({
                "nome": subscriber.nome,
                "email": subscriber.email
            })
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscribers",
                    "count": len(formated_subscribet),
                    "attribute": {
                        "subscribes": formated_subscribet

                    }
                }
            }
        )
    
    def __fromat_event_ranking(self, event_ranking: list) ->HttpResponse:
        formated_event_ranking = []

        for position in event_ranking:
            formated_event_ranking.append({
                "link": position.link,
                "=total_subscribers": position.total
            })
        return HttpResponse(
            body={
                "data": {
                    "type": "Ranking",
                    "count": len(formated_event_ranking),
                    "attribute": {
                        "ranking": formated_event_ranking

                    }
                }
            }
        )