#include "sfenetre1.h"
#include "ui_sfenetre1.h"

sfenetre1::sfenetre1(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::sfenetre1)
{
    ui->setupUi(this);
}

sfenetre1::~sfenetre1()
{
    delete ui;
}
