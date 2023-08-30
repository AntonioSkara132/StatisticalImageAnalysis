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
python code/Main.py "processed_data/*.jpg" "PATH TO SAVE RESULTS" 1

```
[OPTIONAL_TOOL] Splits coco format into patches
```
python code/cocoSpliter.py [INPUT_JSON] [OUTPUT_JSON] [ORIGINAl_IMAGES_DIRECTORY] IMAGE_HEIGHT IMAGE_WIDTH

```
Example without saving the results

```
python code/Main.py 
```
Example of cocoSpliter
```
python code/cocoSpliter.py "annotations/_annotations.coco_train.json" "output.json" "/train/" 200 200

```
### TODO

- [ ] Clean up code to make it reusable for other modalities and following pep-8 standards
- [ ] Add more features


