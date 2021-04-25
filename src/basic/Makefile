# Default command
.DEFAULT_GOAL := help

help:	## Show this help message
	@fgrep -h '##' $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

run:  ## Run train and test on the model with the specified parameters
	@## ORDER param: specify the ngram order (integer number)
	@## METHOD param: specify the smoothing method to build the language model
	@## possible values [absolute, katz, kneser_ney, presmoothed, unsmoothed, witten_bell]
	@## CUTOFF param: by default to 2, can be modified inside basic.py
	@./train.sh $(order) $(method)
	@./test.sh
	@./clean.sh

train: 	## Train the basic model
	@## ORDER param: specify the ngram order (integer number)
	@## METHOD param: specify the smoothing method to build the language model
	@## possible values [absolute, katz, kneser_ney, presmoothed, unsmoothed, witten_bell]
	@## CUTOFF param: by default to 2, can be modified inside basic.py
	@./train.sh $(order) $(method)

test: 	## Test the basic model
	@./test.sh

clean: 	## Clean all the temporary files generated during train and test
	@./clean.sh