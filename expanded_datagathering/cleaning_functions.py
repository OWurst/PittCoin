import pandas as pd

def simplify_quotes(text):
    """
    Simplifies the quotes in the text to avoid errors when saving to csv.
    """
    text = text.replace('"', "'")
    text = text.replace("'''", '"')
    return text

def clean_unicode(text):
    text_utf8 = text.replace('\u2018', "'").replace('\u2019', "'")
    text_utf8 = text_utf8.replace('\u203a', '>').replace('\u2039', '<')
    text_utf8 = text_utf8.replace('\u201c', "'").replace('\u201d', "'")
    text_utf8 = text_utf8.replace('\u2014', '-').replace('\u2015', '-')

    # replace newlines, new paragraphs, and tabs with spaces
    text_utf8 = text_utf8.replace('\u2028', ' ').replace('\u2029', ' ')
    text_utf8 = text_utf8.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # replace weird 00a0 character with space
    text_utf8 = text_utf8.replace('\u00a0', ' ')

    # replace weird 00b7 character with period
    text_utf8 = text_utf8.replace('\u00b7', '.')

    # replace weird 00e2 character with space
    text_utf8 = text_utf8.replace('\u00e2', ' ')

    # replace weird 00e2 character with space
    text_utf8 = text_utf8.replace('\u00e2', ' ')

    text_utf8 = text_utf8.replace('\u2013', '-')

    # remove oe character
    text_utf8 = text_utf8.replace('\u0153', 'oe')

    # make euro symbol into the word 'euro'
    text_utf8 = text_utf8.replace('\u20ac', 'euro')

    # make pound symbol into the word 'pound'
    text_utf8 = text_utf8.replace('\u00a3', 'pound')

    # make yen symbol into the word 'yen'
    text_utf8 = text_utf8.replace('\u00a5', 'yen')

    # make unicode space into a regular space
    text_utf8 = text_utf8.replace('\u2002', ' ').replace('\u2003', ' ')
    text_utf8 = text_utf8.replace('\u2004', ' ').replace('\u2005', ' ')
    text_utf8 = text_utf8.replace('\u2006', ' ').replace('\u2007', ' ')
    text_utf8 = text_utf8.replace('\u2008', ' ').replace('\u2009', ' ')
    text_utf8 = text_utf8.replace('\u200a', ' ').replace('\u200b', ' ')
    text_utf8 = text_utf8.replace('\u200c', ' ').replace('\u200d', ' ')
    text_utf8 = text_utf8.replace('\u200e', ' ').replace('\u200f', ' ')

    # make tm symbol into the word 'trademark'
    text_utf8 = text_utf8.replace('\u2122', 'trademark')

    # make copyright symbol into the word 'copyright'
    text_utf8 = text_utf8.replace('\u00a9', 'copyright')

    # make registered symbol into the word 'registered'
    text_utf8 = text_utf8.replace('\u00ae', 'registered')

    # make bullet symbol into *
    text_utf8 = text_utf8.replace('\u2022', '*')

    # make ellipsis symbol into ...
    text_utf8 = text_utf8.replace('\u2026', '...')

    # make em dash symbol into --
    text_utf8 = text_utf8.replace('\u2014', '--')

    # convert to utf-8
    text_utf8 = text_utf8.encode('utf-8').decode('utf-8')

    return text_utf8

def clean(df):
    df = df.dropna()

    df.loc[:, 'text'] = df['text'].apply(lambda x: '"' + x + '"')
    df.loc[:, 'title'] = df['title'].apply(lambda x: '"' + x + '"')

    # remove all newline characters
    df.loc[:, 'text'] = df['text'].apply(lambda x: x.replace('\n', ' '))
    df.loc[:, 'title'] = df['title'].apply(lambda x: x.replace('\n', ' '))

    # clean unicode mess
    df.loc[:, 'text'] = df['text'].apply(clean_unicode)
    df.loc[:, 'title'] = df['title'].apply(clean_unicode)

    # simplify quotes
    df.loc[:, 'text'] = df['text'].apply(simplify_quotes)
    df.loc[:, 'title'] = df['title'].apply(simplify_quotes)

    # make lowercase
    df.loc[:, 'text'] = df['text'].apply(lambda x: x.lower())
    df.loc[:, 'title'] = df['title'].apply(lambda x: x.lower())

    df.loc[:, 'date']= pd.to_datetime(df['date'])

    return df