from anytree import NodeMixin
import data_retrival
import json
from os.path import exists

class Tech(NodeMixin):
    def __init__(self, name, seed_list=None, children=None):
        super(Tech, self).__init__()
        self.name = name
        if children:
            self.children = children
        self.keywords_path = 'cache/keywords/' + name
        self.papers_path = 'cache/papers/' + name

    def get_keywords(load=True, store=True, min_support=2):
        if load and exists(self.keywords_path):
            self.keywords = json.loads(open(self.keywords_path).read())
        else:
            self.keywords = []
            for seed in seed_list:
                 self.keywords += data_retrival.fetch_keywords(seed)
            self.keywords = [i for i in self.keywords if self.keywords.count(i) >= min_support]
        if store:
            with open(keywords_path, 'w') as fp:
                json.dump(self.keywords, fp)

    def get_papers(load=True, store=True, min_support=2):
        if load and exists(self.papers_path):
            self.papers = json.loads(open(self.papers_path).read())
        else:
            self.papers = []
            for keyword in self.keywords:
                 self.papers += data_retrival.fetch_papers(keyword)
            self.papers = [i for i in self.papers if self.papers.count(i) >= min_support]
        if store:
            with open(papers_path, 'w') as fp:
                json.dump(self.papers, fp)