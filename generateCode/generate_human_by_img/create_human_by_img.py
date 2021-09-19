import random
import os
import shutil
import numpy as np

# download shoes from http://www.makehumancommunity.org/clothes/dudoc_domsjeans1.html
# download hair from http://www.makehumancommunity.org/clothes/mhair02.html
# download top from http://www.makehumancommunity.org/clothes/ballet_costume.html
# download bottom from http://www.makehumancommunity.org/clothes/m_trousers_01.html
# put these files into folder named 'models'
# generate_list: index, cloth texture, model folder name, model file name 


cloth_pic_Folder = 'cloth_pic/'
person_Folder = 'create_person/'
person_save_Folder = person_Folder + 'deepfashion_pair_models/'
basic_personID = 0


def readCSV2List(readCSV2List_filePath):
    try:
        readCSV2List_file = open(readCSV2List_filePath, 'r', encoding="gbk")
        readCSV2List_context = readCSV2List_file.read()
        readCSV2List_result = readCSV2List_context.split("\n")
        readCSV2List_result_length = len(readCSV2List_result)
        for readCSV2List_i in range(readCSV2List_result_length):
            readCSV2List_result[readCSV2List_i] = readCSV2List_result[readCSV2List_i].split(",")
        return readCSV2List_result
    except Exception:
        print("Load data has some problem")
    finally:
        readCSV2List_file.close();

def generateHuman(cloth_list, person_id, sex):
    haveAcc = 0
    # load acc
    hair = open('modeleTxt/hair.txt', 'r').readlines()
    shoe = open('modeleTxt/shoe.txt', 'r').readlines()
    pifu = open('modeleTxt/skin.txt', 'r').readlines()

    if not os.path.exists(person_save_Folder):
        os.makedirs(person_save_Folder)

    if sex > 0:
        Gender1 = 1000000
    else:
        Gender1 = 0
    #     setting
    Gender = '%.6f' % (Gender1 / 1000000)
    Muscle = '%.6f' % (random.randint(0, 1000000) / 1000000)
    African_1 = random.randint(0, 1000000)
    African = '%.6f' % (African_1 / 1000000)
    Asian_1 = random.randint(0, 1000000 - African_1)
    Asian = '%.6f' % (Asian_1 / 1000000)
    Caucasian = '%.6f' % ((1000000 - Asian_1 - African_1) / 1000000)
    if Gender1 > 1000000 / 2:
        m_height = random.gauss(170, 5.7) / 200
        while m_height > 1:
            m_height = random.gauss(170, 5.7) / 200
        Height = '%.6f' % (m_height)
    else:
        m_height = random.gauss(160, 5.2) / 200
        while m_height > 1:
            m_height = random.gauss(160, 5.2) / 200
        Height = '%.6f' % (m_height)
    BreastSize = '%.6f' % (random.randint(0, 70) / 100)
    Age = '%.6f' % (random.randint(20, 90) / 100)
    BreastFirmness = '%.6f' % (random.randint(30, 100) / 100)
    Weight = '%.6f' % (random.randint(0, 1000000) / 1000000)

    file_name = 'B' + str(person_id)
    # creating person file
    f = open(person_save_Folder + file_name + ".mhm", 'a')
    f.write('# Written by MakeHuman 1.1.1\n')
    f.write('version v1.1.1\n')
    f.write('tags ' + file_name + '\n')
    f.write('camera 0.0 0.0 0.0 0.0 0.0 1.0\n')
    f.write('modifier macrodetails-universal/Muscle ' + Muscle + '\n')
    f.write('modifier macrodetails/African ' + African + '\n')
    f.write('modifier macrodetails-proportions/BodyProportions 0.500000\n')
    f.write('modifier macrodetails/Gender ' + Gender + '\n')
    f.write('modifier macrodetails-height/Height ' + Height + '\n')
    f.write('modifier breast/BreastSize ' + BreastSize + '\n')
    f.write('modifier macrodetails/Age ' + Age + '\n')
    f.write('modifier breast/BreastFirmness ' + BreastFirmness + '\n')
    f.write('modifier macrodetails/Asian ' + Asian + '\n')
    f.write('modifier macrodetails/Caucasian ' + Caucasian + '\n')
    f.write('modifier macrodetails-universal/Weight ' + Weight + '\n')
    f.write('skeleton cmu_mb.mhskel\n')
    f.write('eyes HighPolyEyes 2c12f43b-1303-432c-b7ce-d78346baf2e6\n')

    # adding clothes
    if Gender1 > 1000000 / 2:
        f.write(hair[random.randint(0, len(hair) - 1)])
    else:
        f.write(hair[random.randint(0, len(hair) - 1)])
    f.write(shoe[random.randint(0, len(shoe) - 1)])
    for i in range(0, len(cloth_list)):
        f.write(cloth_list[i]+'\n')
    f.write('clothesHideFaces True\n')
    f.write(pifu[random.randint(0, len(pifu) - 1)])
    f.write('material Braid01 eead6f99-d6c6-4f6b-b6c2-210459d7a62e braid01.mhmat\n')
    f.write('material HighPolyEyes 2c12f43b-1303-432c-b7ce-d78346baf2e6 eyes/materials/brown.mhmat\n')
    f.write('subdivide False\n')

