# BirdsOfAlabama
A classifier for 21 species of Alabama birds.

CSVs are provided in image_csvs that can be used to download the same images used to train. The first time the notebook is run, be sure to uncomment a cell to download the images.

If the images are already downloaded and the ImageCleaner is used, uncomment the next cell to make the ImageDataBunch from the generated csv file 'cleaned.csv'.

The model used was resnet18 - the model .pth file for resnet34 was 262 Mb. Github only accepts 100 Mb files, and the resnet18 file was ~50 Mb, with only a small decrease in validation set accuracy.

## Action Shots
![Upload Screen](https://raw.githubusercontent.com/adinhobl/BirdsOfAlabama/master/readme_images/upload.png "Upload Screen")

![Result Screen](https://raw.githubusercontent.com/adinhobl/BirdsOfAlabama/master/readme_images/result.png "Result Screen")