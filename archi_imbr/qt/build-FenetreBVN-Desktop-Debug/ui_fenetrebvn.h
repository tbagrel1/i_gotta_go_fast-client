/********************************************************************************
** Form generated from reading UI file 'fenetrebvn.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FENETREBVN_H
#define UI_FENETREBVN_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QGraphicsView>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_FenetreBVN
{
public:
    QGraphicsView *LabelIcone;
    QLabel *LabelDescription;
    QLabel *LabelCredits;
    QPushButton *BoutonQuitter;
    QPushButton *BoutonContinuer;

    void setupUi(QDialog *FenetreBVN)
    {
        if (FenetreBVN->objectName().isEmpty())
            FenetreBVN->setObjectName(QString::fromUtf8("FenetreBVN"));
        FenetreBVN->resize(600, 300);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(FenetreBVN->sizePolicy().hasHeightForWidth());
        FenetreBVN->setSizePolicy(sizePolicy);
        FenetreBVN->setMinimumSize(QSize(600, 300));
        FenetreBVN->setMaximumSize(QSize(600, 300));
        LabelIcone = new QGraphicsView(FenetreBVN);
        LabelIcone->setObjectName(QString::fromUtf8("LabelIcone"));
        LabelIcone->setGeometry(QRect(20, 20, 561, 91));
        LabelDescription = new QLabel(FenetreBVN);
        LabelDescription->setObjectName(QString::fromUtf8("LabelDescription"));
        LabelDescription->setGeometry(QRect(20, 120, 561, 51));
        QFont font;
        font.setPointSize(11);
        font.setBold(true);
        font.setWeight(75);
        LabelDescription->setFont(font);
        LabelDescription->setAlignment(Qt::AlignCenter);
        LabelDescription->setWordWrap(true);
        LabelCredits = new QLabel(FenetreBVN);
        LabelCredits->setObjectName(QString::fromUtf8("LabelCredits"));
        LabelCredits->setGeometry(QRect(20, 249, 561, 31));
        QFont font1;
        font1.setPointSize(10);
        font1.setBold(false);
        font1.setWeight(50);
        LabelCredits->setFont(font1);
        LabelCredits->setAlignment(Qt::AlignCenter);
        BoutonQuitter = new QPushButton(FenetreBVN);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(20, 190, 271, 41));
        QFont font2;
        font2.setPointSize(15);
        BoutonQuitter->setFont(font2);
        BoutonContinuer = new QPushButton(FenetreBVN);
        BoutonContinuer->setObjectName(QString::fromUtf8("BoutonContinuer"));
        BoutonContinuer->setGeometry(QRect(310, 190, 271, 41));
        BoutonContinuer->setFont(font2);

        retranslateUi(FenetreBVN);

        QMetaObject::connectSlotsByName(FenetreBVN);
    } // setupUi

    void retranslateUi(QDialog *FenetreBVN)
    {
        FenetreBVN->setWindowTitle(QApplication::translate("FenetreBVN", "FenetreBVN", 0, QApplication::UnicodeUTF8));
        LabelDescription->setText(QApplication::translate("FenetreBVN", "Ce petit logiciel a pour but de vous aider \303\240 taper plus vite au clavier, en particulier les mots les plus utilis\303\251s de la langue Fran\303\247aise", 0, QApplication::UnicodeUTF8));
        LabelCredits->setText(QApplication::translate("FenetreBVN", "- Thomas BAGREL, Julien ROMARY - Version V1.0.0 - 04/03/2016 -\n"
"tomsb07@gmail.com", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("FenetreBVN", "Quitter", 0, QApplication::UnicodeUTF8));
        BoutonContinuer->setText(QApplication::translate("FenetreBVN", "Continuer", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class FenetreBVN: public Ui_FenetreBVN {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FENETREBVN_H
