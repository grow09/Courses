from abc import abstractclassmethod, abstractmethod

class Publication(object):
    def Publication(self, heading, text, date, autor, source, endDate):
        self.heading = heading
        self.text = text
        self.date = date
        self.autor = autor
        self.source = source
        self.endDate = endDate

    @abstractmethod
    def printMaterial(self):
        print("Печать материала")

class News(Publication):
    def Publication(self, heading, text, date, source):
        self.heading = heading
        self.text = text
        self.date = date
        self.source = source

    def printMaterial(self):
        return "%s : %s \n Источник: %s \n дата: %s" % (self.heading, self.text, self.source, self.date)

class Advertisement(Publication):
    def Publication(self, heading, text, date, autor):
        self.heading = heading
        self.text = text
        self.date = date
        self.autor = autor

    def printMaterial(self):
        return "%s: %s \n Автор: %s \n дата: %s" % (self.heading, self.text, self.autor, self.date)

class Article(Publication):
    def Publication(self, heading, text, endDate):
        self.heading = heading
        self.text = text
        self.endDate = endDate

    def printMaterial(self):
        return "%s: %s \n дата: %s" % (self.heading, self.text, self.endDate)


if __name__ == "__main__":
    news = News()
    news.Publication(heading = "Валюта", text = "Доллар знову впав", date = "2020-02-23", source = "Нацбанк")
    print(news.printMaterial())
    ad = Advertisement()
    ad.Publication(heading = "Евровидение", text = "Песня с которой Украина выступит на евровидении...", date = "2020-02-22", autor = "gRow09")
    print(ad.printMaterial())
    article = Article()
    article.Publication(heading = "Куплю квартиру", text = "звонити 067235534523", endDate = "2020-02-27")
    print(article.printMaterial())
