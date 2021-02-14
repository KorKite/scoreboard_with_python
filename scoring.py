import pandas as pd
from pymongo import MongoClient
from sklearn.metrics import accuracy_score
import time

class scoring:
    def __init__(self):
        self.answer = pd.read_csv("answer.csv")
        my_client = MongoClient("mongodb://localhost:27017/")
        self.db = my_client["scoring_test"]["rank"]

    def check_accuracy(self, array_list):
        return accuracy_score(self.answer, array_list)*100

    def check_ok(self, csv_file):
        if csv_file.shape == (150, 1):
            return True
        else:
            return False

    def write(self, csv_file, regis_name, uploaded_name, user_ip):
        file = pd.read_csv(csv_file).to_numpy()
        if self.check_ok(file):
            file = file.reshape(-1)
        else:
            return "CSV파일의 형식이 다릅니다. 문제에 맞는 정답을 제출해주세요."
        acc = self.check_accuracy(file)
        now = time.localtime()
        self.db.insert_one({
            "name":regis_name,
            "acc":round(acc, 2),
            "filename":uploaded_name,
            "user_ip": user_ip,
            "createdAt": "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        })
        return f"정상적으로 제출되었습니다. 정확도: {acc}, 등록된 이름: {regis_name}"
    
    def read_rank(self):
        rank = sorted(list(self.db.find()), key= (lambda x:x["acc"]), reverse=True)
        for i in range(len(rank)):
            rank[i]["rank"] = i+1
        return rank

if __name__ == "__main__":
    #TESTING CODE
    sc = scoring()
    print(sc.write("answer.csv", "hello"))