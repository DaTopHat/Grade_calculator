no_changed_point_int = 0
new_point_int = 0
total_category_points = 0
total = 0
ui = 0


def summative():
    global total
    global total_category_points
    global new_point_int
    global no_changed_point_int
    if total_category_points != 0 and new_point_int != 0:
        new_point_total = new_point_int / total_category_points * 60
        total = new_point_total + no_changed_point_int
        total = round(total, 2)


def formative():
    global total
    global total_category_points
    global new_point_int
    global no_changed_point_int
    if total_category_points != 0 and new_point_int != 0:
        new_point_total = new_point_int / total_category_points * 40
        total = new_point_total + no_changed_point_int
        total = round(total, 2)


def timed():
    global ui
    global no_changed_point_int
    global new_point_int
    global total_category_points
    global total
    self = ui
    new_point_int = self.new_points.value()
    total_category_points = self.total_cat_points.value()
    no_changed_point_int = self.not_changed_points.value()
    if self.select_summative.isChecked():
        summative()
    if self.select_formative.isChecked():
        formative()
    self.output.setText(str(total))


def set_up(self):
    from PyQt5.QtCore import QTimer
    self.timer = QTimer()
    # noinspection PyUnresolvedReferences
    self.timer.timeout.connect(timed)
    self.timer.start(100)


def main():
    import window
    import sys
    global ui

    app = window.QtWidgets.QApplication(sys.argv)
    Dialog = window.QtWidgets.QDialog()
    ui = window.Ui_Grade_Calculator()
    ui.setupUi(Dialog)
    Dialog.show()
    # noinspection PyTypeChecker
    set_up(ui)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
