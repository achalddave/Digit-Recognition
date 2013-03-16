all: data train-images train-labels test-image test-labels

data:
	mkdir data

train-images:
	curl http://www.ocf.berkeley.edu/~achal/mnist-data/train-images.gz > data/train-images.gz
	gunzip data/train-images.gz
	touch data/train-images

train-labels:
	curl http://www.ocf.berkeley.edu/~achal/mnist-data/train-labels.gz > data/train-labels.gz
	gunzip data/train-labels.gz
	touch data/train-labels

test-image:
	curl http://www.ocf.berkeley.edu/~achal/mnist-data/test-images.gz > data/test-images.gz
	gunzip data/test-images.gz
	touch data/test-images

test-labels:
	curl http://www.ocf.berkeley.edu/~achal/mnist-data/test-labels.gz > data/test-labels.gz
	gunzip data/test-labels.gz
	touch data/test-labels
