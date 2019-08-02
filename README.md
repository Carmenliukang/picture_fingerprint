# 鲁班商品按照cid 分类后去重
鲁班商品按照cid 分类后去重

1. 具体的流程如下：
    1. 获取 cid 类型。
    2. 获取 每一种 cid 的 goods detail
    3. 使用 进程池 方式 开始运行。备注 测试后 发现 4个进程 是可以 支持的。
    4. 将结果存储到 MySQL 中
    
2. 相关表结构的说明:
    1. luban_goods_detail 鲁班商品的商品数据
    2. luban_goods_product_id_image cid product_id image 对应关系。
    
3. 相关说明：
    1. 代码整体已经注释了，有相关具体的需求，可以邮件联系
    2. 优化了代码,每次图片都只计算一次 hash 数值
    
