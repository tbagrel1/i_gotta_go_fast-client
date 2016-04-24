#include "fenetrebvn.h"
#include "ui_fenetrebvn.h"

FenetreBVN::FenetreBVN(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::FenetreBVN)
{
    ui->setupUi(this);
}

FenetreBVN::~FenetreBVN()
{
    delete ui;
}
