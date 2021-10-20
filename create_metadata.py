import os
import numpy as np

train_dataset = 'train'
test_dataset = 'test'
metadata_dir = 'metadata'

# train metadata
train_labels = []
train_image_paths = []

for dir in os.listdir(train_dataset):
    print(dir)
    train_labels.append(dir)
    for filename in os.listdir(train_dataset + '/' + dir):
        train_image_paths.append(dir + '/' + filename)
        print(dir + '/' + filename)

with open(metadata_dir + '/' + train_dataset + '/image_paths.npy', 'wb') as f:
    np.save(f, train_image_paths)

with open(metadata_dir + '/' + train_dataset+ '/labels.npy', 'wb') as f:
    np.save(f, train_labels)

# test metadata

test_labels = []
test_image_paths = []

for dir in os.listdir(test_dataset):
    print(dir)
    test_labels.append(dir)
    for filename in os.listdir(test_dataset + '/' + dir):
        test_image_paths.append(dir + '/' + filename)
        print(dir + '/' + filename)

with open(metadata_dir + '/' + test_dataset + '/image_paths.npy', 'wb') as f:
    np.save(f, test_image_paths)

with open(metadata_dir + '/' + test_dataset+ '/labels.npy', 'wb') as f:
    np.save(f, test_labels)