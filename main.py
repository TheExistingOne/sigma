from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from sigma.taskloader import parse_tasks

tasks = parse_tasks()
task_index = 0

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()

    window_layout = QHBoxLayout()
    button_layout = QVBoxLayout()
    text_layout = QVBoxLayout()

    task = QLabel("")
    desc = QLabel("")
    remind = QLabel("")
    date = QLabel("")
    time = QLabel("")


    def load_sample(config):
        task.setText('Task: ' + config.get("name"))
        desc.setText('Description: ' + config.get("notification-body"))
        remind.setText('Reminder: ' + str(config.get("notify")))
        date.setText('Date: ' + str(config.get("day")).zfill(2) + "/" + str(config.get("month")).zfill(2) + "/" +
                     str(config.get("year")).zfill(2))
        time.setText('At: ' + str(config.get("hour")).zfill(2) + ":" + str(config.get("minute")).zfill(2))

    def init_taskwidget(layout):
        layout.addWidget(task)
        layout.addWidget(desc)
        layout.addWidget(remind)
        layout.addWidget(date)
        layout.addWidget(time)

    def increment_task_pointer():
        global task_index
        if task_index < len(tasks) - 1:
            task_index += 1
        else:
            task_index = 0
        load_sample(tasks[task_index])


    def decrement_task_pointer():
        global task_index
        if task_index == 0:
            task_index = len(tasks) - 1
        else:
            task_index -= 1
        load_sample(tasks[task_index])


    load_sample(tasks[task_index])
    init_taskwidget(text_layout)
    window_layout.addLayout(text_layout)

    next_button = QPushButton("Next")
    previous_button = QPushButton("Previous")

    next_button.clicked.connect(increment_task_pointer)
    previous_button.clicked.connect(decrement_task_pointer)

    button_layout.addWidget(next_button)
    button_layout.addWidget(previous_button)
    window_layout.addLayout(button_layout)

    window.setLayout(window_layout)
    window.show()

    app.exec_()
