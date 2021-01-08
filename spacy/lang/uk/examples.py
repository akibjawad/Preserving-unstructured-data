# coding: utf8
from __future__ import unicode_literals


"""
Example sentences to test spaCy and its language models.

>>> from spacy.lang.uk.examples import sentences
>>> docs = nlp.pipe(sentences)
"""


sentences = [
    "Ніч на середу буде морозною.",
    "Чим кращі книги ти читав, тим гірше спиш.",  # Serhiy Zhadan
    "Найстаріші ґудзики, відомі людству, археологи знайшли в долині ріки Інд.",
    "Слов'янське слово «Україна» вперше згадується у Київському літописному зводі за Іпатіївським списком під 1187 роком.",  # wikipedia
    "Де у Києві найсмачніша кава?",
    "Від Нижнього озера довгими дерев’яними сходами, над якими синьо й біло горіли маленькі коробочки-ліхтарики, підіймалися до нього двоє стовусів: найкращий друг Вертутій і його дванадцятилітній онук Чублик.",  # blyznets_viktor_semenovych/zemlia_svitliachkiv
    "Китайський космічний зонд \"Чан'е-4\" вперше в історії здійснив м'яку посадку на зворотному боці Місяця.",
    "Коли до губ твоїх лишається півподиху, коли до губ твоїх лишається півкроку – зіниці твої виткані із подиву, в очах у тебе синьо і широко.",  # Hryhorij Czubaj
    "Дорогу сестру збираю у дорогу, а брати вирішили не брати машину.",  # homographs
]
