#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน และแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชั่น 2 ฟังค์ชั้น
#cast / converting

#รับค่าข้อมูล
def moneyAndPeopleInput() :
    money = float(input("insert Money: "))
    people = int(input("insert People: "))
    return money, people

#คำนวณ แล้วแสดงผลออกมา
def moneyCalculate(money, people) :
    #เงินขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น
    doublefloatmoney = "%.2f" % money
    print(f"Money {money:.2f} บาท คน {(people)} คน แชร์กันคนละ {round(money/people)} บาท")
    print("Money", doublefloatmoney, "บาท คน", people, "คน แชร์กันคนละ", (round(money / people)), "บาท")
    print("Money " +  str("%.2f" % money) + " บาท คน " + str(people) + " คน แชร์กันคนละ " + str(round(money/people)) + " บาท ")
    print("Money {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท".format(money, people, round(money / people)))
    print("Money %s บาท คน %d คน แชร์กันคนละ %d บาท" %(doublefloatmoney, people , round(money / people)))


money, person = moneyAndPeopleInput()

moneyCalculate(money, person)