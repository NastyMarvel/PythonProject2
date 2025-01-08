class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __repr__(self):
        return f'Task({self.description}, {self.due_date}, {"Done" if self.is_done else "Not done"})'


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, index):
        try:
            self.tasks[index].mark_as_done()
        except IndexError:
            print(f'Задача с индексом {index} не найдена.')

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.is_done]

    def display_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if len(current_tasks) == 0:
            print('Нет текущих задач.')
        else:
            for i, task in enumerate(current_tasks):
                print(f'{i + 1}. {task}')


# Использование кода
if __name__ == "__main__":
    # Создание менеджера задач
    manager = TaskManager()

    # Добавление нескольких задач
    manager.add_task(Task("Сделать домашнюю работу", "10-12-2023"))
    manager.add_task(Task("Пойти в магазин", "11-12-2023"))
    manager.add_task(Task("Позвонить маме", "09-12-2023"))

    # Отметка одной из задач как выполненной
    manager.mark_task_as_done(0)

    # Вывод текущих задач
    manager.display_current_tasks()
