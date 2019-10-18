# python脚本中发送http请求
# http请求封装在模块中
import requests

class HTTP:
    # classmethod类方法,用到类的变量
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful标准,返回结果json格式
        # return_json控制是否返回原生json格式或处理后的格式
        # 根据状态码判断返回是否是正常的文本
        if r.status_code != 200:
            return {} if return_json else ''
        # 特例处理方法,简化代码
        return r.json() if return_json else r.text