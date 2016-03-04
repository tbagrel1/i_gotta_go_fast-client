#ifndef SAPP1_H
#define SAPP1_H

#include <QMainWindow>

namespace Ui {
class sapp1;
}

class sapp1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit sapp1(QWidget *parent = 0);
    ~sapp1();

private:
    Ui::sapp1 *ui;
};

#endif // SAPP1_H
