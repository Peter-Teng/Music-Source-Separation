import random
import os
import shutil

'''
In this script, we split the wav files in MIR-1K train set.
'''

data_path = "/home/dhp/datasets/MIR-1K/"
train_path = "/home/dhp/datasets/MIR-1K/train"
test_path = "/home/dhp/datasets/MIR-1K/test"
wav_path = os.path.join(data_path, "UndividedWavfile")

if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(test_path):
    os.makedirs(test_path)

audios = os.listdir(wav_path)
audios.sort()
print(len(audios))
seed = 42
random.seed(seed)

test_size = 30
test_list = []
while True:
    # randomly choose 30 wav file as test set
    index = random.choice(range(len(audios)))
    if index not in test_list:
        test_list.append(index)
        shutil.copyfile(os.path.join(wav_path, audios[index]), os.path.join(test_path, audios[index]))
    if len(test_list) == 30:
        break


# generate the train set
for index in range(len(audios)):
    if index not in test_list:
        shutil.copyfile(os.path.join(wav_path, audios[index]), os.path.join(train_path, audios[index]))

print("---------------------Information--------------------------")

print("The train wav files are: ")
for index in range(len(audios)):
    if index not in test_list:
        print(audios[index].split('.')[0])

print("\n----------------------------------------------------------\n")

print("The test wav files are: ")
for index in test_list:
    print(audios[index].split('.')[0])
