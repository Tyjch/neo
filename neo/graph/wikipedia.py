from py2neo.ogm import GraphObject, Property, RelatedTo
from wikipedia import WikipediaPage
from neo.graph.data import Node, TimeMixin, DefaultGraphMixin

'''
class WikiNode(Node):

    has_category = RelatedTo("WikiNode")
    has_article = RelatedTo("WikiNode")

    def __init__(self, title, graph=default_graph, label="Wikipedia"):
        super(WikiNode, self).__init__(title, label=label)
        #self.__primarylabel__ = label
        graph.push(self)

    def get_categories(self):

        wikipage = WikipediaPage(self.title)

        prefix = "Category:"

        for category in wikipage.categories:
            title = prefix + category
            category = WikiNode(title, self.graph, label="Category")
            category.depth = self.depth + 1

            self.graph.create(category)
            self.graph.push(category)

            self.has_category.add(category)
            self.graph.push(self)

    def get_articles(self):

        wikipage = WikipediaPage(self.title)

        # TODO: 'wikipage.links' doesn't return all links when the page is a category

        for article in wikipage.links:
            article = WikiNode(article, self.graph, label="Article")
            article.depth = self.depth + 1

            self.graph.create(article)
            self.graph.push(article)

            self.has_article.add(article)
            self.graph.push(self)
'''


class WikiNode(DefaultGraphMixin, TimeMixin, Node):

    WIKILABELS = ["Article", "Category"]

    def __init__(self, title, label):

        if label not in WikiNode.WIKILABELS:
            print("{} is not permitted as a label for this class", label)

        else:
            # TODO: Check if a node with the same primary key-value pair exists in the graph first
            Node.__init__(self, title, label)
            TimeMixin.__init__(self)
            DefaultGraphMixin.__init__(self)





