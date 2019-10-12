def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """

    letters, counter = [], []
    for l in msg:
        if l in letters:
            counter[letters.index(l)] += 1
        else:
            letters.append(l)
            counter.append(1)
    counter = [c for l,c in sorted(zip(letters,counter))]
    letters = sorted(letters)
    m = counter.index(max(counter))

    return letters[m], counter[m]


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)
