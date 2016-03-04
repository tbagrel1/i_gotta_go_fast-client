#ifndef MODULE3_H
#define MODULE3_H

#include <QMainWindow>

namespace Ui {
class Module3;
}

class Module3 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Module3(QWidget *parent = 0);
    ~Module3();

private:
    Ui::Module3 *ui;
};

#endif // MODULE3_H
