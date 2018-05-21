class HttpResponseDict(object):
    def __init__(self):
        self.responseDict = {
            'success': 200,
            'not found': 404,
            'incorrect parameters': 422
        }

    def __getitem__(self, item):
        return self.responseDict[item]
