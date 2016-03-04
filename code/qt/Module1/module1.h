#ifndef MODULE1_H
#define MODULE1_H

#include <QMainWindow>

namespace Ui {
class Module1;
}

class Module1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Module1(QWidget *parent = 0);
    ~Module1();

private:
    Ui::Module1 *ui;
};

#endif // MODULE1_H
