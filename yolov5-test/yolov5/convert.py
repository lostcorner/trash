import torch

aaa=torch.load('/home/ma-user/work/yolov5-test/yolov5/test.pt')

# print(aaa['model'].names)

aaa['model'].names=['充电宝','包','洗护用品','塑料玩具','塑料器皿','塑料衣架','玻璃器皿','金属器皿','快递纸袋','插头电线',
        '旧衣服','易拉罐','枕头','毛绒玩具','鞋','砧板','纸盒纸箱','调料瓶','酒瓶','金属食品罐','金属厨具','锅','食用油桶',
        '饮料瓶','书籍纸张','垃圾桶','塑料厨具','毛巾','纸袋','饮料盒','剩饭剩菜','大骨头','果皮果肉','茶叶渣','菜帮菜叶',
        '蛋壳','鱼骨','干电池','软膏','过期药物','一次性快餐盒','污损塑料','烟蒂','牙签','花盆','陶瓷器皿','筷子','污损用纸']

# print(aaa['model'].names)


torch.save(aaa, '/home/ma-user/work/yolov5-test/yolov5/testaaa.pt') 

bbb=torch.load('/home/ma-user/work/yolov5-test/yolov5/testaaa.pt')

print(aaa['model'].names)
print(bbb['model'].names)
print(bbb['model'])

