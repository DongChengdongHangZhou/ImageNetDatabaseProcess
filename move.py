import csv
import shutil


def move_val():
    with open("validation_label.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            dir = line.split()[0]
            class_idt = line.split()[1]
            src_dir = './ILSVRC2012_img_val/'+dir
            dst_dir = './val_with_label/'+class_idt+'/'+dir
            try:
                shutil.move(src_dir,dst_dir)
            except:
                pass

move_val()