def createClothes(modelFolder,modelName, uuid, saveName, saveFolder, imgName):
    def create_mhclo(modelFolder,modelName, uuid, saveName, saveFolder):
        file = 'models/' + modelFolder + '/' + modelName + '.mhclo'
        savePath = saveFolder + '/' + modelFolder + '/'
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        with open(file, "r", encoding="utf-8") as f1, open(savePath + '' + saveName + ".mhclo", "a",
                                                           encoding="utf-8") as f2:
            for line in f1:
                if 'uuid' in line:
                    line = 'uuid ' + uuid + '\n'
                if 'name' in line:
                    line = 'name ' + str(saveName) + '\n'
                if 'material' in line:
                    line = 'material ' + str(saveName) + '.mhmat' + '\n'
                f2.write(line)
        for filename in os.listdir('models/' + modelFolder + '/'):
            if 'mhclo' not in filename and 'mhmat' not in filename:
                shutil.copy('models/' + modelFolder + '/' + filename, savePath)

    def create_mhmat(modelFolder,modelName, uuid, saveName, saveFolder, imgName):
        file = 'models/' + modelFolder + '/' + modelName + '.mhmat'
        savePath = saveFolder + '/' + modelFolder + '/'
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        with open(file, "r", encoding="utf-8") as f1, open(savePath + saveName + ".mhmat", "a",
                                                           encoding="utf-8") as f2:
            for line in f1:
                if 'name' in line:
                    line = 'name ' + str(saveName) + '\n'
                if 'diffuseTexture' in line:
                    line = 'diffuseTexture ' + imgName + '\n'
                f2.write(line)
        shutil.move(cloth_pic_Folder+imgName, savePath + imgName)

    create_mhclo(modelFolder,modelName, uuid, saveName, saveFolder)
    create_mhmat(modelFolder,modelName, uuid, saveName, saveFolder, imgName)


def create_pair_person():
    clothlist = readCSV2List('generate_list.csv')
    personID = basic_personID
    sex = 0
    for i in range(0, len(clothlist), 2):
        try:
            print(i)
            sex = (sex+1)%2
            pair_list = []
            for j in range (i,i+2):
                uuid = '20210919-0000-0000-0000-' + str(j).zfill(12)
                save_name = 'create_'+str(j).zfill(7)
                save_folder = person_Folder+str(personID)
                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)
                img_name = clothlist[j][1]
                pair_list.append('clothes ' + save_name + ' ' + uuid)
                createClothes(clothlist[j][2],clothlist[j][3], uuid, save_name, save_folder, img_name)
            generateHuman(pair_list, personID, sex)
            personID += 1
        except:
            print(i, personID)
create_pair_person()
