#include "sapp1.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    sapp1 w;
    w.show();

    return a.exec();
}
