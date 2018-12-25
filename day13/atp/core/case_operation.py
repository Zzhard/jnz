import xlrd
from core.my_requests import MyRequest
def get_case(path):
    '''
    :param path: excel测试用例
    :return: 二维数组，每一个里面是一条测试用例
    '''
    all_case = []
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        row_data = sheet.row_values(i)[4:8]
        all_case.append(row_data)
    #[[url,get,data,check],[url,get,data,check]]
    return all_case

def send_request(url,method,data,headers=None):
    req = MyRequest(url,data,headers=headers)
    if method.upper()=="POST":
        res = req.post()
    elif method.upper() =='GET':
        res = req.get()
    else:
        res = {"data":"暂时不支持该方法！"}
    return res['data']


