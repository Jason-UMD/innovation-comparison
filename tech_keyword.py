
from anytree import NodeMixin
from pybliometrics.scopus import ScopusSearch

class Keyword(NodeMixin):
    def __init__(self, keyword, children=None):
        super(Keyword, self).__init__()
        self.name = keyword
        if children:
            self.children = children
        #TODO: make scopus calls
        #s = ScopusSearch("TITLE-ABS-KEY ( " + keyword + " )")
        #print(s)
