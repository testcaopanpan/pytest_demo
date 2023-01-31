import pytest
import os,time

if __name__=="__main__":
    pytest.main()
    time.sleep(5)
    os.system("allure generate ./temps -o ./reports --clean")#执行将temps路径下的所有本次的json文件生成allure形象报告存储到reports路径下，