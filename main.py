from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from sigma.taskloader import parse_tasks

# Load tasks from /tasks into array
tasks = parse_tasks()
task_index = 0

if __name__ == '__main__':
    # Creating main app window
    app = QApplication([])
    window = QWidget()

    # Defining layouts
    window_layout = QHBoxLayout()
    button_layout = QVBoxLayout()
    text_layout = QVBoxLayout()
    
    # creating variables to store text
    task = QLabel("")
    desc = QLabel("")
    remind = QLabel("")
    date = QLabel("")
    time = QLabel("")


    def load_sample(config):
        # When passed a config, parse it to sane text that can be displayed to the user
        # and write that text to the QLabels initialized earlier
        task.setText('Task: ' + config.get("name"))
        desc.setText('Description: ' + config.get("notification-body"))
        remind.setText('Reminder: ' + str(config.get("notify")))
        date.setText('Date: ' + str(config.get("day")).zfill(2) + "/" + str(config.get("month")).zfill(2) + "/" +
                     str(config.get("year")).zfill(2))
        time.setText('At: ' + str(config.get("hour")).zfill(2) + ":" + str(config.get("minute")).zfill(2))

    def init_taskwidget(layout):
        # Load the widgets into a provided layout
        layout.addWidget(task)
        layout.addWidget(desc)
        layout.addWidget(remind)
        layout.addWidget(date)
        layout.addWidget(time)

    def increment_task_pointer():
        # Increase task index and reset to 0 if about to overflow
        global task_index
        if task_index < len(tasks) - 1:
            task_index += 1
        else:
            task_index = 0
        load_sample(tasks[task_index])


    def decrement_task_pointer():
        # Decrease task pointer and reset to zero if about to go negative
        global task_index
        if task_index == 0:
            task_index = len(tasks) - 1
        else:
            task_index -= 1
        load_sample(tasks[task_index])

    # Initializng the text and adding to the correct layout
    load_sample(tasks[task_index])
    init_taskwidget(text_layout)
    window_layout.addLayout(text_layout)
    
    # Initializing and connecting the buttons
    next_button = QPushButton("Next")
    previous_button = QPushButton("Previous")
    next_button.clicked.connect(increment_task_pointer)
    previous_button.clicked.connect(decrement_task_pointer)
    
    # Adding buttons to corresponding layout
    button_layout.addWidget(next_button)
    button_layout.addWidget(previous_button)
    window_layout.addLayout(button_layout)
    
    #Create and run the window    
    window.setLayout(window_layout)
    window.show()
    app.exec_()
