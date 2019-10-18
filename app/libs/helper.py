def is_isbn_or_key(word):
    """
        接收:
            q:q|isbn,即能代表普通关键字又能代表isbn,因为网页没有分类选项
            page:start,count
        """
    # isbn
    # isbn13 13个0到9数字组成
    # isbn10 10个0到9数字组成,含有一些'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    # q.isdigit()判断q对象字符串是否只由数字组成
    # 多个判断条件的顺序会对代码运行效率产生影响,对判断为False概率较大的条件要放在前面,可以减少判断流程,提高效率;较耗时的条件判断(如需要查询数据库)放在后面
    return isbn_or_key