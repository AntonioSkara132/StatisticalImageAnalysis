# StatisticalImageAnalysis
Simple image statistical analysis and data visualization software.

###About
Purpose of this software is to visualize image data using histograms, with the respect to the matplotlib.pyplot module

### Usage

1. Install requirements by running the following command:
```
pip install -r requirements.txt
```

2. Run the `Main.py` script with the following arguments:

```
python Main.py "PATH_TO_DIR" [OPTIONAL] "PATH_TO_SAVE_RESULTS"
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
