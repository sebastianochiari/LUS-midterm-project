# Default command
.DEFAULT_GOAL := help

help:	## Show this help message
	@fgrep -h '##' $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

setup: ## Edit system permission to run the bash scripts
	@chmod +x batch.sh
	@chmod +x clean.sh
	@chmod +x test.sh
	@chmod +x train.sh

train: 	## Train the basic model
	@## ORDER param: specify the ngram order (integer number)
	@## METHOD param: specify the smoothing method to build the language model
	@## possible values [absolute, katz, kneser_ney, presmoothed, unsmoothed, witten_bell]
	@## CUTOFF param: optional, by default set equal to 2
	@./train.sh $(order) $(method) $(cutoff)

test: 	## Test the basic model
	@## ORDER param: specify the ngram order (integer number)
	@## METHOD param: specify the smoothing method to build the language model
	@## possible values [absolute, katz, kneser_ney, presmoothed, unsmoothed, witten_bell]
	@## CUTOFF param: optional, by default set equal to 2
	@## !! TESTING IS PERFORMED BASED ON THE FILES CONTAINED IN THE FOLDER AFTER TRAINING !!
	@## parameters has to be specified in order to rename uniquely the results.csv file
	@./test.sh $(order) $(method) $(cutoff)

run:  ## Run train and test on the model with the specified parameters
	@## ORDER param: specify the ngram order (integer number)
	@## METHOD param: specify the smoothing method to build the language model
	@## possible values [absolute, katz, kneser_ney, presmoothed, unsmoothed, witten_bell]
	@## CUTOFF param: optional, by default set equal to 2
	@./train.sh $(order) $(method) $(cutoff)
	@./test.sh $(order) $(method) $(cutoff)
	@./clean.sh

all: ## Run a set of multiple train and test with different parameters
	@./batch.sh

clean: 	## Clean all the temporary files generated during train and test
	@./clean.sh