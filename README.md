# Object Detection in an Urban Environment

### Project overview
In this project, we look at object detection in camera images. Object detection has a wide variety of application, but for this course we are specifically interested in the application of self driving cars, where object detection is used for scene understanding. Good scene understanding is important for reliable driving. 

### Set up

A local setup was used, as there were minor and major issues with the provided workspace including too little space for processing the files and larger jupyter notebooks, crashing internet browser etc.

To run the code, Anaconda is recommended. Python 3.8 was used. See requirements.txt for the required python packages. It is also required to install the Google Cloud SDK and has to be added to the path. Additionally the Tensorflow Object Detection API is necessary, commit `3db445c7b0404f9b98cbc47616bab08bfa3d8130` was used to create the report, see [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html) for the installation process. One has to apply to the [Waymo open dataset](https://waymo.com/open/) and install the python package and then run the `launch_download.sh` to download the data and preprocess it. To create the videos ffmpeg has to be also installed, one can check on linux whether the binary is accessible in the path using `which ffmpeg`.

### Dataset
#### Dataset analysis - A quantitative and qualitative description of the dataset

Here we try to understand our dataset by a quantitative and qualitative analysis. By plotting images from different files we can tell that they are from seperate rides, we created an animation of one ride, see the file [here](./visualizations/one_ride.mp4) and the following 10 images from one ride:
![10 images of a ride with bounding boxes](./visualizations/ten_images.png)

Using cluster analysis on the mean and standard deviation of pixel values we can see there are at least two clusters, the first being day driving and the second during the night:

![T-SNE of the pixel values](./visualizations/tsne_pixel_values.png)
Cluster 1:
![3 Images of the 1st cluster](./visualizations/cluster_0.png)
Cluster 2:
![3 Images of the 2nd cluster](./visualizations/cluster_1.png)

But we can see there are only 9 files in our dataset for night driving which we may take into account during data splitting.

We count the occurances of the different classes and show them in the following figure

![Class occurances](./visualizations/class_occurances.png)

we can see that there are much fewer bounding boxes for cyclists in the dataset which we will have to be careful about when splitting the dataset.

#### Cross validation

One common way to do splitting is to just do random splits, however since this data has similar characteristics to time series prediction, randomly splitting across the whole dataset could potentially underestimate the error in practice. Instead, the course guidelines suggest to just split in terms of files, this approach should not suffer from the afformentioned problem. Having decided on just splitting in terms of files, we now have to decide on the splitting of the files. We decided on a 70%, 15%, 15% split and have formulated an objective in terms of the class balance and day/night scenario balance in the train, validation and test set. This objective then was minimized using a simulated annealing approach (see the jupyter notebook for details) to compute the resulting splits saved to the files `filenames_training.txt`, `filenames_validation.txt` and `filenames_test.txt`.

### Training 
#### Reference experiment
Here the `edit_config.py` was used to create a `pipeline_new.config` which the reference model was trained with. The model was then also evaluated using the validation set which is shown as the blue dot in the following plots, whereas the training metrics are shown in orange.

![Images of tensorboard plots](./visualizations/screenshot_0.png)

Unsurprisingly, as a pretty small dataset was used, there is quite a gap between training and validation loss.

We can also see the precision and recall using the validation set;

![Images of tensorboard plots](./visualizations/screenshot_1.png)
![Images of tensorboard plots](./visualizations/screenshot_2.png)

#### Improve on the reference
First multiple augmentations were added, hopping that the gab between training and validation loss smaller can be made smaller, by brining more variation in the training data.
The augmentations include

* random_horizontal_flip
* random_crop_image
* random_adjust_saturation
* random_adjust_brightness
* random_adjust_contrast
* random_black_patches
* random_jpeg_quality
* random_jitter_boxes

Let's have a look at some of the augmented images:

![Augmented image 0](./visualizations/augmented_image0.png)
![Augmented image 1](./visualizations/augmented_image1.png)
![Augmented image 2](./visualizations/augmented_image2.png)

Looking at the model zoo of the tensorflow object detection API, 

![Model zoo TF OD API](./visualizations/model_zoo_screenshot.png)

we can see that EfficientDet has a better mAP score, which is why EfficientDet was used for the second model. Due to limited GPU memory with this bigger model, the batch size was reduced to 3.
The optimizer was also changed to Adam which requires lower learning rates on this example. Let's have a look at the results, the old results are still being shown overlayed. The new training loss is shown in red whereas the validation loss is shown in light blue.

![Images of tensorboard plots](./visualizations/screenshot_improved.png)
![Images of tensorboard plots](./visualizations/precision_improved.png)
![Images of tensorboard plots](./visualizations/recall_improved.png)

As we can see the localization loss is much smaller, the train validation gap is smaller and the precision is also quite a bit better.

Now the test errors are reported, these were generated by changing the pipline config files to point to the test folders and then rerunning the evaluation.

Model | Precision/mAP@.50IOU | Recall/AR@100 | Classification loss | Localization loss
------------ | ------------- | ------------- | ------------- | -------------
Reference | 0.296298 | 0.207544 | 0.391801 | 0.493153
Improved | 0.337684 | 0.218508 | 0.231632 | 0.018697

An animation of a test ride is stored [here](./visualizations/animation.mp4).

## TODO
* Run the pep8 package
* requirements.txt
* Check [Review criteria](https://review.udacity.com/#!/rubrics/2940/view) again
