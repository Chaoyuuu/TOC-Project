import requests
from bs4 import BeautifulSoup
#department_list = ["E8", "E2", "F7"]

# class find(object):
# 	"""docstring for find"""
# 	def __init__(self, arg):
# 		super(find, self).__init__()
# 		self.arg = arg

def course_url(name, num):
    find_list = []
    print(name + num)
    tmp = name + num
    urll = "http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no=" + name
    re2 = requests.get(urll)
    re2.encoding = 'utf8'
    soup2 = BeautifulSoup(re2.text, 'html.parser')
        #print(soup2)
    print("-----------------------")

    course1 = soup2.find_all('td')
    i = 0
    for tag in range(1,len(course1)):
        i = i+1
        
        if (i%24 == 2) and (course1[tag].text == num):
            # print("你搜尋的課程是: F7" + course1[tag].text)
            # print("classname: " + course1[tag + 8].text)
            # print("time: " + course1[tag + 14].text)
            # print("課程連結: " + course1[tag + 8].find("a").get("href") )
            find_list.append("你搜尋的課程是: ")
            find_list.append(tmp+'/ ' + course1[tag + 8].text + '/ ' + course1[tag + 14].text + '\n')
            if course1[tag+13].text != '額滿':
            	find_list.append("!!還有餘額!! (" + course1[tag +13].text + ")")
            else:
            	find_list.append("已經額滿了喔")
            find_list.append("\n課程連結: " + course1[tag + 8].find("a").get("href"))

        # elif int(course1[tag].text) < 30:
        # 	print("hiii")
        	# break
    
    print('\n'.join(find_list))
    if len(find_list)==0:
    	return "沒有這堂課喔~"  
    else: 
    	return '\n'.join(find_list)
   
def find_classroom(date, time):
	classroom_list = ["4201  一般教室(60人)", "4202  一般教室(60人)", "4203  階梯教室(108人)", "4204  階梯教室(92人)", "no", "4215  視聽教室(9人)", "4217 圖書室(12人)", "4260 一般教室(30人)", "4261 一般教室(60人)", "4263 一般教室(110人)", "4264 一般教室(130人)","65104新大樓研討室(70人)", "65105新大樓研討室(70人)", "65203電腦教室(70人)", "65304電腦教室(120人)", "65504新大樓研討室(16人)","65605新大樓研討室(20人)", "65705新大樓研討室(13人)", "65805新大樓研討室(15人)", "65905新大樓研討室(12人)", "65A13新大樓研討室(17人)","65405階梯教室(125人)", "65404電腦教室"]
	classroom_time = []
	empty_room = []
	test = []

	urll = "http://www.csie.ncku.edu.tw/Class2014/class/2018/" + date
	re2 = requests.get(urll)
	re2.encoding = 'utf8'
	soup2 = BeautifulSoup(re2.text, 'html.parser')
	# print(soup2)
	# print("-----------------------")
	c1 = soup2.find_all("tr")
	# print(c1)
	target_time = time.split('-')
	target_time1 = int(target_time[0]) #14
	target_time2 = int(target_time[1]) #14
	target_range = target_time2 - target_time1 + 1

	for i in range(0, target_range):
		classroom_time.append(target_time1+i)


	for i in range(2, len(c1)):    #all
		c2 = c1[i].find_all("td", {"class":"class_inner no_event "})
		# print(c2)
		count = target_range
		for j in range(0, len(c2)):  #every room
			tmp = c2[j].get("name").split(';')			
			for k in range(0, len(classroom_time)):
				if int(tmp[0]) == classroom_time[k]:
					count = count - 1
					

		if count == 0 and i!=0 and i!=1 and i!=6:
			test.append(i-2)
			empty_room.append(classroom_list[i-2])
			
	print('\n'.join(empty_room))

	if len(empty_room)==0:
		return "你查詢的日期/時段: " + date + " ["+ time +"]\n" + "很抱歉>< 沒有空教室ㄌ"
	else:
		tmp = "這些教室可以使用!!!\n" + "日期/時段: " + date + "  ["+ time +"]\n" + "----------------------\n"
		return tmp + '\n'.join(empty_room) #+ "\n\n" + "教室連結:" + "http://www.csie.ncku.edu.tw/Class2014/class/2018/" + date
	

    
