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
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Module
{
public:
    QWidget *Frame;
    QFrame *SFrameAvancement;
    QLabel *LabelAvancement;
    QProgressBar *BarreAvancement;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QFrame *line;
    QFrame *line_2;
    QFrame *line_3;
    QFrame *SFrameTemps;
    QLabel *LabelRestant;
    QLabel *LabelRestantV;
    QLabel *LabelSMots;
    QFrame *Sep1;
    QLabel *LabelSMotsV;
    QLabel *LabelScore;
    QLabel *LabelScoreV;
    QFrame *Sep2;
    QScrollArea *ScoresBox;
    QWidget *SScoresBox;
    QLabel *label_4;
    QLabel *label_7;
    QGraphicsView *LabelLogo;
    QFrame *SFrameControle;
    QPushButton *BoutonStartPause;
    QPushButton *BoutonQuitter;
    QLabel *LabelInfo;
    QLabel *label;
    QLabel *label_3;
    QLabel *label_2;
    QGraphicsView *graphicsView;
    QLineEdit *lineEdit;
    QLabel *label_5;
    QLabel *label_6;
    QFrame *frame;
    QLabel *LabelStat;
    QProgressBar *BarreReussite;
    QProgressBar *BarreErreurs;
    QLabel *LabelReussite;
    QLabel *LabelErreurs;
    QFrame *frame_2;
    QGraphicsView *graphicsView_2;
    QGraphicsView *graphicsView_3;
    QGraphicsView *graphicsView_4;
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
        LabelAvancement->setGeometry(QRect(20, 20, 111, 21));
        QFont font;
        font.setPointSize(12);
        LabelAvancement->setFont(font);
        LabelAvancement->setAlignment(Qt::AlignCenter);
        BarreAvancement = new QProgressBar(SFrameAvancement);
        BarreAvancement->setObjectName(QString::fromUtf8("BarreAvancement"));
        BarreAvancement->setGeometry(QRect(20, 50, 111, 341));
        BarreAvancement->setValue(50);
        BarreAvancement->setTextVisible(false);
        BarreAvancement->setOrientation(Qt::Vertical);
        BarreAvancement->setTextDirection(QProgressBar::TopToBottom);
        label_8 = new QLabel(SFrameAvancement);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(210, 30, 51, 41));
        label_8->setFont(font);
        label_8->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        label_9 = new QLabel(SFrameAvancement);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(210, 200, 51, 41));
        label_9->setFont(font);
        label_10 = new QLabel(SFrameAvancement);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(210, 370, 51, 41));
        label_10->setFont(font);
        line = new QFrame(SFrameAvancement);
        line->setObjectName(QString::fromUtf8("line"));
        line->setGeometry(QRect(140, 35, 61, 31));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(SFrameAvancement);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setGeometry(QRect(140, 210, 61, 21));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);
        line_3 = new QFrame(SFrameAvancement);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setGeometry(QRect(140, 380, 61, 21));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);
        SFrameTemps = new QFrame(Frame);
        SFrameTemps->setObjectName(QString::fromUtf8("SFrameTemps"));
        SFrameTemps->setGeometry(QRect(900, 150, 281, 411));
        SFrameTemps->setAutoFillBackground(false);
        SFrameTemps->setFrameShape(QFrame::StyledPanel);
        SFrameTemps->setFrameShadow(QFrame::Raised);
        LabelRestant = new QLabel(SFrameTemps);
        LabelRestant->setObjectName(QString::fromUtf8("LabelRestant"));
        LabelRestant->setGeometry(QRect(10, 10, 261, 31));
        QFont font1;
        font1.setPointSize(14);
        LabelRestant->setFont(font1);
        LabelRestant->setAlignment(Qt::AlignCenter);
        LabelRestantV = new QLabel(SFrameTemps);
        LabelRestantV->setObjectName(QString::fromUtf8("LabelRestantV"));
        LabelRestantV->setGeometry(QRect(10, 50, 261, 81));
        QFont font2;
        font2.setPointSize(24);
        LabelRestantV->setFont(font2);
        LabelRestantV->setFrameShape(QFrame::StyledPanel);
        LabelRestantV->setAlignment(Qt::AlignCenter);
        LabelSMots = new QLabel(SFrameTemps);
        LabelSMots->setObjectName(QString::fromUtf8("LabelSMots"));
        LabelSMots->setGeometry(QRect(190, 200, 71, 21));
        LabelSMots->setFont(font);
        LabelSMots->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        Sep1 = new QFrame(SFrameTemps);
        Sep1->setObjectName(QString::fromUtf8("Sep1"));
        Sep1->setGeometry(QRect(10, 140, 261, 16));
        Sep1->setFrameShape(QFrame::HLine);
        Sep1->setFrameShadow(QFrame::Sunken);
        LabelSMotsV = new QLabel(SFrameTemps);
        LabelSMotsV->setObjectName(QString::fromUtf8("LabelSMotsV"));
        LabelSMotsV->setGeometry(QRect(20, 200, 151, 21));
        QFont font3;
        font3.setPointSize(16);
        LabelSMotsV->setFont(font3);
        LabelScore = new QLabel(SFrameTemps);
        LabelScore->setObjectName(QString::fromUtf8("LabelScore"));
        LabelScore->setGeometry(QRect(190, 230, 71, 21));
        LabelScore->setFont(font);
        LabelScore->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelScoreV = new QLabel(SFrameTemps);
        LabelScoreV->setObjectName(QString::fromUtf8("LabelScoreV"));
        LabelScoreV->setGeometry(QRect(20, 230, 151, 21));
        LabelScoreV->setFont(font3);
        Sep2 = new QFrame(SFrameTemps);
        Sep2->setObjectName(QString::fromUtf8("Sep2"));
        Sep2->setGeometry(QRect(10, 260, 261, 20));
        Sep2->setFrameShape(QFrame::HLine);
        Sep2->setFrameShadow(QFrame::Sunken);
        ScoresBox = new QScrollArea(SFrameTemps);
        ScoresBox->setObjectName(QString::fromUtf8("ScoresBox"));
        ScoresBox->setGeometry(QRect(10, 310, 261, 91));
        ScoresBox->setWidgetResizable(true);
        SScoresBox = new QWidget();
        SScoresBox->setObjectName(QString::fromUtf8("SScoresBox"));
        SScoresBox->setGeometry(QRect(0, 0, 259, 89));
        ScoresBox->setWidget(SScoresBox);
        label_4 = new QLabel(SFrameTemps);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(10, 160, 261, 31));
        label_4->setFont(font1);
        label_4->setAlignment(Qt::AlignCenter);
        label_7 = new QLabel(SFrameTemps);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(10, 280, 261, 21));
        label_7->setFont(font1);
        label_7->setAlignment(Qt::AlignCenter);
        LabelLogo = new QGraphicsView(Frame);
        LabelLogo->setObjectName(QString::fromUtf8("LabelLogo"));
        LabelLogo->setGeometry(QRect(20, 20, 1161, 111));
        LabelLogo->setFrameShape(QFrame::NoFrame);
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
        LabelInfo->setFont(font);
        LabelInfo->setFrameShape(QFrame::StyledPanel);
        LabelInfo->setAlignment(Qt::AlignCenter);
        label = new QLabel(Frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(50, 50, 531, 51));
        QFont font4;
        font4.setFamily(QString::fromUtf8("Monospace"));
        font4.setPointSize(30);
        label->setFont(font4);
        label->setFrameShape(QFrame::StyledPanel);
        label->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label->setIndent(0);
        label_3 = new QLabel(Frame);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(620, 50, 531, 51));
        label_3->setFont(font4);
        label_3->setFrameShape(QFrame::StyledPanel);
        label_3->setMargin(0);
        label_3->setIndent(0);
        label_2 = new QLabel(Frame);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(580, 50, 41, 51));
        label_2->setFont(font4);
        label_2->setFrameShape(QFrame::WinPanel);
        label_2->setAlignment(Qt::AlignCenter);
        graphicsView = new QGraphicsView(Frame);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setGeometry(QRect(320, 130, 561, 81));
        graphicsView->setFrameShape(QFrame::NoFrame);
        lineEdit = new QLineEdit(Frame);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(580, 130, 41, 51));
        lineEdit->setFont(font4);
        lineEdit->setAlignment(Qt::AlignCenter);
        label_5 = new QLabel(Frame);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(350, 130, 231, 51));
        label_5->setFont(font4);
        label_5->setFrameShape(QFrame::StyledPanel);
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_5->setIndent(0);
        label_6 = new QLabel(Frame);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(620, 130, 231, 51));
        QFont font5;
        font5.setPointSize(30);
        font5.setBold(true);
        font5.setItalic(false);
        font5.setWeight(75);
        label_6->setFont(font5);
        label_6->setFrameShape(QFrame::NoFrame);
        label_6->setAlignment(Qt::AlignCenter);
        label_6->setIndent(0);
        frame = new QFrame(Frame);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(320, 290, 561, 131));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        LabelStat = new QLabel(frame);
        LabelStat->setObjectName(QString::fromUtf8("LabelStat"));
        LabelStat->setGeometry(QRect(160, 10, 241, 21));
        LabelStat->setFont(font1);
        LabelStat->setAlignment(Qt::AlignCenter);
        BarreReussite = new QProgressBar(frame);
        BarreReussite->setObjectName(QString::fromUtf8("BarreReussite"));
        BarreReussite->setGeometry(QRect(20, 40, 411, 31));
        BarreReussite->setAutoFillBackground(true);
        BarreReussite->setValue(75);
        BarreReussite->setTextVisible(false);
        BarreReussite->setInvertedAppearance(false);
        BarreErreurs = new QProgressBar(frame);
        BarreErreurs->setObjectName(QString::fromUtf8("BarreErreurs"));
        BarreErreurs->setGeometry(QRect(20, 80, 411, 31));
        BarreErreurs->setAutoFillBackground(true);
        BarreErreurs->setValue(25);
        BarreErreurs->setTextVisible(false);
        BarreErreurs->setInvertedAppearance(true);
        LabelReussite = new QLabel(frame);
        LabelReussite->setObjectName(QString::fromUtf8("LabelReussite"));
        LabelReussite->setGeometry(QRect(450, 40, 91, 31));
        LabelReussite->setFont(font1);
        LabelReussite->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        LabelErreurs = new QLabel(frame);
        LabelErreurs->setObjectName(QString::fromUtf8("LabelErreurs"));
        LabelErreurs->setGeometry(QRect(450, 80, 91, 31));
        LabelErreurs->setFont(font1);
        LabelErreurs->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        frame_2 = new QFrame(Frame);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setGeometry(QRect(320, 230, 561, 41));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        graphicsView_2 = new QGraphicsView(frame_2);
        graphicsView_2->setObjectName(QString::fromUtf8("graphicsView_2"));
        graphicsView_2->setGeometry(QRect(0, 0, 187, 41));
        graphicsView_3 = new QGraphicsView(frame_2);
        graphicsView_3->setObjectName(QString::fromUtf8("graphicsView_3"));
        graphicsView_3->setGeometry(QRect(187, 0, 187, 41));
        graphicsView_4 = new QGraphicsView(frame_2);
        graphicsView_4->setObjectName(QString::fromUtf8("graphicsView_4"));
        graphicsView_4->setGeometry(QRect(374, 0, 187, 41));
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
        label_8->setText(QApplication::translate("Module", "100 %", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("Module", "50 %", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("Module", "0 %", 0, QApplication::UnicodeUTF8));
        LabelRestant->setText(QApplication::translate("Module", "Temps ou Mots restants", 0, QApplication::UnicodeUTF8));
        LabelRestantV->setText(QApplication::translate("Module", "25 / 30", 0, QApplication::UnicodeUTF8));
        LabelSMots->setText(QApplication::translate("Module", "s / Mots", 0, QApplication::UnicodeUTF8));
        LabelSMotsV->setText(QApplication::translate("Module", "2,01", 0, QApplication::UnicodeUTF8));
        LabelScore->setText(QApplication::translate("Module", "Score", 0, QApplication::UnicodeUTF8));
        LabelScoreV->setText(QApplication::translate("Module", "1281", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("Module", "Scores", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("Module", "Meilleurs scores", 0, QApplication::UnicodeUTF8));
        BoutonStartPause->setText(QApplication::translate("Module", "Start / Pause", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Module", "Quitter", 0, QApplication::UnicodeUTF8));
        LabelInfo->setText(QApplication::translate("Module", "Ici des informations sur le programme", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Module", "L\303\251o l", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("Module", " cerf court dans la for\303\252t", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("Module", "e", 0, QApplication::UnicodeUTF8));
        lineEdit->setText(QString());
        label_5->setText(QApplication::translate("Module", "L\303\251o l", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        label_6->setToolTip(QApplication::translate("Module", "<html><head/><body><p>Il faut que l'on fasse clignoter ce label si le caract\303\250re est juste ou faux</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_6->setText(QApplication::translate("Module", "    <<<", 0, QApplication::UnicodeUTF8));
        LabelStat->setText(QApplication::translate("Module", "Statistiques", 0, QApplication::UnicodeUTF8));
        LabelReussite->setText(QApplication::translate("Module", "R\303\251ussite", 0, QApplication::UnicodeUTF8));
        LabelErreurs->setText(QApplication::translate("Module", "Erreurs", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        graphicsView_3->setToolTip(QApplication::translate("Module", "<html><head/><body><p>Pour afficher des m\303\251dailles / \303\251toiles en fonction de la performance</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
    } // retranslateUi

};

namespace Ui {
    class Module: public Ui_Module {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MODULE_H
