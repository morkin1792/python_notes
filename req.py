import requests 

class Req:
    def __init__(self, keep_session = False, mark = 'CYPHER'):
        self.session = None
        if keep_session:
            self.session = requests.session()
        self.mark = mark

    def requestCore(self, method, url, headers = '', body = ''):
        """
        do a request

        :param str method: GET, POST, ...
        :param str url: url to request
        :param str headers: headers to request (separate by breakline)
        :param str body: body to request (separate by breakline)
        """
        session = self.session
        if not self.session:
            session = requests.session()
        if len(headers) > 1:
            headers = {h[0:h.index(':')]: h[h.index(':')+1:] for h in list(filter(lambda u: len(u) > 1, headers.split('\n')))}
            for k in headers.keys():
                while headers[k][0] == ' ':
                    headers[k] = headers[k][1:]
            session.headers.update(headers)
        r = session.request(method, url, '', body)
        if not self.session:
            session.close()
        return r


    def request(self, method, url, headers, body, payload):
        payload = str(payload)
        if self.mark in url:
            url = url.replace(self.mark, payload, 1)
        elif self.mark in body:
            body = body.replace(self.mark, payload, 1)
        elif self.mark in headers:
            headers = headers.replace(self.mark, payload, 1)
        else:
            raise Exception('missing mark: ' + self.mark)
        return self.requestCore(method, url, headers, body)