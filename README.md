# xuexi

## Requirement

    uiautomator2>=2.5.3
    ADB
    安卓模拟器或真机（未经测试）

## Usage

桥接模拟器，或WiFi或USB连接打开了`开发者选项`的真机 **（未经测试）**,确保执行`adb devices`可以看到连接上的设备。直接运行`xuexi.py`。

发表观点在`redwords.json`里，是从[人民网一个活动](http://miaonaiting.people.com.cn/zhutijiaoyu/Myapp/index.php/Index/listrow/p/1/pageSize/20000)下载的。


## TODO
- [x] 登录
- [x] 阅读文章
- [x] 视听学习
- [x] 文章学习时长
- [x] 视听学习时长
- [ ] 每日答题
- [ ] 每周答题
- [ ] 专项答题
- [ ] 挑战答题
- [ ] 订阅
- [x] 收藏
- [x] 分享
- [x] 发表观点
- [x] 本地频道

## 后续思路

不知道为什么答题界面元素都dump不到。可以考虑上OCR，比较麻烦。

一个题库：http://49.235.90.76:5000/

## Reference

https://blog.csdn.net/cumt_TTR/article/details/104027917

https://github.com/kessil/AutoXue

https://github.com/openatx/uiautomator2

https://github.com/IKeepMoving/xuexiqiangguo
