/********************************************************************************
** Form generated from reading UI file 'module.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MODULE_H
#define UI_MODULE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QWidget>
#include "knuminput.h"

QT_BEGIN_NAMESPACE

class Ui_Module
{
public:
    QWidget *centralWidget;
    KDoubleNumInput *kdoublenuminput;
    QMenuBar *menuBar;

    void setupUi(QMainWindow *Module)
    {
        if (Module->objectName().isEmpty())
            Module->setObjectName(QString::fromUtf8("Module"));
        Module->resize(1200, 720);
        centralWidget = new QWidget(Module);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        kdoublenuminput = new KDoubleNumInput(centralWidget);
        kdoublenuminput->setObjectName(QString::fromUtf8("kdoublenuminput"));
        kdoublenuminput->setGeometry(QRect(330, 290, 81, 24));
        Module->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(Module);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1200, 20));
        Module->setMenuBar(menuBar);

        retranslateUi(Module);

        QMetaObject::connectSlotsByName(Module);
    } // setupUi

    void retranslateUi(QMainWindow *Module)
    {
        Module->setWindowTitle(QApplication::translate("Module", "Module", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Module: public Ui_Module {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MODULE_H
