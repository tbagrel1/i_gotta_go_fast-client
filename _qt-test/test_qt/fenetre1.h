#ifndef FENETRE1_H
#define FENETRE1_H

#include <QMainWindow>

namespace Ui {
class Fenetre1;
}

class Fenetre1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Fenetre1(QWidget *parent = 0);
    ~Fenetre1();

private:
    Ui::Fenetre1 *ui;
};

#endif // FENETRE1_H
