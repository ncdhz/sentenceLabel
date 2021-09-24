from nltk.tokenize import sent_tokenize
class Tools:
    Answer = 'answer'
    
    Question = 'question'
    
    Article = 'article'
    
    Options = 'options'
    
    Data = 'data'

    Sentences = 'sentences'

    Number = 'number'

    Config = 'config'

    Segmentation = 'segmentation'
    
    SentList = 'sent_list'
    
    SentName = 'sentName'

    SegmentationFunc = 'sent_list = sent_tokenize(article)'

    @staticmethod
    def refresh():
        Tools.Answer = 'answer'
        Tools.Question = 'question'
        Tools.Article = 'article'
        Tools.Options = 'options'
        Tools.Data = 'data'
        Tools.Sentences = 'sentences'
        Tools.Number = 'number'
        Tools.SentList = 'sent_list'

    @staticmethod
    def injection(config):
        if type(config) != dict:
            return False
        if type(config) == dict:
            answer = config.get('answer', 'answer')
            question = config.get('question', 'question')
            article = config.get('article', 'article')
            data = config.get('data', 'data')
            options = config.get('options', 'options')
            sentences = config.get('sentences', 'sentences')
            number = config.get('number', 'number')
            if type(answer) != str:
                return False
            if type(question) != str:
                return False
            if type(article) != str:
                return False
            if type(data) != str:
                return False
            if type(options) != str:
                return False
            if type(sentences) != str:
                return False
            if type(number) != str:
                return False
            Tools.Answer = answer
            Tools.Question = question
            Tools.Article = article
            Tools.Options = options
            Tools.Data = data
            Tools.Sentences = sentences
            Tools.Number = number
        return True

def check_segmentation(segmentation):
    exec(f'''{Tools.Article} = "my name is xiaoming. I am very happy every day."\n''' + segmentation)
    sent_list_ = locals()[Tools.SentList]
    type(sent_list_) == list
    for s in sent_list_:
        assert type(s) == str

def check_format(d):
    assert type(d[Tools.Answer]) == str
    assert d[Tools.Answer] != ''
    assert len(d[Tools.Answer]) == 1
    if not is_int(d[Tools.Answer]):
        assert is_a2z(d[Tools.Answer])
    assert d[Tools.Question] != ''
    assert type(d[Tools.Question]) == str
    assert d[Tools.Article] != ''
    assert type(d[Tools.Article]) == str
    assert len(d[Tools.Options]) != 0
    for o in d[Tools.Options]:
        assert type(o) == str
        assert o != ''

def is_int(s):
    is_i = True
    try:
        int(s)
    except Exception:
        is_i = False
    return is_i

def is_a2z(s):
    s = s.lower()
    return s >= 'a' and s <= 'z'