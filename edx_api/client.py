"""edX api client"""
# pylint: disable=fixme
import requests

from .course_structure import CourseStructure


# pylint: disable=too-few-public-methods
class EdxApi(object):
    """
    A client for speaking with edX.
    """
    def __init__(self, credentials, base_url='https://courses.edx.org/'):
        if 'access_token' not in credentials:
            raise AttributeError(
                "Due to a lack of support for Client Credentials Grant in edX,"
                " you must specify the access token."
            )

        self.base_url = base_url
        self.credentials = credentials

    def get_requester(self):
        """
        Returns an object to make authenticated requests. See python `requests` for
        the API.
        """
        # TODO(abrahms): Perhaps pull this out into a factory function for
        # generating an EdxApi instance with the proper requester & credentials.
        session = requests.session()
        session.headers.update({
            'Authorization': 'Bearer {}'.format(self.credentials['access_token'])
        })
        return session

    @property
    def course_structure(self):
        """Course Structure API"""
        return CourseStructure(self.get_requester(), self.base_url)