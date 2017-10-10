import os

def main():
    base ='C:\\Users\\glliu\\bankHistory.v4.fullyBuild'

    files = listFiles(base)
    if files is None:
        print("\"",base, "\":","\t", "NOT existing")
        return  None

    for i in files:
        print(i,"=",files[i])

def listFiles(base): # 取得给定目录下所有目录和磁盘文件列表
    if(False == os.path.isdir(base)): # http://stackabuse.com/python-check-if-a-file-or-directory-exists/
        return None

    files = dict() # 使用dict以同时返回(不含路径在内的)文件名称(key)和含路径在内的完整名称(value)

    for filename in os.listdir(base):   # [csv.abc csv.bankcomm csv.bob csv.boc csv.ccb csv.ceb csv.cgb csv.cmb csv.fxcm csv.huilvwang csv.icbc csv.investing csv.netease csv.spdb csv.truefx]
        #print (filename, end=" ")
        files[filename]=base+"\\"+filename

    return  files

if __name__ == "__main__": main()