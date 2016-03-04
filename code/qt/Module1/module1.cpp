#include "module1.h"
#include "ui_module1.h"

Module1::Module1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Module1)
{
    ui->setupUi(this);
}

Module1::~Module1()
{
    delete ui;
}
