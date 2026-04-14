## Others
- Proyect in GitHub: https://github.com/jacesca/pytorch_examples
- Launch jupyter notebook
```
jupyter notebook
```
- Commands to save the environment requirements:
```
conda list -e > requirements.txt
# or
pip list --format=freeze > requirements.txt

conda env export > requirements.yml
```
- For coding style
```
black model.py
flake8 model.py
```

## Extra documentation
- [PreTrained Models](https://pytorch.org/vision/0.9/models.html)
- [Models and pre-trained weights](https://pytorch.org/vision/stable/models.html)
- [PIL - image.open returning wrong type](https://stackoverflow.com/questions/59936504/pil-image-open-returning-wrong-type)
- [ssd300_vgg16](https://pytorch.org/vision/main/models/generated/torchvision.models.detection.ssd300_vgg16.html)
- [Dive into Deep Learning](http://d2l.ai/index.html)
- [14.3. Object Detection and Bounding Boxes](http://d2l.ai/chapter_computer-vision/bounding-box.html)
- [14.6. The Object Detection Dataset](http://d2l.ai/chapter_computer-vision/object-detection-dataset.html)
