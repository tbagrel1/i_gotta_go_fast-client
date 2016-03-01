#ifndef SFENETRE1_H
#define SFENETRE1_H

#include <QDialog>

namespace Ui {
class sfenetre1;
}

class sfenetre1 : public QDialog
{
    Q_OBJECT

public:
    explicit sfenetre1(QWidget *parent = 0);
    ~sfenetre1();

private:
    Ui::sfenetre1 *ui;
};

#endif // SFENETRE1_H
