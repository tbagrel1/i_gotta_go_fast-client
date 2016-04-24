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
    QWidget *Fenetre;
    QFrame *SFrameAvancement;
    QLabel *LabelAvancementT;
    QProgressBar *BarreAvancement;
    QLabel *Label100;
    QLabel *Label50;
    QLabel *Label0;
    QFrame *Ligne100;
    QFrame *Ligne50;
    QFrame *Ligne0;
    QFrame *SFrameTemps;
    QLabel *LabelRestantT;
    QLabel *LabelRestantV;
    QLabel *LabelSMots;
    QFrame *LigneRestant2Scores;
    QLabel *LabelSMotsV;
    QLabel *LabelScore;
    QLabel *LabelScoreV;
    QFrame *LigneScores2Best;
    QScrollArea *ScoresBox;
    QWidget *SScoresBox;
    QLabel *LabelScoreT;
    QLabel *LabelBestT;
    QGraphicsView *SFrame1Saisie;
    QFrame *SFrameControle;
    QPushButton *BoutonStartPause;
    QPushButton *BoutonQuitter;
    QLabel *LabelInfo;
    QLabel *LabelTexteDroite;
    QLabel *LabelTexteGauche;
    QLabel *LabelTexteCentre;
    QGraphicsView *SFrame2Saisie;
    QLineEdit *EntryTapeCentre;
    QLabel *LabelTapeDroit;
    QLabel *LabelTapeFleche;
    QFrame *SFenetreStat;
    QLabel *LabelStatT;
    QProgressBar *BarreReussite;
    QProgressBar *BarreErreurs;
    QLabel *LabelReussite;
    QLabel *LabelErreurs;
    QFrame *SFenetreEtoiles;
    QGraphicsView *Etoile1;
    QGraphicsView *Etoile2;
    QGraphicsView *Etoile3;
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
        Fenetre = new QWidget(Module);
        Fenetre->setObjectName(QString::fromUtf8("Fenetre"));
        SFrameAvancement = new QFrame(Fenetre);
        SFrameAvancement->setObjectName(QString::fromUtf8("SFrameAvancement"));
        SFrameAvancement->setGeometry(QRect(20, 150, 281, 411));
        SFrameAvancement->setFrameShape(QFrame::StyledPanel);
        SFrameAvancement->setFrameShadow(QFrame::Raised);
        LabelAvancementT = new QLabel(SFrameAvancement);
        LabelAvancementT->setObjectName(QString::fromUtf8("LabelAvancementT"));
        LabelAvancementT->setGeometry(QRect(20, 20, 111, 21));
        QFont font;
        font.setPointSize(12);
        LabelAvancementT->setFont(font);
        LabelAvancementT->setAlignment(Qt::AlignCenter);
        BarreAvancement = new QProgressBar(SFrameAvancement);
        BarreAvancement->setObjectName(QString::fromUtf8("BarreAvancement"));
        BarreAvancement->setGeometry(QRect(20, 50, 111, 341));
        BarreAvancement->setValue(68);
        BarreAvancement->setTextVisible(false);
        BarreAvancement->setOrientation(Qt::Vertical);
        BarreAvancement->setTextDirection(QProgressBar::TopToBottom);
        Label100 = new QLabel(SFrameAvancement);
        Label100->setObjectName(QString::fromUtf8("Label100"));
        Label100->setGeometry(QRect(210, 30, 51, 41));
        Label100->setFont(font);
        Label100->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        Label50 = new QLabel(SFrameAvancement);
        Label50->setObjectName(QString::fromUtf8("Label50"));
        Label50->setGeometry(QRect(210, 200, 51, 41));
        Label50->setFont(font);
        Label0 = new QLabel(SFrameAvancement);
        Label0->setObjectName(QString::fromUtf8("Label0"));
        Label0->setGeometry(QRect(210, 370, 51, 41));
        Label0->setFont(font);
        Ligne100 = new QFrame(SFrameAvancement);
        Ligne100->setObjectName(QString::fromUtf8("Ligne100"));
        Ligne100->setGeometry(QRect(140, 35, 61, 31));
        Ligne100->setFrameShape(QFrame::HLine);
        Ligne100->setFrameShadow(QFrame::Sunken);
        Ligne50 = new QFrame(SFrameAvancement);
        Ligne50->setObjectName(QString::fromUtf8("Ligne50"));
        Ligne50->setGeometry(QRect(140, 210, 61, 21));
        Ligne50->setFrameShape(QFrame::HLine);
        Ligne50->setFrameShadow(QFrame::Sunken);
        Ligne0 = new QFrame(SFrameAvancement);
        Ligne0->setObjectName(QString::fromUtf8("Ligne0"));
        Ligne0->setGeometry(QRect(140, 380, 61, 21));
        Ligne0->setFrameShape(QFrame::HLine);
        Ligne0->setFrameShadow(QFrame::Sunken);
        SFrameTemps = new QFrame(Fenetre);
        SFrameTemps->setObjectName(QString::fromUtf8("SFrameTemps"));
        SFrameTemps->setGeometry(QRect(900, 150, 281, 411));
        SFrameTemps->setAutoFillBackground(false);
        SFrameTemps->setFrameShape(QFrame::StyledPanel);
        SFrameTemps->setFrameShadow(QFrame::Raised);
        LabelRestantT = new QLabel(SFrameTemps);
        LabelRestantT->setObjectName(QString::fromUtf8("LabelRestantT"));
        LabelRestantT->setGeometry(QRect(10, 10, 261, 31));
        QFont font1;
        font1.setPointSize(14);
        LabelRestantT->setFont(font1);
        LabelRestantT->setAlignment(Qt::AlignCenter);
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
        LigneRestant2Scores = new QFrame(SFrameTemps);
        LigneRestant2Scores->setObjectName(QString::fromUtf8("LigneRestant2Scores"));
        LigneRestant2Scores->setGeometry(QRect(10, 140, 261, 16));
        LigneRestant2Scores->setFrameShape(QFrame::HLine);
        LigneRestant2Scores->setFrameShadow(QFrame::Sunken);
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
        LigneScores2Best = new QFrame(SFrameTemps);
        LigneScores2Best->setObjectName(QString::fromUtf8("LigneScores2Best"));
        LigneScores2Best->setGeometry(QRect(10, 260, 261, 20));
        LigneScores2Best->setFrameShape(QFrame::HLine);
        LigneScores2Best->setFrameShadow(QFrame::Sunken);
        ScoresBox = new QScrollArea(SFrameTemps);
        ScoresBox->setObjectName(QString::fromUtf8("ScoresBox"));
        ScoresBox->setGeometry(QRect(10, 310, 261, 91));
        ScoresBox->setWidgetResizable(true);
        SScoresBox = new QWidget();
        SScoresBox->setObjectName(QString::fromUtf8("SScoresBox"));
        SScoresBox->setGeometry(QRect(0, 0, 259, 89));
        ScoresBox->setWidget(SScoresBox);
        LabelScoreT = new QLabel(SFrameTemps);
        LabelScoreT->setObjectName(QString::fromUtf8("LabelScoreT"));
        LabelScoreT->setGeometry(QRect(10, 160, 261, 31));
        LabelScoreT->setFont(font1);
        LabelScoreT->setAlignment(Qt::AlignCenter);
        LabelBestT = new QLabel(SFrameTemps);
        LabelBestT->setObjectName(QString::fromUtf8("LabelBestT"));
        LabelBestT->setGeometry(QRect(10, 280, 261, 21));
        LabelBestT->setFont(font1);
        LabelBestT->setAlignment(Qt::AlignCenter);
        SFrame1Saisie = new QGraphicsView(Fenetre);
        SFrame1Saisie->setObjectName(QString::fromUtf8("SFrame1Saisie"));
        SFrame1Saisie->setGeometry(QRect(20, 20, 1161, 111));
        SFrame1Saisie->setFrameShape(QFrame::NoFrame);
        SFrameControle = new QFrame(Fenetre);
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
        LabelTexteDroite = new QLabel(Fenetre);
        LabelTexteDroite->setObjectName(QString::fromUtf8("LabelTexteDroite"));
        LabelTexteDroite->setGeometry(QRect(50, 50, 531, 51));
        QFont font4;
        font4.setFamily(QString::fromUtf8("Monospace"));
        font4.setPointSize(30);
        LabelTexteDroite->setFont(font4);
        LabelTexteDroite->setFrameShape(QFrame::StyledPanel);
        LabelTexteDroite->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelTexteDroite->setIndent(0);
        LabelTexteGauche = new QLabel(Fenetre);
        LabelTexteGauche->setObjectName(QString::fromUtf8("LabelTexteGauche"));
        LabelTexteGauche->setGeometry(QRect(620, 50, 531, 51));
        LabelTexteGauche->setFont(font4);
        LabelTexteGauche->setFrameShape(QFrame::StyledPanel);
        LabelTexteGauche->setMargin(0);
        LabelTexteGauche->setIndent(0);
        LabelTexteCentre = new QLabel(Fenetre);
        LabelTexteCentre->setObjectName(QString::fromUtf8("LabelTexteCentre"));
        LabelTexteCentre->setGeometry(QRect(580, 50, 41, 51));
        LabelTexteCentre->setFont(font4);
        LabelTexteCentre->setFrameShape(QFrame::WinPanel);
        LabelTexteCentre->setAlignment(Qt::AlignCenter);
        SFrame2Saisie = new QGraphicsView(Fenetre);
        SFrame2Saisie->setObjectName(QString::fromUtf8("SFrame2Saisie"));
        SFrame2Saisie->setGeometry(QRect(320, 130, 561, 81));
        SFrame2Saisie->setFrameShape(QFrame::NoFrame);
        EntryTapeCentre = new QLineEdit(Fenetre);
        EntryTapeCentre->setObjectName(QString::fromUtf8("EntryTapeCentre"));
        EntryTapeCentre->setGeometry(QRect(580, 130, 41, 51));
        EntryTapeCentre->setFont(font4);
        EntryTapeCentre->setAlignment(Qt::AlignCenter);
        LabelTapeDroit = new QLabel(Fenetre);
        LabelTapeDroit->setObjectName(QString::fromUtf8("LabelTapeDroit"));
        LabelTapeDroit->setGeometry(QRect(350, 130, 231, 51));
        LabelTapeDroit->setFont(font4);
        LabelTapeDroit->setFrameShape(QFrame::StyledPanel);
        LabelTapeDroit->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        LabelTapeDroit->setIndent(0);
        LabelTapeFleche = new QLabel(Fenetre);
        LabelTapeFleche->setObjectName(QString::fromUtf8("LabelTapeFleche"));
        LabelTapeFleche->setGeometry(QRect(620, 130, 231, 51));
        QFont font5;
        font5.setPointSize(30);
        font5.setBold(true);
        font5.setItalic(false);
        font5.setWeight(75);
        LabelTapeFleche->setFont(font5);
        LabelTapeFleche->setFrameShape(QFrame::NoFrame);
        LabelTapeFleche->setAlignment(Qt::AlignCenter);
        LabelTapeFleche->setIndent(0);
        SFenetreStat = new QFrame(Fenetre);
        SFenetreStat->setObjectName(QString::fromUtf8("SFenetreStat"));
        SFenetreStat->setGeometry(QRect(320, 290, 561, 131));
        SFenetreStat->setFrameShape(QFrame::StyledPanel);
        SFenetreStat->setFrameShadow(QFrame::Raised);
        LabelStatT = new QLabel(SFenetreStat);
        LabelStatT->setObjectName(QString::fromUtf8("LabelStatT"));
        LabelStatT->setGeometry(QRect(160, 10, 241, 21));
        LabelStatT->setFont(font1);
        LabelStatT->setAlignment(Qt::AlignCenter);
        BarreReussite = new QProgressBar(SFenetreStat);
        BarreReussite->setObjectName(QString::fromUtf8("BarreReussite"));
        BarreReussite->setGeometry(QRect(20, 40, 411, 31));
        BarreReussite->setAutoFillBackground(true);
        BarreReussite->setValue(75);
        BarreReussite->setTextVisible(false);
        BarreReussite->setInvertedAppearance(false);
        BarreErreurs = new QProgressBar(SFenetreStat);
        BarreErreurs->setObjectName(QString::fromUtf8("BarreErreurs"));
        BarreErreurs->setGeometry(QRect(20, 80, 411, 31));
        BarreErreurs->setAutoFillBackground(true);
        BarreErreurs->setValue(25);
        BarreErreurs->setTextVisible(false);
        BarreErreurs->setInvertedAppearance(true);
        LabelReussite = new QLabel(SFenetreStat);
        LabelReussite->setObjectName(QString::fromUtf8("LabelReussite"));
        LabelReussite->setGeometry(QRect(450, 40, 91, 31));
        LabelReussite->setFont(font1);
        LabelReussite->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        LabelErreurs = new QLabel(SFenetreStat);
        LabelErreurs->setObjectName(QString::fromUtf8("LabelErreurs"));
        LabelErreurs->setGeometry(QRect(450, 80, 91, 31));
        LabelErreurs->setFont(font1);
        LabelErreurs->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        SFenetreEtoiles = new QFrame(Fenetre);
        SFenetreEtoiles->setObjectName(QString::fromUtf8("SFenetreEtoiles"));
        SFenetreEtoiles->setGeometry(QRect(320, 230, 561, 41));
        SFenetreEtoiles->setFrameShape(QFrame::StyledPanel);
        SFenetreEtoiles->setFrameShadow(QFrame::Raised);
        Etoile1 = new QGraphicsView(SFenetreEtoiles);
        Etoile1->setObjectName(QString::fromUtf8("Etoile1"));
        Etoile1->setGeometry(QRect(0, 0, 187, 41));
        Etoile2 = new QGraphicsView(SFenetreEtoiles);
        Etoile2->setObjectName(QString::fromUtf8("Etoile2"));
        Etoile2->setGeometry(QRect(187, 0, 187, 41));
        Etoile3 = new QGraphicsView(SFenetreEtoiles);
        Etoile3->setObjectName(QString::fromUtf8("Etoile3"));
        Etoile3->setGeometry(QRect(374, 0, 187, 41));
        Module->setCentralWidget(Fenetre);
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
        LabelAvancementT->setText(QApplication::translate("Module", "Avancement", 0, QApplication::UnicodeUTF8));
        Label100->setText(QApplication::translate("Module", "100 %", 0, QApplication::UnicodeUTF8));
        Label50->setText(QApplication::translate("Module", "50 %", 0, QApplication::UnicodeUTF8));
        Label0->setText(QApplication::translate("Module", "0 %", 0, QApplication::UnicodeUTF8));
        LabelRestantT->setText(QApplication::translate("Module", "Temps ou Mots restants", 0, QApplication::UnicodeUTF8));
        LabelRestantV->setText(QApplication::translate("Module", "25 / 30", 0, QApplication::UnicodeUTF8));
        LabelSMots->setText(QApplication::translate("Module", "s / Mots", 0, QApplication::UnicodeUTF8));
        LabelSMotsV->setText(QApplication::translate("Module", "2,01", 0, QApplication::UnicodeUTF8));
        LabelScore->setText(QApplication::translate("Module", "Score", 0, QApplication::UnicodeUTF8));
        LabelScoreV->setText(QApplication::translate("Module", "1281", 0, QApplication::UnicodeUTF8));
        LabelScoreT->setText(QApplication::translate("Module", "Scores", 0, QApplication::UnicodeUTF8));
        LabelBestT->setText(QApplication::translate("Module", "Meilleurs scores", 0, QApplication::UnicodeUTF8));
        BoutonStartPause->setText(QApplication::translate("Module", "Start / Pause", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Module", "Quitter", 0, QApplication::UnicodeUTF8));
        LabelInfo->setText(QApplication::translate("Module", "Ici des informations sur le programme", 0, QApplication::UnicodeUTF8));
        LabelTexteDroite->setText(QApplication::translate("Module", "L\303\251o l", 0, QApplication::UnicodeUTF8));
        LabelTexteGauche->setText(QApplication::translate("Module", " cerf court dans la for\303\252t", 0, QApplication::UnicodeUTF8));
        LabelTexteCentre->setText(QApplication::translate("Module", "e", 0, QApplication::UnicodeUTF8));
        EntryTapeCentre->setText(QString());
        LabelTapeDroit->setText(QApplication::translate("Module", "L\303\251o l", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        LabelTapeFleche->setToolTip(QApplication::translate("Module", "<html><head/><body><p>Il faut que l'on fasse clignoter ce label si le caract\303\250re est juste ou faux</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        LabelTapeFleche->setText(QApplication::translate("Module", "    <<<", 0, QApplication::UnicodeUTF8));
        LabelStatT->setText(QApplication::translate("Module", "Statistiques", 0, QApplication::UnicodeUTF8));
        LabelReussite->setText(QApplication::translate("Module", "R\303\251ussite", 0, QApplication::UnicodeUTF8));
        LabelErreurs->setText(QApplication::translate("Module", "Erreurs", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        Etoile2->setToolTip(QApplication::translate("Module", "<html><head/><body><p>Pour afficher des m\303\251dailles / \303\251toiles en fonction de la performance</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
    } // retranslateUi

};

namespace Ui {
    class Module: public Ui_Module {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MODULE_H
