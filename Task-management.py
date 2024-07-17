#name

task=[]
vulgar_words=['fuck', 'beat', 'bitch', 'asshole', 'poor']


while True:
    todo_list=input('Enter your Todo List Here: ').lower()
    
    if todo_list == '':
      print('No empty Task is allowed...')
      continue

    if todo_list.isnumeric():
      print('Task should not be a number...')
      continue

    if todo_list in vulgar_words:
      print('task should not be a vulgar word...........')
      continue
      
    if todo_list == 'exit':
      print(f'Tasks added: {task}')
      break

    task.append(todo_list)
    print(f'Tasks added: {task}')



