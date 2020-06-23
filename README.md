# RandPerson
This project contains the ReandPerson dataset described in our paper "Surpassing Real-World Source Training Data: Random 3D Characters for Generalizable Person Re-Identification".

&nbsp;
<p align="center"><img width=700 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/unity.png"></p>
<p align="center">Fig. 1. Sample images from the proposed RandPerson dataset.</p>
&nbsp;

## Table of Contents

- [Dataset Description](#link-of-the-dataset)
- [Characters and Scenes](#characters-and-scenes)
- [Experimental Results](#experimental-results)
- [Contacts](#contacts)
- [Citation](#citation)

## Dataset Description

The RandPerson dataset is generated by [MakeHuman](http://www.makehumancommunity.org/) and [Unity3D](https://unity.com/). This is the first synthetic person re-identification dataset with a set-up similar to real video
surveillance systems, i.e. with a camera network and multiple people moving at the same time. The dataset contains 1,756,759 synthesized
person images of 8,000 identities. Images in this dataset generally contain different viewpoints, poses, illuminations, backgrounds, occlusions, and resolutions, as shown in Fig. 1. 

### Download Links
Due to the large amount of data, currently only the image subset used in the experiments of our paper is provided, including 128,160 images. They can be downloaded from the following links.

* [Baidu Yun Drive](https://pan.baidu.com/s/1peTSlhze9BzDQGbcakkz2w) (code: ueeg)
* [Google Drive](https://drive.google.com/file/d/12u1xdVo6-Q-i_knsbrBrRkClFkq10oNH/view?usp=sharing)

### File Structure
```shell
randperson_subset
├── 000000_c00_s00_f000264.jpg
├── 000000_c00_s00_f001032.jpg
├── 000000_c01_s00_f001632.jpg
```

The filenames are encoded as follows. Take "000000_c00_s00_f000264.jpg" as an example,
*  000000 is the id of the person
*  c00   is the id of the camera
*  s00   is the id of the scene
*  f000264   is the number of frames

## Characters and Scenes

We propose to generate a large number of clothing models by randomly generating a lot of UV texture maps. Then a new clothing model can be created by choosing an existing clothing model, and replacing its UV texture map with a generated one. Fig. 2 shows examples of generated clothing and characters.

<p align="center"><img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/makehuman.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/scene.png"></p>
<p align="center">&nbsp;&nbsp;&nbsp; Fig. 2. Examples of generated clothes and characters. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fig. 3. Customized Unity3D scenarios used in this work.</p>

For the rendering in Unity3D, we obtain a set of customized environments, including 11 scenes, eight outdoor and three indoor, as shown in Fig. 3. Then, we set up a network with multiple cameras for each scene, and run them simultaneously in the virtual environments, simulating real video surveillance. An example is shown in Fig. 4. Then, the randomly generated characters can be imported and move simultaneously through the camera network.

<p align="center"><img width=600 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/scene_detail.png"></p>
<p align="center">Fig. 4. Example configuration of camera networks and character movements.</p>

## Experimental Results

To validate the effectiveness of the RandPerson dataset, we apply a basic deep learning model for cross-dataset person re-identification. The experimental results are shown in the following tables.

<p align="center"><img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table2.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table3.png"></p>

<p align="center"><img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table4.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height=300 src="https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table5.png"></p>

## Contacts

Yanan Wang

Inception Institute of Artificial Intelligence (IIAI)

yanan.wang@inceptioniai.org

## Citation

@article{RandPerson,

  author    = {Yanan Wang and Shengcai Liao and Ling Shao},
               
  title     = {Surpassing Real-World Source Training Data: Random {3D} Characters for Generalizable Person Re-Identification},
  
  journal   = {arXiv:2006.xxxx},
  
  year      = {2020}
  
}

