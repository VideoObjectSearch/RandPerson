# RandPerson
This project contains the ReandPerson dataset described in our paper "[Surpassing Real-World Source Training Data: Random 3D Characters for Generalizable Person Re-Identification](https://arxiv.org/abs/2006.12774)".  

<p align="center"><img width=700 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/unity.png"></p>
<p align="center">Fig. 1. Sample images from the proposed RandPerson dataset.</p>  

## Table of Contents

- [Dataset Description](#link-of-the-dataset)
- [Characters and Scenes](#characters-and-scenes)
- [Experimental Results](#experimental-results)
- [Contacts](#contacts)
- [Citation](#citation)

## Dataset Description

The RandPerson dataset is generated by [MakeHuman](http://www.makehumancommunity.org/) and [Unity3D](https://unity.com/). This is the first synthetic person re-identification dataset with a set-up similar to real video surveillance systems, i.e. with a camera network and multiple people moving at the same time. The dataset contains 1,801,816 synthesized person images of 8,000 identities. Images in this dataset generally contain different viewpoints, poses, illuminations, backgrounds, occlusions, and resolutions, as shown in Fig. 1. 

### Download Links
Due to the large amount of data, currently only the image subset used in the experiments of our paper is provided in Google Drive, including 132,145 images. All data is provided in Baidu Yun Drive, including videos and images (The video is uploading). Images include images and key points position. They can be downloaded from the following links. 

* [Baidu Yun Drive](https://pan.baidu.com/s/1nfjRzNmxMKddYmVALoXfNw) (code: v6mt)
* [Google Drive](https://drive.google.com/file/d/1qIFvTPt1q37_xWeGbFumZag6uAx9c4--/view?usp=sharing)

### File Structure
```shell
randperson
├── images
│   ├── scene00
│   │      ├── camera0_1.tar.gz  # This file contains valid pictures in camera0_1.mp4
│   │      │      ├── 000000_s00_c00_f000264.jpg
│   │      │      ├── 000000_s00_c00_f001032.jpg
│   │      │      ├── 000000_s00_c01_f001632.jpg
│   │      ├── camera0_1_point.txt # This file contains key points position of the images in camera0_1.tar.gz. 
│   │      ├── delete_camera0_1.tar.gz # Because the key points may also be recorded when the model is destroyed, we move the last picture of each id after cutting the picture to the file
│   │      ├── camera0_2.tar.gz
│   │      ├── camera0_2_point.txt
│   │      ├── delete_camera0_2.tar.gz
│   │      ├── camera1_1.tar.gz
│   │      ├── camera1_1_point.txt
│   │      ├── delete_camera1_1.tar.gz
│   │      ├── camera1_2.tar.gz
│   │      ├── camera1_2_point.txt
│   │      ├── delete_camera1_2.tar.gz
│   ├── scene01
│   ```
│   ├── scene10
│   ├── subset
├── videos
│   uploading...
├── readme.txt
│   uploading...
```
The filenames are encoded as follows. Take "000000_s00_c00_f000264.jpg" as an example,
*  000000 is the id of the person
*  s00   is the id of the scene
*  c00   is the id of the camera
*  f000264   is the number of frames

camera*_*_point.txt Data format: image name, the upper left corner of the video x, the upper left corner of the video y, the lower right corner of the video x, the lower right corner of the video y, the distance of head point in the image from the upper left corner x (The following distances are from the upper left corner), the distance y of head point in the image, left shoulder distance x, left shoulder distance y, right shoulder x, right shoulder y, left hand x, left hand y, right hand x, right hand y, left foot x, left foot y, right foot x, right foot y

## Characters and Scenes

We design a method to generate a large number of random UV texture maps and use them to create different 3D clothing models. The method is shown in Fig2, colors and texture patterns are combined to create random UV texture maps. Fig.3 shows the texture patterns we used is shown. Then, an automatic code is developed to randomly generate various different 3D characters with diverse clothes, races and attributes. Fig. 4 shows examples of our generated clothing and characters.

<p align="center"><img height=200 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/color.png"><img height=200 width=200 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/pattern.png"></p>

<p align="center">&nbsp;&nbsp;&nbsp; Fig. 2. Illustration of how to generate UV texture maps. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fig. 3. Texture patterns used in this work.</p>


<p align="center"><img height=200 width=315 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/makehuman.png"><img height=200 width=465 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/scene.png"></p>

<p align="center">&nbsp;&nbsp;&nbsp; Fig. 4. Examples of generated clothes and characters. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fig. 5. Customized Unity3D scenarios used in this work.</p>

Next, we simulate a number of different virtual environments (including 11 scenes, eight outdoor and three indoor, as shown in Fig. 5) using Unity3D, with customized camera networks similar to real surveillance systems. Finally, we import multiple 3D characters at the same time, with various movements and interactions along different paths through the camera networks. The simulation is illustrated in Fig. 6.

<p align="center"><img width=600 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/scene_detail.png"></p>
<p align="center">Fig. 6. Example configuration of camera networks and character movements.</p>

## Experimental Results

By training person re-identification models on these synthesized person images, we demonstrate, for the first time, that models trained on virtual data can generalize
well to unseen target images, surpassing the models trained on various real-world datasets, including CUHK03, Market-1501, DukeMTMC-reID, and almost MSMT17. The experimental results are shown in the following tables.

<p align="center"><img height=250 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table1.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height=250 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table2.png"></p>

<p align="center"><img height=250 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table3.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height=250 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table4.png"></p>

## Contacts

Yanan Wang  
Inception Institute of Artificial Intelligence (IIAI)  
yanan.wang@inceptioniai.org

## Citation

```
@inproceedings{wang2020surpassing,
	title={{Surpassing Real-World Source Training Data: Random 3D Characters for Generalizable Person Re-Identification}},
	author={Wang, Yanan and Liao, Shengcai and Shao, Ling},
	booktitle={28th ACM International Conference on Multimedia (ACMMM)},
	year={2020}
}
```
