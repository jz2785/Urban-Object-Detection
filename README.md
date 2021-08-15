# Object Detection in an Urban Environment

### Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

### Set up

This is setup for the provided environement, we have to redownload and process the files due to a bug in the provided download_process.py
Run `bash launch_download.sh` and give `/tmp` as answer where to install the SDK since we do not have enough disk space for both the google cloud SDK and the TFrecords. Then answer yes to add gsutil to the path and the script `/home/workspace/.student_bashrc`. The bash file `launch_download.sh` will automatically  reload the configuration and start the download process.

### Dataset
#### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.
#### Cross validation

Train - Test
Train -> repeated k-cross validation to get an accurate prediction accuracy 

### Training 
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
 
## TODO
See "5. Submission" for which files have to be in the submission and repository

* ~~Git~~
* Exploratory Data Analysis
* Create the splits
* Edit the config file
* Training
* Improve the performances
* Creating an animation
* Class level metrics
* Custom augmentation
* Run the pep8 package
* requirements.txt
* Check [Review criteria](https://review.udacity.com/#!/rubrics/2940/view) again