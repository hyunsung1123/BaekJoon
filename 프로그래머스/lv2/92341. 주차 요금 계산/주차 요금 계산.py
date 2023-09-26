import math
def solution(fees, records):
    answer = []
    time_dict = {} #출차에 관한 시간을 담을 딕셔너리.
    fee_dict = {} #주차비용을 담을 딕셔너리,
    #fees에 관한 변수 설정. 각각 기본 시간/기본 요금/ 단위 시간/ 단위 요금 에 해당
    standard_time,standard_charge,unit_time,unit_charge = fees[0],fees[1],fees[2],fees[3]
    # IN/OUT 에 관한 정보를 보고 fee_dict에 각 자동차의 누적 주차 시간 저장.(분 단위로)
    for i in records:
        time,car_number,state = i.split(" ")
        hour,minute = time.split(":")
        if state == "IN":
            time_dict[car_number] = int(hour)*60 + int(minute)
        if state == "OUT":
            if car_number in fee_dict:
                fee_dict[car_number] += ((int(hour)*60 + int(minute)) - time_dict[car_number])
            else:
                fee_dict[car_number] = (int(hour)*60 + int(minute)) - time_dict[car_number]
            del(time_dict[car_number])  #fee_dict에 추가했으므로 time_dict에서는 해당 차량에 관한 정보 초기화 해주는 작업.
    # 출차 기록이 없는 차에 대한 요금 산정
    for i in time_dict:
        if i not in fee_dict:
            fee_dict[i] = (1439 - time_dict[i])
        else:
            fee_dict[i] += (1439- time_dict[i])
    # key 즉 자동차번호에 오름차순 정렬 후 요금 규칙에 맞게 요금 산정
    for car_number, time in sorted(fee_dict.items()):
        if standard_time >= time:
            fee = standard_charge
        else:
            fee = standard_charge + math.ceil((time-standard_time)/unit_time) * unit_charge
        answer.append(fee)
    return answer