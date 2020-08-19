f = open('list.csv', 'w', encoding='UTF-8-sig') #encoding='UTF-8-sig' : 맥북 엑셀 한글깨짐 오류 해결

colors = ['빨강', '주황', '노랑', '초록']
fruits = ['사과', '오렌지', '바나나', '라임']

for i in range(len(colors)):
    f.write(colors[i] + ',' + fruits[i] + '\n')

f.close()