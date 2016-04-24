#ifndef MODULE_H
#define MODULE_H

#include <QMainWindow>

namespace Ui {
class Module;
}

class Module : public QMainWindow
{
    Q_OBJECT

public:
    explicit Module(QWidget *parent = 0);
    ~Module();

private:
    Ui::Module *ui;
};

#endif // MODULE_H
