#ifndef FENETREBVN_H
#define FENETREBVN_H

#include <QDialog>

namespace Ui {
class FenetreBVN;
}

class FenetreBVN : public QDialog
{
    Q_OBJECT

public:
    explicit FenetreBVN(QWidget *parent = 0);
    ~FenetreBVN();

private:
    Ui::FenetreBVN *ui;
};

#endif // FENETREBVN_H
