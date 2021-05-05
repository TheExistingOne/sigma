from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from sigma.taskloader import parse_task


def load_sample(layout):
    config = parse_task('sample.yaml')
    layout.addWidget(QLabel('Task: ' + config.get("name")))
    layout.addWidget(QLabel('Description: ' + config.get("notification-body")))
    layout.addWidget(QLabel('Reminder: ' + str(config.get("notify"))))
    layout.addWidget(
        QLabel('Date: ' + str(config.get("day")).zfill(2) + "/" + str(config.get("month")).zfill(2) + "/" + str(config.get("year")).zfill(2)))
    layout.addWidget(QLabel('At: ' + str(config.get("hour")).zfill(2) + ":" + str(config.get("minute")).zfill(2)))


if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()

    layout = QVBoxLayout()
    load_sample(layout)

    window.setLayout(layout)
    window.show()

    app.exec_()
