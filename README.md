# StatisticalImageAnalysis
Simple image statistical analysis and data visualization software.

###About
Purpose of this software is to statistically analyze image "defects", using some basic preprocessing image techniques beforehand.

### Usage

To run statistical analysis tool:

1. Install requirements by running the following command:
```
pip install -r requirements.txt
```

2. Run image preprocessing tool on your dataset

```
python code/process.py "DATASET DIRECTORY" "./processed_data/" [OPTIONAL] VALUE_OF_GAMMA
```

3. Run image analysis tool
```
python code/Main.py "processed_data/*.jpg" "PATH TO SAVE RESULTS"

```

#### Examples

Example with directly saving the results to a specific path:

```
python code/Main.py "data/*.jpg" "./statistics_%s.png"
```

Example without saving the results

```
python code/Main.py "test_data/*.gif"
```


### TODO

- [ ] Clean up code to make it reusable for other modalities and following pep-8 standards
- [ ] Add more features


