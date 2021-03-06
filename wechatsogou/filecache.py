# -*- coding: utf-8 -*-

# from werkzeug.contrib.cache import FileSystemCache
from cachelib.file import FileSystemCache  # 查找werkzeug.contrib.cache已经无效,改为cachelib.file可用

class WechatCache(FileSystemCache):
    """基于文件的缓存

    """

    def __init__(self, cache_dir='/tmp/wechatsogou-cache', default_timeout=300):
        """初始化

        cache_dir是缓存目录
        """
        super(WechatCache, self).__init__(cache_dir, default_timeout)

    def get(self, key):
        try:
            return super(WechatCache, self).get(key)
        except ValueError:
            return None
