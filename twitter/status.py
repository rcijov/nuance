# -*- coding: utf-8 -*-
from .exception import Exception

class Status():

    # https://dev.twitter.com/docs/error-codes-responses
    codes = {
        400: 'Bad Request: The request was invalid',
        401: ('Unauthorized: Authentication credentials ',
              ' were missing or incorrect'),
        403: ('Forbidden: The request is understood, but',
              'it has been refused or access is not allowed'),
        404: ('Not Found: The URI requested is invalid or',
              'the resource requested does not exists'),
        406: 'Not Acceptable: Invalid format is specified in the request',
        410: 'Gone: This resource is gone',
        420: 'Enhance Your Calm:  You are being rate limited',
        422: 'Unprocessable Entity: Image unable to be processed',
        429: ('Too Many Requests: Request cannot be served ',
              'due to the application\'s rate limit having ',
              'been exhausted for the resource'),
        500: 'Internal Server Error: Something is broken',
        502: 'Bad Gateway: Twitter is down or being upgraded',
        503: ('Service Unavailable: The Twitter servers ',
              'are up, but overloaded with requests'),
        504: ('Gateway timeout: The request couldn\'t ',
              'be serviced due to some failure within our stack'),
                }

    def __init__(self,http_status):
        if http_status in self.codes:
            raise Exception(http_status, self.exceptions[http_status])



