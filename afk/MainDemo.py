import time
import yysOS
import yysKB


class yysOperator():
    def MainAccount(self):
        while True:
            yysKB.peassKey(yysOS.N1, yysOS.N7)
            time.sleep(3)


    def testdebug(self, i):
        yysKB.peassKey(yysOS.N1, yysOS.N7)
        print("dododo:" + str(i))
        time.sleep(3)


if __name__ == '__main__':
    exc = yysOperator()
    # exc.MainAccount()
    print('this is test!')
