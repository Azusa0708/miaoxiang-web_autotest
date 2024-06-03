import jieba
from utils.asserts.assert_accuracy import assert_accuracy
from utils.reptile.get_text import placeholder_text,text_answer

def compare_similarity():
    numofwords_in_placeholder = 0
    numofwords_in_text_answer = 0
    words_in_placeholder = list(jieba.cut(placeholder_text,cut_all=False))
    words_in_text_answer = list(jieba.cut(text_answer,cut_all=False))
    numofwords_in_placeholder = sum(1 for _ in words_in_placeholder)
    #numofwords_in_text_answer = sum(1 for _ in words_in_text_answer)
    set_words_in_placeholder = set(words_in_placeholder)
    set_words_in_text_answer = set(words_in_text_answer)
    
    common_words = set_words_in_placeholder & set_words_in_text_answer

    Accuracy = float(len(common_words)) / float(numofwords_in_placeholder)
    assert_accuracy(Accuracy)