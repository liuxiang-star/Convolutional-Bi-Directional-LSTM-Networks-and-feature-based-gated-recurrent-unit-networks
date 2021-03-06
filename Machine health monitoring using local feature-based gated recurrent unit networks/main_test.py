# -*- coding: utf-8 -*-

import pickle
import numpy as np
from Feature_based_GRU import FBGRU
import tensorflow as tf

def load_data(normal_stat=False):
    if normal_stat:
        filepath = "./data/data_normal.p"
    else:
        filepath = "./data/data_seq.p"
    with open(filepath, mode='rb') as f:
        x = pickle.load(f, encoding='latin1')
    return x[0], x[1], x[2], x[3]  # retrun train_x, train_y, test_x, test_y

if __name__ == '__main__':
    train_x, train_y, test_x, test_y = load_data()
    print(train_x.shape)
    print(train_y.shape)

    l = 20  # time steps
    d = 70  # data length
    k = 50  # filter number
    m = 4  # filter size
    s = 2  # pool size
    batch_size = 30  # batch size

    train_x = train_x.reshape([-1, l, d])
    test_x = test_x.reshape([-1, l, d])
    model = FBGRU(MODEL_TYPE     = 'Regression',
                   INPUT_LENGTH   = d,
                   TIME_STEP      = l,
                   CELL_UNITS     = 100,
                   FULL_UNITS     = [100, 400],
                   KEEP_PROB      = 0.5,
                   OUTPUT_NUM     = 1, )

    model.train_model(train_x     = train_x,
                      train_y     = train_y,
                      test_x      = test_x,
                      test_y      = test_y,
                      batch_size  = batch_size,
                      num_epochs  = 1000,
                      num_threads = 4, )




