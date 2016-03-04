#include "module3.h"
#include "ui_module3.h"

Module3::Module3(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Module3)
{
    ui->setupUi(this);
}

Module3::~Module3()
{
    delete ui;
}
