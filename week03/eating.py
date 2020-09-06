import threading
import random
import time

activity = []
mutex = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]

threads = []

class MyThread(threading.Thread):
    def __init__(self, n, mealCount): #n:线程标示号，mealCount:吃饭次数限定
        super().__init__() 
        self.n = n
        self.mealCount = mealCount

    def run(self):
        global activity
        eatCount = 0
        time.sleep(1)
        leftFork = self.n - 1 #左叉锁号
        rightFork = self.n % 5 #右叉锁号
        while eatCount < self.mealCount:
            if mutex[leftFork].acquire(1): #获取左叉子
                print(f'{self.n} get leftFork') 
                activity.append([self.n,1,1])
                if mutex[rightFork].acquire(1, random.randint(1,5)): #获取右叉，随机1-5秒超时，避免死锁
                    print(f'{self.n} get rightFork and eat,count: {eatCount}') #成功吃面
                    activity.append([self.n,2,3])
                    time.sleep(random.randint(1,3)) #随机1-3秒的吃面时间
                    eatCount += 1
                    mutex[rightFork].release() #释放右叉
                    activity.append([self.n,2,2])
                    print(f'{self.n} release rightFork')
                    time.sleep(random.randint(1,3)) #吃面结束，随机1-5秒的思考哲学问题时间
                else:
                    print(f'{self.n} cant get rightFork')
                mutex[leftFork].release() #释放左叉
                activity.append([self.n,1,2])
                print(f'{self.n} release leftFork')
            else:
                print(f'{self.n} cant get leftFork')

if __name__ == '__main__':
    mealCount = int(input("请输入就餐次数:"))
    if mealCount < 1 or mealCount > 60:
        print(f'【非法输入】就餐次数区间：1-60')
    for i in range(5):
        t = MyThread(i, mealCount)
        threads.append(t)
        t.start()
    for j in threads:
        j.join()

    print(activity)