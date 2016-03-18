#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import Word2Vec
model = Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
model.init_sims(replace=True)
model.save('google_word2vec_pretrained')
