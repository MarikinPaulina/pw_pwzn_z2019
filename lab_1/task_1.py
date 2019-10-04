def task_1():
    task = '\n'
    for i in range(1,10):
        task += f'{str(i)*i}\n'
    return task


assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
