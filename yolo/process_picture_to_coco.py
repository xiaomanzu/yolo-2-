#coding=utf-8
import os
import shutil



#----------------------------------------------------------------------
def pic_to_coco():
    """"""

    test_label_path = 'traffic/TSRD-Test Annotation'
    train_label_path = 'traffic/TSRD-Train Annotation'
    for i in [test_label_path,train_label_path]:
        label_txt = os.listdir(i)
        write_label = []
        with open(os.path.join(i, label_txt[0]), 'r') as f:
            for path in f:
                path = path.strip().split(';')
                pic_name = path[0].split('.')[0]
                w = float(path[1])
                h = float(path[2])
                x1 = float(path[3])
                y1 = float(path[4])
                x2 = float(path[5])
                y2 = float(path[6])
                label_type = path[7]
                coco_center_point_x = ((x2 - x1) / 2 + x1) / w
                coco_center_point_y = ((y2 - y1) / 2 + y1) / h
                coco_w = (x2 - x1) / w
                coco_h = (y2 - y1) / h
                write_label.append(str(label_type))
                write_label.append(str(coco_center_point_x))
                write_label.append(str(coco_center_point_y))
                write_label.append(str(coco_w))
                write_label.append(str(coco_h))
                
                with open(os.path.join(i,pic_name + '.txt'),'w') as s:
                    s.write(' '.join(write_label) + '\n')
                    write_label = []
                
#----------------------------------------------------------------------
def split_test_train():
    """"""
    
    image_path = 'rubbish/images/train'
    label_path = 'rubbish/labels/train'
    #sepa = f'{os.sep}images{os.sep}'
    #sepb = f'{os.sep}labels{os.sep}'
    sepa = '/images/'
    sepb = '/labels/'
    image_list = os.listdir(image_path)
    
    for i,img in enumerate(image_list):
        if i % 9 == 0:
            img = os.path.join(image_path,img)
            label = sepb.join(img.rsplit(sepa,1)).rsplit('.')[0] + '.txt'
            shutil.move(img,'/val/'.join(img.rsplit('/train\\')))
            shutil.move(label, '/val/'.join(label.rsplit('/train\\')))
            
            
    
    
    
                


if __name__ == '__main__':
    #pic_to_coco()
    split_test_train()