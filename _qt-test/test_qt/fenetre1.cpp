#include "fenetre1.h"
#include "ui_fenetre1.h"

Fenetre1::Fenetre1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Fenetre1)
{
    ui->setupUi(this);
}

Fenetre1::~Fenetre1()
{
    delete ui;
}
