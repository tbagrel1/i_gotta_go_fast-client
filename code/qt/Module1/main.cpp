#include "module1.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Module1 w;
    w.show();

    return a.exec();
}
