File Structure：

Source：Code
Data：Databases
Experiments：Experiments results


Data preparation：

1. Put your dataset in the /Data/randperson/, eg:/Data/randperson/randperson_subset

2. modify file: '/Source/reid/datasets/RandPerson.py', change 'self.img_path' (in 11 lines) to your dataset name. eg:randperson_subset。

Train：

1. modify file: '/Source/ablation/train.sh', '--sub_method': Storage subdirectory of experiment results

2. run 'sh train.sh'
