#ifndef MODULE2_H
#define MODULE2_H

#include <QMainWindow>

namespace Ui {
class Module2;
}

class Module2 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Module2(QWidget *parent = 0);
    ~Module2();

private:
    Ui::Module2 *ui;
};

#endif // MODULE2_H
