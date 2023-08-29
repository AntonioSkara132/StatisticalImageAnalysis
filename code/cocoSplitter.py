from pycocotools import coco
import utils
import json
from tqdm import tqdm
import sys



def polygon_area(x_s, y_s):
    n = len(x_s)
    area = 0

    for i in range(n):
        x1 = x_s[i]
        y1 = y_s[i]
        x2 = x_s[(i + 1) % n]
        y2 = y_s[(i + 1) % n]
        # Next vertex (wraps around for the last vertex)
        area += (x1 * y2 - x2 * y1)

    return round(0.5 * abs(area),2)

def main():
    save_json = "_annotations.coco.json"
    if len(sys.argv) > 1:
        dir_json = sys.argv[1]
        if len(sys.argv > 2):
            save_json = sys.argv[2]
    else:
        print("No directory specified!")
        exit(-1)

    data = coco.COCO(dir_json)
    info = {}
    licenses = []
    images = []
    annotations = []
    categories = []

    files = data.imgs

    info =  {"year": "2023", "version": "10", "description": "Exported from roboflow.com", "contributor": "",
             "url": "https://public.roboflow.com/object-detection/undefined",
             "date_created": "2023-08-21T17:48:20+00:00"}
    licenses = [{"id":1,"url":"https://creativecommons.org/licenses/by/4.0/","name":"CC BY 4.0"}]

    categories.append({"id": 0, "name": "holes", "supercategory": "none"})

    patch_height = 200
    patch_width = 200

    id = 0

    for image_id in tqdm(range(len(files))):
        ann_ids = data.getAnnIds(imgIds=image_id, catIds=1)
        for y_start in range(0, 2000, 200):
            for x_start in range(0, 2400, 200):
                images.append({"id": id, "license": 1, "file_name": "patch_" + str(id) + ".jpg", "height": patch_height, "width": patch_width,
                               "date_captured": "2023-08-21T17:48:20+00:00"})
                id+=1
                for ann_id in ann_ids:
                    segmentation = data.anns[ann_id]["segmentation"][0]
                    x_s = [segmentation[i] for i in range(0,len(segmentation), 2)]
                    #print(x_s)
                    y_s = [segmentation[i] for i in range(1,len(segmentation), 2)]
                    #print(y_s)
                    new_segmentation = []
                    for i in range(len(x_s)):
                        #print(x_s[i], y_s[i], x_start, y_start)
                        if (x_start <= x_s[i] < (x_start+200)) and (y_start <= y_s[i] < (y_start+200)):
                            #print(x_s[i], y_s[i], x_start, y_start)
                            new_segmentation.append(round(x_s[i] - x_start, 2))
                            new_segmentation.append(round(y_s[i] - y_start, 2))
                    if len(new_segmentation) == 0:continue
                    segmentation = new_segmentation
                    x_s = [segmentation[i] for i in range(0, len(segmentation), 2)]
                    y_s = [segmentation[i] for i in range(1, len(segmentation), 2)]
                    xmin = int(min(x_s))
                    ymin = int(min(y_s))
                    xmax = int(max(x_s))
                    ymax = int(max(y_s))
                    bbox = [xmin, ymin, xmax - xmin, ymax - ymin]
                    area = polygon_area(x_s, y_s)
                    annot = {"id": id, "image_id": image_id,
                             "category_id": 0, "bbox": bbox,
                             "area": area,
                             "segmentation": [segmentation],
                             "iscrowd": 0}
                    annotations.append(annot)
    new_coco = {"info": info, "licenses": licenses, "categories": categories,  "images": images, "annotations": annotations}
    with open("../annotations/_annotations.coco.json", "w") as json_file:
        json.dump(new_coco, save_json)

if __name__ == "__main__":
        main()

