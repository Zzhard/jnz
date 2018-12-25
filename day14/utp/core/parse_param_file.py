from conf.setting import DATA_PATH
import os
def textFileToList(file,seq=','):
    file=os.path.join(DATA_PATH,file)
    print(file)
    case_data = []
    with open(file,encoding='utf-8') as f:
        for line in f:
            new_line = line.strip()
            if new_line:
                case_data.append(new_line.split(seq))
    return case_data

def excelToList(file):
    #你需要补的
    case_data = []
    return case_data



#自动化测试

#测试开发、