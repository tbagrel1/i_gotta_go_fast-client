#include "module.h"
#include "ui_module.h"

Module::Module(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Module)
{
    ui->setupUi(this);
}

Module::~Module()
{
    delete ui;
}
