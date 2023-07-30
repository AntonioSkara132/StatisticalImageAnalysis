# StatisticalImageAnalysis
Simple image statistical analysis software

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

Example with a test_data, position yourself in a StatisticalImageAnalysis directory

```
python code/Main.py "data/*.jpg" "./statistics_%s.png""
```

### TODO

- [ ] Clean up code to make it reusable for other modalities and following pep-8 standards
- [ ] Add more features
