create_novel_table = """CREATE TABLE IF NOT EXISTS novels (
    id integer primarykey,
    name text not null,
    slug text not null,
    coverurl text,
    abbreviation text,
    synopsis text,
    language text,
    timecreated integer,
    status integer,
    chaptercount integer,
    tagscs string
    );
    """

def get_novel_list_query(_from, _limit):
    return """
        SELECT * from novels where id > {} order by id
        limit {}""".format(_from, _limit) 
def insert_novel_query(novel):
    pass
