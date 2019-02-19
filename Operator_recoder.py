import datetime
def cal_op(op):
    if op == '1': return 'SS'
    if op == '2': return 'RO'
    if op == '3': return 'TO'
    if op == '4': return 'EO'

print('파일 레코딩 시작')
while True:
    operator = cal_op(input('누가?:SS = 1, RO = 2, TO = 3, EO = 4'))
    save_time = datetime.datetime.now()
    cont = input('내용:')

    print('{}\t{}\t{}'.format(save_time, operator, cont))

    # call excel
    with open('Save_DB.txt', 'a') as f:
        f.write('{}\t\t{}\t{}\n'.format(save_time, operator, cont))