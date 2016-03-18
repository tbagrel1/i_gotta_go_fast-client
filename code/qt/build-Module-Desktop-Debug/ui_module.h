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
#include <QtGui/QFrame>
#include <QtGui/QGraphicsView>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QProgressBar>
#include <QtGui/QPushButton>
#include <QtGui/QScrollArea>
#include <QtGui/QTextEdit>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Module
{
public:
    QWidget *Frame;
    QFrame *SFrameAvancement;
    QLabel *LabelAvancement;
    QProgressBar *BarreAvancement;
    QFrame *SFrameTemps;
    QLabel *LabelStat;
    QLabel *LabelRestant;
    QLabel *LabelRestantV;
    QProgressBar *BarreReussite;
    QProgressBar *BarreErreurs;
    QLabel *LabelReussite;
    QLabel *LabelErreurs;
    QLabel *LabelSMots;
    QFrame *Sep1;
    QLabel *LabelSMotsV;
    QLabel *LabelScore;
    QLabel *LabelScoreV;
    QFrame *Sep2;
    QScrollArea *ScoresBox;
    QWidget *SScoresBox;
    QFrame *SFrameTaper;
    QTextEdit *TextBoxTaper;
    QLineEdit *EntryTaper;
    QGraphicsView *LabelLogo;
    QFrame *SFrameControle;
    QPushButton *BoutonStartPause;
    QPushButton *BoutonQuitter;
    QLabel *LabelInfo;
    QMenuBar *Menu;

    void setupUi(QMainWindow *Module)
    {
        if (Module->objectName().isEmpty())
            Module->setObjectName(QString::fromUtf8("Module"));
        Module->resize(1200, 600);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Module->sizePolicy().hasHeightForWidth());
        Module->setSizePolicy(sizePolicy);
        Module->setMinimumSize(QSize(1200, 600));
        Module->setMaximumSize(QSize(1200, 600));
        Frame = new QWidget(Module);
        Frame->setObjectName(QString::fromUtf8("Frame"));
        SFrameAvancement = new QFrame(Frame);
        SFrameAvancement->setObjectName(QString::fromUtf8("SFrameAvancement"));
        SFrameAvancement->setGeometry(QRect(20, 150, 281, 411));
        SFrameAvancement->setFrameShape(QFrame::StyledPanel);
        SFrameAvancement->setFrameShadow(QFrame::Raised);
        LabelAvancement = new QLabel(SFrameAvancement);
        LabelAvancement->setObjectName(QString::fromUtf8("LabelAvancement"));
        LabelAvancement->setGeometry(QRect(20, 20, 241, 21));
        QFont font;
        font.setPointSize(14);
        LabelAvancement->setFont(font);
        LabelAvancement->setAlignment(Qt::AlignCenter);
        BarreAvancement = new QProgressBar(SFrameAvancement);
        BarreAvancement->setObjectName(QString::fromUtf8("BarreAvancement"));
        BarreAvancement->setGeometry(QRect(60, 50, 161, 341));
        BarreAvancement->setValue(56);
        BarreAvancement->setTextVisible(false);
        BarreAvancement->setOrientation(Qt::Vertical);
        BarreAvancement->setTextDirection(QProgressBar::TopToBottom);
        SFrameTemps = new QFrame(Frame);
        SFrameTemps->setObjectName(QString::fromUtf8("SFrameTemps"));
        SFrameTemps->setGeometry(QRect(900, 150, 281, 411));
        SFrameTemps->setAutoFillBackground(false);
        SFrameTemps->setFrameShape(QFrame::StyledPanel);
        SFrameTemps->setFrameShadow(QFrame::Raised);
        LabelStat = new QLabel(SFrameTemps);
        LabelStat->setObjectName(QString::fromUtf8("LabelStat"));
        LabelStat->setGeometry(QRect(20, 140, 241, 21));
        LabelStat->setFont(font);
        LabelStat->setAlignment(Qt::AlignCenter);
        LabelRestant = new QLabel(SFrameTemps);
        LabelRestant->setObjectName(QString::fromUtf8("LabelRestant"));
        LabelRestant->setGeometry(QRect(10, 10, 261, 31));
        LabelRestant->setFont(font);
        LabelRestant->setAlignment(Qt::AlignCenter);
        LabelRestantV = new QLabel(SFrameTemps);
        LabelRestantV->setObjectName(QString::fromUtf8("LabelRestantV"));
        LabelRestantV->setGeometry(QRect(10, 50, 261, 81));
        QFont font1;
        font1.setPointSize(24);
        LabelRestantV->setFont(font1);
        LabelRestantV->setFrameShape(QFrame::StyledPanel);
        LabelRestantV->setAlignment(Qt::AlignCenter);
        BarreReussite = new QProgressBar(SFrameTemps);
        BarreReussite->setObjectName(QString::fromUtf8("BarreReussite"));
        BarreReussite->setGeometry(QRect(10, 170, 181, 21));
        BarreReussite->setAutoFillBackground(true);
        BarreReussite->setValue(75);
        BarreReussite->setTextVisible(false);
        BarreReussite->setInvertedAppearance(false);
        BarreErreurs = new QProgressBar(SFrameTemps);
        BarreErreurs->setObjectName(QString::fromUtf8("BarreErreurs"));
        BarreErreurs->setGeometry(QRect(10, 200, 181, 21));
        BarreErreurs->setAutoFillBackground(true);
        BarreErreurs->setValue(25);
        BarreErreurs->setTextVisible(false);
        BarreErreurs->setInvertedAppearance(true);
        LabelReussite = new QLabel(SFrameTemps);
        LabelReussite->setObjectName(QString::fromUtf8("LabelReussite"));
        LabelReussite->setGeometry(QRect(200, 170, 71, 21));
        QFont font2;
        font2.setPointSize(12);
        LabelReussite->setFont(font2);
        LabelReussite->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelErreurs = new QLabel(SFrameTemps);
        LabelErreurs->setObjectName(QString::fromUtf8("LabelErreurs"));
        LabelErreurs->setGeometry(QRect(200, 200, 71, 21));
        LabelErreurs->setFont(font2);
        LabelErreurs->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelSMots = new QLabel(SFrameTemps);
        LabelSMots->setObjectName(QString::fromUtf8("LabelSMots"));
        LabelSMots->setGeometry(QRect(200, 250, 71, 21));
        LabelSMots->setFont(font2);
        LabelSMots->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        Sep1 = new QFrame(SFrameTemps);
        Sep1->setObjectName(QString::fromUtf8("Sep1"));
        Sep1->setGeometry(QRect(10, 230, 261, 16));
        Sep1->setFrameShape(QFrame::HLine);
        Sep1->setFrameShadow(QFrame::Sunken);
        LabelSMotsV = new QLabel(SFrameTemps);
        LabelSMotsV->setObjectName(QString::fromUtf8("LabelSMotsV"));
        LabelSMotsV->setGeometry(QRect(20, 250, 151, 21));
        QFont font3;
        font3.setPointSize(16);
        LabelSMotsV->setFont(font3);
        LabelScore = new QLabel(SFrameTemps);
        LabelScore->setObjectName(QString::fromUtf8("LabelScore"));
        LabelScore->setGeometry(QRect(200, 280, 71, 21));
        LabelScore->setFont(font2);
        LabelScore->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelScoreV = new QLabel(SFrameTemps);
        LabelScoreV->setObjectName(QString::fromUtf8("LabelScoreV"));
        LabelScoreV->setGeometry(QRect(20, 280, 151, 21));
        LabelScoreV->setFont(font3);
        Sep2 = new QFrame(SFrameTemps);
        Sep2->setObjectName(QString::fromUtf8("Sep2"));
        Sep2->setGeometry(QRect(10, 310, 261, 20));
        Sep2->setFrameShape(QFrame::HLine);
        Sep2->setFrameShadow(QFrame::Sunken);
        ScoresBox = new QScrollArea(SFrameTemps);
        ScoresBox->setObjectName(QString::fromUtf8("ScoresBox"));
        ScoresBox->setGeometry(QRect(10, 330, 261, 71));
        ScoresBox->setWidgetResizable(true);
        SScoresBox = new QWidget();
        SScoresBox->setObjectName(QString::fromUtf8("SScoresBox"));
        SScoresBox->setGeometry(QRect(0, 0, 259, 69));
        ScoresBox->setWidget(SScoresBox);
        SFrameTaper = new QFrame(Frame);
        SFrameTaper->setObjectName(QString::fromUtf8("SFrameTaper"));
        SFrameTaper->setGeometry(QRect(320, 150, 561, 271));
        SFrameTaper->setFrameShape(QFrame::StyledPanel);
        SFrameTaper->setFrameShadow(QFrame::Raised);
        TextBoxTaper = new QTextEdit(SFrameTaper);
        TextBoxTaper->setObjectName(QString::fromUtf8("TextBoxTaper"));
        TextBoxTaper->setGeometry(QRect(20, 20, 521, 161));
        TextBoxTaper->setFont(font3);
        EntryTaper = new QLineEdit(SFrameTaper);
        EntryTaper->setObjectName(QString::fromUtf8("EntryTaper"));
        EntryTaper->setGeometry(QRect(80, 200, 401, 51));
        QFont font4;
        font4.setPointSize(18);
        EntryTaper->setFont(font4);
        EntryTaper->setAlignment(Qt::AlignCenter);
        LabelLogo = new QGraphicsView(Frame);
        LabelLogo->setObjectName(QString::fromUtf8("LabelLogo"));
        LabelLogo->setGeometry(QRect(20, 20, 1161, 111));
        SFrameControle = new QFrame(Frame);
        SFrameControle->setObjectName(QString::fromUtf8("SFrameControle"));
        SFrameControle->setGeometry(QRect(320, 440, 561, 121));
        SFrameControle->setFrameShape(QFrame::StyledPanel);
        SFrameControle->setFrameShadow(QFrame::Raised);
        BoutonStartPause = new QPushButton(SFrameControle);
        BoutonStartPause->setObjectName(QString::fromUtf8("BoutonStartPause"));
        BoutonStartPause->setGeometry(QRect(10, 60, 261, 51));
        BoutonStartPause->setFont(font3);
        BoutonQuitter = new QPushButton(SFrameControle);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(290, 60, 261, 51));
        BoutonQuitter->setFont(font3);
        LabelInfo = new QLabel(SFrameControle);
        LabelInfo->setObjectName(QString::fromUtf8("LabelInfo"));
        LabelInfo->setGeometry(QRect(10, 10, 541, 41));
        LabelInfo->setFont(font2);
        LabelInfo->setFrameShape(QFrame::StyledPanel);
        LabelInfo->setAlignment(Qt::AlignCenter);
        Module->setCentralWidget(Frame);
        Menu = new QMenuBar(Module);
        Menu->setObjectName(QString::fromUtf8("Menu"));
        Menu->setGeometry(QRect(0, 0, 1200, 20));
        Module->setMenuBar(Menu);

        retranslateUi(Module);
        QObject::connect(BoutonQuitter, SIGNAL(clicked()), Module, SLOT(close()));

        QMetaObject::connectSlotsByName(Module);
    } // setupUi

    void retranslateUi(QMainWindow *Module)
    {
        Module->setWindowTitle(QApplication::translate("Module", "Module", 0, QApplication::UnicodeUTF8));
        LabelAvancement->setText(QApplication::translate("Module", "Avancement", 0, QApplication::UnicodeUTF8));
        LabelStat->setText(QApplication::translate("Module", "Statistiques", 0, QApplication::UnicodeUTF8));
        LabelRestant->setText(QApplication::translate("Module", "Temps / Mots restants", 0, QApplication::UnicodeUTF8));
        LabelRestantV->setText(QApplication::translate("Module", "25 / 30", 0, QApplication::UnicodeUTF8));
        LabelReussite->setText(QApplication::translate("Module", "R\303\251ussite", 0, QApplication::UnicodeUTF8));
        LabelErreurs->setText(QApplication::translate("Module", "Erreurs", 0, QApplication::UnicodeUTF8));
        LabelSMots->setText(QApplication::translate("Module", "S / Mots", 0, QApplication::UnicodeUTF8));
        LabelSMotsV->setText(QApplication::translate("Module", "2,01", 0, QApplication::UnicodeUTF8));
        LabelScore->setText(QApplication::translate("Module", "Score", 0, QApplication::UnicodeUTF8));
        LabelScoreV->setText(QApplication::translate("Module", "TextLabel", 0, QApplication::UnicodeUTF8));
        TextBoxTaper->setHtml(QApplication::translate("Module", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte g\303\251n\303\251ral \303\240 <span style=\" color:#ff0000;\">taper</span> &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte g\303\251n\303\251ral \303\240 taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte g\303\251n\303\251ral \303\240 taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte g\303\251n\303\251ral \303\240 taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte g\303\251n\303\251ral \303\240 taper &gt;</p></body></html>", 0, QApplication::UnicodeUTF8));
        EntryTaper->setText(QApplication::translate("Module", "tap|er", 0, QApplication::UnicodeUTF8));
        BoutonStartPause->setText(QApplication::translate("Module", "Start / Pause", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Module", "Quitter", 0, QApplication::UnicodeUTF8));
        LabelInfo->setText(QApplication::translate("Module", "Ici des informations sur le programme", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Module: public Ui_Module {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MODULE_H
