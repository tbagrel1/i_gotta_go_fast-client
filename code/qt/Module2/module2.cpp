#include "module2.h"
#include "ui_module2.h"

Module2::Module2(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Module2)
{
    ui->setupUi(this);
}

Module2::~Module2()
{
    delete ui;
}
