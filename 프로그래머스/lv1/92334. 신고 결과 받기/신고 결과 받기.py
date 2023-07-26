#신고받은 횟수 누적 딕셔너리 declare_id_dic
#메일을 받을 횟수 누적 딕셔너리 get_mail_id_dic를 만듬.
def solution(id_list, report, k):
    declare_id_dic = {i : 0 for i in id_list}
    get_mail_id_dic = {i : 0 for i in id_list}
    get_mali_list=[]
    #중복은 1개로 취급하니 set사용.
    report = set(report)
    #각 id별 신고받은 횟수를 누적한다.
    for i in report:
        user_id,declare_id=i.split(" ")
        declare_id_dic[declare_id] +=1 #신고횟수 누적
    #누적받은 신고횟수와 k를 비교해 k보다 클때의 i 값 즉 id값을 tmp에 넣어준다.
    for i in declare_id_dic:
        if declare_id_dic.get(i) >= k:
            get_mali_list.append(i)
    #신고한 id가 tmp에 있는 경우 메일을 받아야하므로 get_mail_id_dic의 value를 1증가시킴.
    for i in report:
        user_id,declare_id=i.split(" ")
        if declare_id in get_mali_list:
            get_mail_id_dic[user_id]+=1
    return list(get_mail_id_dic.values())