#include "score.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Score w;
    w.show();

    return a.exec();
}
