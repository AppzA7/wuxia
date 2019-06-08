import wuxia

class Novel:
    Wuxia = wuxia.WuxiaWorld()
    def __init__(self, id = None, name = None, slug = None, coverurl = None, abbr = None, synopsis = None, language = None, timecreated = None, status = None, chaptercount = None, tags = None):
        self.id = id
        self.name = name
        self.slug = slug
        self.coverurl = coverurl
        self.abbr = abbr
        self.synopsis = synopsis
        self.language = language
        self.timecreated = timecreated
        self.status = status
        self.chaptercount = chaptercount
        self.tagscs = str(tags)[1:-1]

    def getChapter(self, chapter):
        url = Novel.Wuxia.getChapterUrl(self.slug, chapter, self.abbr)

        #fetch the url

if __name__ == "__main__":    
    overgeared = Novel(slug="overgeared", abbr="og")
    print (overgeared.getChapter(1))

    