#include "sapp1.h"
#include "ui_sapp1.h"

sapp1::sapp1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::sapp1)
{
    ui->setupUi(this);
}

sapp1::~sapp1()
{
    delete ui;
}
