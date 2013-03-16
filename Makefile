all: data train-images train-labels test-image test-labels

data:
	mkdir data

train-images:
	curl http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz > data/train-images.gz
	gunzip data/train-images.gz
	touch data/train-images

train-labels:
	curl http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz > data/train-labels.gz
	gunzip data/train-labels.gz
	touch data/train-labels

test-image:
	curl http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz > data/test-images.gz
	gunzip data/test-images.gz
	touch data/test-images

test-labels:
	curl http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz > data/test-labels.gz
	gunzip data/test-labels.gz
	touch data/test-labels
