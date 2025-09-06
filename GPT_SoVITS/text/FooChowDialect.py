# reference: https://huggingface.co/spaces/Naozumi0512/Bert-VITS2-Cantonese-Yue/blob/main/text/chinese.py

import re

from text.symbols import punctuation
from text.symbols2 import symbols


rep_map = {
    "：": ",",
    "；": ",",
    "，": ",",
    "。": ".",
    "！": "!",
    "？": "?",
    "\n": ".",
    "·": ",",
    "、": ",",
    "...": "…",
    "$": ".",
    "“": "'",
    "”": "'",
    '"': "'",
    "‘": "'",
    "’": "'",
    "（": "'",
    "）": "'",
    "(": "'",
    ")": "'",
    "《": "'",
    "》": "'",
    "【": "'",
    "】": "'",
    "[": "'",
    "]": "'",
    "—": "-",
    "～": "-",
    "~": "-",
    "「": "'",
    "」": "'",
}


def replace_punctuation(text):
    # text = text.replace("嗯", "恩").replace("呣", "母")
    pattern = re.compile("|".join(re.escape(p) for p in rep_map.keys()))

    replaced_text = pattern.sub(lambda x: rep_map[x.group()], text)

    # replaced_text = re.sub(r"[^\u4e00-\u9fa5" + "".join(punctuation) + r"]+", "", replaced_text)

    return replaced_text


def text_normalize(text):
    dest_text = ""
    for sentence in text:
        dest_text += replace_punctuation(sentence)
    return dest_text


punctuation_set = set(punctuation)




def g2p(text):
    phones = []
    for word in text.split(' '):
        if word in symbols:
            phones.append(word)
        elif word.upper() in symbols:
            phones.append(word.upper())
        else:
            if word.endswith(('1','2','3','4','5')):
                if word.startswith(('ng', 'nj')):
                    if word[2:] in symbols:
                        phones.append(word[:2])
                        phones.append(word[2:])
                    else:
                        print(f"ERROR 出现了未知的音素 {word}")
                elif word.startswith(('f','b','p','m','d','t','n','l','s','z','c','g','k','h','w','j')):
                    if word[1:] in symbols:
                        phones.append(word[:1])
                        phones.append(word[1:])
                    else:
                        print(f"ERROR 出现了未知的音素 {word}")
            else:
                # print(f"ERROR 出现了未知的音素 {word}")
                for char in word:
                    phones.append(char.upper())

    return phones


if __name__ == "__main__":
    text = "ai55 zang55 hai33 jy55 dou24 bei55 a33 yes"
    text = text_normalize(text)
    phones = g2p(text)
    print(phones)
