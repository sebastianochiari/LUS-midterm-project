# LUS midterm project
**Concept tagging module for movie domain**. Midterm project for *Language Understanding Systems* course @ UNITN.

The main dataset used for train and test the model is [`NL2SparQL4NLU`](https://github.com/esrel/NL2SparQL4NLU). The other datasets used for comparing the module performance are the following:
- [`ATIS Dataset`](https://github.com/howl-anderson/ATIS_dataset)
- [`NLU evaluation corpora`](https://github.com/sebischair/NLU-Evaluation-Corpora)
- [`NLU benchmark`](https://github.com/sonos/nlu-benchmark)

The detailed description of the whole module can be found inside the `report.pdf`. 

### ⚙️ Requirements
- `Python` (version `3.9.2`)
- [`OpenFST`](http://www.openfst.org/twiki/bin/view/FST/WebHome) library
- [`OpenGRM`](http://www.opengrm.org) Ngram library

### 🔧 How to use
- Clone the repository `https://github.com/sebastianochiari/LUS-midterm-project`
- Install all the dependencies listed above
- Move to the model folder of your choice `src/basic`, `src/no_O` or `src/normalized` (more info about model implementation can be found further down in the README or in the `report.pdf`)
- 
- Run the command `make` or `make help`, which will display all the instructions to run correctly the model

Each **makefile** has the following commands:
- `make`  
Default command, it runs the `make help` command
- `make help`  
Diplays the help message, with all the instructions to run correctly the model
- `make train order=<num> method=<method>`  
Trains the model with the specified `order` and `method` 
- `make test order=<num> method=<method>`  
Tests the model just trained. Testing is performed based on the files contained in the folder after training; parameters are optional and they are used to rename the `results.csv` file
- `make run order=<num> method=<method>`  
Performs train and test of the model with the specified `order` and `method`. At the end, it cleans the directory from all the temporary files generated.
- `make clean`  
Cleans the directory from all the temporary files generated during train and test (excluded the `results` file)

### 📝 Models

