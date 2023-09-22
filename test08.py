#เขียนโปรเเกรม รับชื่อ อายุ ทางเเป้นพิมพ์ เเล้วเเสดงผลออกมาว่า ชื่อ อายุนั้รเป็น เด็ก คนหนุ่ม หรือคนเเก่
# อายุน้อยกว่า ๅค คือ เด็ก /อายุ 19 - 45 คนหนุ่ม/ 46 ขึ้น คือคนเเก่

#หาฟีเจอร์การทำงาน เพื่อจะเอาไปเขียนเป็นฟังชั่น
#ฟีเจอร์ รับค่าข้อมูล , ตรวจสอบเเละเเสดงผลว่า เป็นเด็ก คนหนุ่ม หรือคนเเก่ , เเสดงชื่อโปรเเกรม

def showProgramName() :
    print('**--โปรเเเกรมตรวจสอบความเป็นเด็ก หนุ่ม แก่--*')

def inputData( ) :
    name =input('ป้อนชื่อ : ')
    age = int( input('ป้อนอายุ : '))
    return name, age

def checkShowstatus(name, age) :
    if age <= 18 :
        print(f'คุณ{name} อายุ {age} ปี เป็นเด็ก')
    elif age >= 19 and age <= 45 :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนหนุ่ม')
    else :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนแก่')

print('------------------')
showProgramName()
print('------------------')
name,age = inputData()
checkShowstatus(name,age)
print('------------------')