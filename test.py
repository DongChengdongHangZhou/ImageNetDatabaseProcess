import csv
from io import StringIO


def make_train_label_simple():
    name_list = [0 for x in range(1000)]
    with open("train_label.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            name = line.split()[0][0:9]
            label = int(line.split()[1])
            name_list[label] = name

    print(len(name_list))

    with open("imagenet2coco.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            name = line.split()[0]
            if line.split()[-1]=='None':
                flag = ' 1'

            if line.split()[-1]!='None':
                flag = ' 0'
            index = name_list.index(name)
            name_list[index] = name+flag

    with open("train_label_simple.txt","w") as f:
        for i in range(1000):
            f.write(name_list[i]+' '+str(i)+'\n')

def make_imagenet_info_csv():
    index_list = []
    string_list = []
    coco_class_list = [0 for x in range(1000)]
    object_name_list = [[] for x in range(1000)]
    csv_file = open('imagenet_info.csv','w',newline='')
    writer = csv.writer(csv_file)
    with open("train_label_simple.txt", "r") as train_label_simple_file:
        for line in train_label_simple_file.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            index_list.append(line.split()[-1])
            string_list.append(line.split()[0])

    with open("imagenet2coco.txt", "r") as imagenet2coco_file:
        for line in imagenet2coco_file.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            coco_class = line.split()[-1]
            string = line.split()[0]
            object_name = line.split('\t')[1]
            object_name = object_name.split(', ')
            flag = string_list.index(string)
            coco_class_list[flag] = coco_class
            object_name_list[flag] = object_name

    for i in range(1000):
        info = [index_list[i],string_list[i],coco_class_list[i]]+object_name_list[i]
        writer.writerow(info)


make_imagenet_info_csv()


