class Article:
 all = []
 def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)

@property
def title(self):
    return self._title

@title.setter
def title(self, title):
    if self._title is not None:
        raise Exception("title should not change after instantiation")
    if isinstance(title, str) and 5 <=len(title) <= 50:
         self._title = title
    else:
         raise Exception("title must be a string and should be betwween 5 and 50 characters")

@property
def author(self):
    return self._author

@author.setter
def author(self, author):
    if self._author is not None:
        raise Exception("author should not change after instantiation")
    if isinstance(author, Author):
        self._author = author
    else:
        raise Exception("author must be an instance of Author")

@property
def magazine(self):
    return self._magazine

@magazine.setter
def magazine(self, magazine):
    if self._magazine is not None:
        raise Exception("magazine should not change after instantiation")
    if isinstance(magazine, Magazine):
        self._magazine = magazine
    else:
        raise Exception("magazine must be an instance of Magazine")


class Author:
    all = []
    magazines = {}

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
       return self._name
    
    @name.setter
    def name(self, name):
       if hasattr(Author, "name"):
        if isinstance(name, str) and len(name) > 0:
           self._name = name
       else:
           raise Exception("name should not change after instantiated")
           

    def articles(self):
        return [article for article in Article.all if article.author == self]
           

    def magazines(self):
        return(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
         return Article(self, magazine, title)

    def topic_areas(self):
        pass

class Magazine:
    all = []
    #authors = {}
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else: 
            raise Exception("name should be able to change after instantiation")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else: 
            raise Exception("category should be able to change")


    def articles(self):
        return[article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.article()]
        contributing_authors = [author for author in authors if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None


author = Author("Felicia")


magazine = Magazine("sona", "fashion") 