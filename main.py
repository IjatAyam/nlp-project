from google_trans_new import google_translator

translator = google_translator()

prefix_file = 'Prefixes.txt'
prefix_mean_file = 'PrefixesMeans.txt'
suffix_file = 'Suffixes.txt'
suffix_mean_file = 'SuffixesMeans.txt'

prefixes = []
suffixes = []

with open(prefix_file, 'r') as f:
    with open(prefix_mean_file, 'r') as f2:
        raw_prefixes = f.read().splitlines()
        raw_prefixes_mean = f2.read().splitlines()
        for i in range(len(raw_prefixes)):
            prefixes.append({
                'term': raw_prefixes[i],
                'mean': raw_prefixes_mean[i],
                'type': 'prefix'
            })

with open(suffix_file, 'r') as f:
    with open(suffix_mean_file, 'r') as f2:
        raw_suffixes = f.read().splitlines()
        raw_suffixes_mean = f2.read().splitlines()
        for i in range(len(raw_suffixes)):
            suffixes.append({
                'term': raw_suffixes[i],
                'mean': raw_suffixes_mean[i],
                'type': 'suffix'
            })

while True:
    input_word = input('Enter the word (enter "-1" to exit): ')

    if input_word == '-1':
        break

    chosen_prefix_term = None
    prefix_length_match = 0
    for prefix in prefixes:
        if input_word.lower().startswith(prefix['term'].lower()):
            if len(prefix['term']) > prefix_length_match:
                prefix_length_match = len(prefix['term'])
                chosen_prefix_term = prefix

    chosen_suffix_term = None
    suffix_length_match = 0
    for suffix in suffixes:
        if input_word.lower().endswith(suffix['term'].lower()):
            if len(suffix['term']) > suffix_length_match:
                suffix_length_match = len(suffix['term'])
                chosen_suffix_term = suffix

    sliced_word = input_word
    if chosen_prefix_term:
        sliced_word = sliced_word[len(chosen_prefix_term['term']):]
    if chosen_suffix_term:
        sliced_word = sliced_word[:-len(chosen_suffix_term['term'])]

    prefix_word = chosen_prefix_term['mean'] if chosen_prefix_term else ''
    suffix_word = chosen_suffix_term['mean'] if chosen_suffix_term else ''

    if len(sliced_word) > 2:
        word_mean = f"{prefix_word} {sliced_word} {suffix_word}"
    else:
        word_mean = f"{prefix_word} {suffix_word}"

    translated_word = translator.translate(word_mean, lang_src='en', lang_tgt='ms')

    print(f'{input_word} => {word_mean} => {translated_word}\n')
