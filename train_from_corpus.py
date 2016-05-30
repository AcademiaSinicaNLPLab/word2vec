#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def parse_arg(argv):
    parser = argparse.ArgumentParser(description='train word2vec model')
    parser.add_argument('-s', '--size', type=int, default=400, help='word vector dimension')
    parser.add_argument('-w', '--window', default=5, help='window size')
    parser.add_argument('-m', '--mincount', default=5, help='minimum count for high frequency word')
    parser.add_argument('-d', '--debug', action='store_true', help="store c compaitable model")
    parser.add_argument('-f', '--full_model', action='store_false', help="do not trim model, which save much memory")
    parser.add_argument('input', help='File path of the training corpus')
    parser.add_argument('output', help='File path of the output data')
    return parser.parse_args(argv[1:])

if __name__ == '__main__':
    args=parse_arg(sys.argv)

    with open(args.input) as f:
        model=Word2Vec(LineSentence(f), size=args.size, window=args.window,
                       min_count=args.mincount, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    if not args.full_model:
        model.init_sims(replace=True)

    model.save(args.output)
    if args.debug:
        model.save_word2vec_format(outp + '.compaitable', binary=False)
