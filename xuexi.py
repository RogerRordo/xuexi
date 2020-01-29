# -*- coding: UTF-8 -*-
import uiautomator2 as u2
from logzero import logger
from time import sleep
import json
import random

DEBUG = False  # 调试模式下，文章和视频逗留时间只有2秒
DELAY_TIME = 2  # 每个操作后的默认缓冲延时（秒）


def click(x, delay=DELAY_TIME):
    x.click()
    sleep(delay)


def press_back(delay=DELAY_TIME):
    d.press('back')
    sleep(delay)


def scroll(delay=DELAY_TIME):
    d.drag(0.5, 0.8, 0.5, 0.2)
    sleep(delay)


def send_keys(x, delay=DELAY_TIME):
    d.send_keys(x)
    sleep(delay)


# 阅读文章，阅读6个文章，每个130秒
def read_articles():
    # 切换到学习-订阅
    click(d(resourceId="cn.xuexi.android:id/home_bottom_tab_button_work"))
    click(
        d.xpath(
            '//*[@resource-id="cn.xuexi.android:id/view_pager"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
        ))
    click(d(text='订阅'))
    logger.info('已切换到学习-订阅')
    # 开始阅读文章
    logger.info('开始阅读文章')
    count = 0
    list = []
    while count < 6:
        for elem in d(className='android.widget.TextView'):
            title = elem.get_text()
            if len(title) < 12 or title in list:
                continue
            list.append(title)
            click(elem)
            if d(description='订阅').exists or d(description='已订阅').exists:  # 通过有无订阅键排除视频、专题和组图
                count = count + 1
                logger.info('正在阅读第 %d 篇文章: %s', count, title)
                scroll()
                if DEBUG:
                    sleep(2)
                else:
                    sleep(130)
            press_back()
            if count == 6:
                break
        scroll()  # 下滑读取更多
    logger.info('阅读文章结束')


# 观看视频，观看6个视频，每个15秒，再看17分钟新闻联播
def watch_video():
    # 切换到电视台-联播频道
    click(d(resourceId='cn.xuexi.android:id/home_bottom_tab_button_contact'))
    click(d(text='联播频道'))
    logger.info('已切换到电视台-联播频道')
    # 开始观看视频
    logger.info('开始观看视频')
    count = 0
    list = []
    while count < 6:
        for elem in d(className='android.widget.TextView'):
            title = elem.get_text()
            if len(title) < 12 or title in list:
                continue
            list.append(title)
            click(elem)
            count = count + 1
            logger.info('正在观看第 %d 个视频: %s', count, title)
            if DEBUG:
                sleep(2)
            else:
                sleep(15)
            press_back()
            if count == 6:
                break
        scroll()  # 下滑读取更多
    # 开始观看新闻联播
    logger.info('开始观看新闻联播')
    click(d(text='联播频道'))
    flag = True
    while flag:
        for elem in d(className='android.widget.TextView'):
            title = elem.get_text()
            if '《新闻联播》' in title:
                click(elem)
                logger.info('正在观看新闻联播: %s', title)
                if DEBUG:
                    sleep(2)
                else:
                    sleep(1020)
                press_back()
                flag = False
                break
        scroll()  # 下滑读取更多
    logger.info('观看视频结束')


# 在联播频道里收藏、转发、评论两个视频
def star_forward_comment():
    # 切换到电视台-联播频道
    click(d(resourceId='cn.xuexi.android:id/home_bottom_tab_button_contact'))
    click(d(text='联播频道'))
    logger.info('已切换到电视台-联播频道')
    # 读入评论库
    with open('redwords.json', 'r') as f:
        redwords = json.load(f)
    logger.info('读入评论库完毕，共计 %s 条评论', redwords['total'])
    # 开始收藏、转发、评论
    logger.info('开始收藏、转发、评论')
    count = 0
    for elem in d(className='android.widget.TextView'):
        title = elem.get_text()
        if len(title) < 12:
            continue
        click(elem)
        count = count + 1
        logger.info('正在收藏、转发、评论第 %d 个视频: %s', count, title)
        # 收藏
        click(
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
            ))
        # 转发 真机要修改
        click(
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]'
            ))
        click(d(text='分享到短信'))
        # 评论
        click(d(text='欢迎发表你的观点'))
        comment = random.choice(redwords['list'])['zuopinneirong']
        send_keys(comment)
        click(d(text='发布'))
        logger.info('已发布观点: %s',comment)
        # 返回
        press_back()
        if count == 2:
            break
    logger.info('收藏、转发、评论结束')


def use_local():
    # 切换到学习-xx（本地）
    click(d(resourceId="cn.xuexi.android:id/home_bottom_tab_button_work"))
    click(
        d.xpath(
            '//*[@resource-id="cn.xuexi.android:id/view_pager"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
        ))
    # 定位城市
    city_list = [
        '北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南',
        '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'
    ]
    for city in city_list:
        if d(text=city).exists:
            break
    if not d(text=city).exists:
        logger.error('找不到本地城市')
    click(d(text=city))
    logger.info('已切换到学习-%s', city)
    # 打开本地频道
    logger.info('开始打开本地频道')
    click(d(text=city + '学习平台'))
    press_back()
    logger.info('打开本地频道结束')


if __name__ == '__main__':
    # 连接设备
    logger.info('开始连接设备')
    d = u2.connect()
    # d = u2.connect('192.168.1.131')
    # d = u2.connect_usb('123456f')
    logger.info('设备已连接')

    # 打开学习强国
    logger.info('打开学习强国')
    d.app_start('cn.xuexi.android')
    d(resourceId='cn.xuexi.android:id/tvv_video_render').wait()
    d(resourceId='cn.xuexi.android:id/tvv_video_render').wait_gone()
    logger.info('学习强国已打开')

    # 开始刷分
    logger.info('开始学习')
    read_articles()
    watch_video()
    star_forward_comment()
    use_local()
    logger.info('学习结束')
