from scrapy.dupefilter import RFPDupeFilter

class CustomURLFilter(RFPDupeFilter):
    """ 只根据url去重"""

    def __init__(self,urls_seen, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)