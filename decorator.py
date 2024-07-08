def singleton(cls):
    instances = {}
    def getinstance(*arg, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*arg, **kwargs)  # 确保 cls() 被调用以创建实例
        return instances[cls]
    return getinstance
