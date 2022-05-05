import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
sets = ['train', 'test', 'val']
 
classes = ["充电宝",
        "包",
        "洗护用品",
        "塑料玩具",
        "塑料器皿",
        "塑料衣架",
        "玻璃器皿",
        "金属器皿",
        "快递纸袋",
        "插头电线",
        "旧衣服",
        "易拉罐",
        "枕头",
        "毛绒玩具",
        "鞋",
        "砧板",
        "纸盒纸箱",
        "调料瓶",
        "酒瓶",
        "金属食品罐",
        "金属厨具",
        "锅",
        "食用油桶",
        "饮料瓶",
        "书籍纸张",
        "垃圾桶",
        "塑料厨具",
        "毛巾",
        "纸袋",
        "饮料盒",
        "剩饭剩菜",
        "大骨头",
        "果皮果肉",
        "茶叶渣",
        "菜帮菜叶",
        "蛋壳",
        "鱼骨",
        "干电池",
        "软膏",
        "过期药物",
        "一次性快餐盒",
        "污损塑料",
        "烟蒂",
        "牙签",
        "花盆",
        "陶瓷器皿",
        "筷子",
        "污损用纸"]  # 类别
 
 
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
 
 
def convert_annotation(image_id):
    in_file = open('Annotations/%s.xml' % (image_id),encoding='utf-8')
    out_file = open('labels/%s.txt' % (image_id), 'w')
    # in_file = open('train/Annotations/%s.xml' % (image_id))
    # out_file = open('train/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
 
wd = getcwd()
print(wd)
'''
for image_set in sets:
    if not os.path.exists('/home/trainingai/zyang/yolov5/paper_data/labels/'):
        os.makedirs('/home/trainingai/zyang/yolov5/paper_data/labels/')
    image_ids = open('/home/trainingai/zyang/yolov5/paper_data/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('paper_data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/paper_data/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()

    if not os.path.exists('train/labels/'):
        os.makedirs('train/labels/')
    image_ids = open('train/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('train/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('train/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
'''
for image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    image_ids = open('ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/ma-user/work/yolov5-test/trash/VOC2007/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()