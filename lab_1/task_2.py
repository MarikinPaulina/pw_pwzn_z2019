def task_2():
    task = '\n'
    for i in range(1,10):
        task += '* '*i if i < 6 else '* '*(10-i)
        task = task[:-1] + '\n'
    return task


assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
