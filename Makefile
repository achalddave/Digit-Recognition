all: train-images train-labels test-image test-labels

train-images:
	curl http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz > train-images.gz
	gunzip train-images.gz
	touch train-images

train-labels:
	curl http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz > train-labels.gz
	gunzip train-labels.gz
	touch train-labels

test-image:
	curl http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz > test-images.gz
	gunzip test-images.gz
	touch test-images

test-labels:
	curl http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz > test-labels.gz
	gunzip test-labels.gz
	touch test-labels

