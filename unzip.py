import os
import tarfile
import shutil

def rename_file():
    srcfile = 'zz.rar'
    dstfile = 'kk.rar'
    os.rename(srcfile,dstfile)

def unzip():
    file_name = ''
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    #因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()


def remove_file():
    pass


def move_file():
    with open("validation_label.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            srcdir='ILSVRC2012_img_val/'+line.split()[0]
            dstdir='val_with_label/'+line.split()[1]
            shutil.move(srcdir,dstdir)


if __name__ == '__main__':
    move_file()