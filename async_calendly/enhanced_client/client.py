from ..basic_client.client import CalendlyClient
from .objects import User, EventType, Event, EventInvitee, OrganizationMembership
from .list_response_handler import ListResponseHandler


class CalendlyEnhancedClient(CalendlyClient):
    # Resource response functions
    async def get_current_user(self):
        response = await super().get_current_user()
        current_user = response['resource']
        return User.create_from_dict(self, current_user)

    async def get_user(self, uuid):
        response = await super().get_user(uuid)
        return response['resource']

    async def get_event(self, uuid):
        response = await super().get_event(uuid)
        return response['resource']

    # Collection response functions

    async def list_event_types(self, count=50, max_pages=100, **kwargs):
        first_response = await super().list_event_types(count=count, **kwargs)
        all_results = await ListResponseHandler.get_all_for_list_response(self, first_response, max_page=max_pages)
        return [EventType.create_from_dict(self, et_dict) for et_dict in all_results]

    async def list_events(self, count=50, max_pages=100, **kwargs):
        first_response = await super().list_events(count=count, **kwargs)
        all_results = await ListResponseHandler.get_all_for_list_response(self, first_response, max_page=max_pages)
        return [Event.create_from_dict(self, e_dict) for e_dict in all_results]

    async def list_event_invitees(self, count=50, max_pages=100, **kwargs):
        first_response = await super().list_event_invitees(count=count, **kwargs)
        all_results = await ListResponseHandler.get_all_for_list_response(self, first_response, max_page=max_pages)
        return [EventInvitee.create_from_dict(self, et_dict) for et_dict in all_results]

    async def list_organization_memberships(self, count=50, max_pages=100, **kwargs):
        first_response = await super().list_organization_memberships(count=count, **kwargs)
        all_results = await ListResponseHandler.get_all_for_list_response(self, first_response, max_page=max_pages)
        return [OrganizationMembership.create_from_dict(self, om_dict) for om_dict in all_results]