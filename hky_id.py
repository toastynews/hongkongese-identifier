from os import listdir
from os.path import isfile, join

hky_dict = {}
hky_markers = ['咗', '唔', '係', '喺', '啦', '嘅', '既', '咁',
                    '佢', '哋', '冇', '仲', '嘢', '乜', '噉', '咪', 
                    '咩', '俾', '㗎', '呢', '嚟', '黎', '啫', '喂',
                    '喇', '喎', '睇']
zh_dict = {}
zh_markers = ['是', '的', '他', '她', '沒', '也', '看', '說', '在']

data_directories = [
    'data/hky-classification/hky/',
    'data/hky-classification/zh/',
    'data/hky-classification/en/'
]
# go through all the above directories and identify language of all files
for directory in data_directories:
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    print(directory)
    for file in only_files:
        # reset stats
        total_words = 0
        hky_words = 0
        zh_words = 0
        en_words = 0
        for word in hky_markers:
            hky_dict[word] = 0
        for word in zh_markers:
            zh_dict[word] = 0

        # count characters
        with open(directory + file, 'r', encoding="utf8") as f:
            token = 0
            for line in f:
                characters = list(map(str, line.rstrip()))
                for character in characters:
                    total_words = total_words + 1
                    if character in hky_dict:
                        hky_words = hky_words + 1
                        hky_dict[character] = hky_dict[character] + 1
                    elif character in zh_dict:
                        zh_words = zh_words + 1
                        zh_dict[character] = zh_dict[character] + 1
                    elif ((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')):
                        en_words = en_words + 1

        # Hong Kongese-ness = Hong Kongese markers / All characters
        # Chinese-ness = Chinese markers / All characters
        # If (Hong Kongese-ness - Chinese-ness) > 0.02, then it is Hong Kongese
        # Otherwise it is Standard Chinese
        en_percent = en_words/total_words
        hky_percent = hky_words/total_words
        zh_percent = zh_words/total_words
        hky_diff_percent = hky_percent-zh_percent
        if en_percent > 0.5:
            print('{} - {} ({})'.format(file, 'en', en_percent))
        elif hky_diff_percent > 0.02:
            print('{} - {} ({})'.format(file, 'hky', hky_diff_percent))
        else:
            print('{} - {} ({})'.format(file, 'zh', hky_diff_percent))
    print()
