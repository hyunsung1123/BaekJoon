def solution(today, terms, privacies):
    answer = []
    today_year,today_month,today_day=map(int,today.split("."))
    for i in terms:
        key,months = i.split(" ")
        for index,j in enumerate(privacies):
            year,month,day = map(int,j[:10].split("."))
            
            if key==j[-1]:
                month=month+int(months)
                
                if month>12:
                    month_tmp=month%12
                    year_tmp=month//12
                    month=month_tmp
                    if month==0:
                        month = 12
                        year_tmp-=1
                    year += year_tmp
                    day -=1
                    if day<=0:
                        day=28-day
                        month-=1
                        if month <= 0:
                            month = 12 + month
                            year -=1
                else:
                    day -=1
                    if day<=0:
                        day=28-day
                        month-=1
                        if month <= 0:
                            month = 12 + month
                print(year,month,day)
                
                if today_year>year:
                    answer.append(index+1)
                    
                elif today_year == year:
                    
                    if today_month > month:
                        answer.append(index+1)
                        
                    elif today_month == month:
                        
                        if today_day > day:
                            answer.append(index+1)
    answer.sort()
    return answer