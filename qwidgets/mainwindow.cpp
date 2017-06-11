#include "mainwindow.h"
#include <QLabel>
#include <QVBoxLayout>

MainWindow::MainWindow(QWidget *parent) :
   QMainWindow(parent)
{
    QLabel *lb = new QLabel();
    lb->setPixmap(QPixmap(":/new/images/wtm3.png"));
    this->setCentralWidget(lb);
    this->setWindowTitle("QWidgets");
}
