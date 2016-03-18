/********************************************************************************
** Form generated from reading UI file 'menu.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MENU_H
#define UI_MENU_H

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
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QTabWidget>
#include <QtGui/QTextEdit>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Menu
{
public:
    QAction *actionImprimer_scores;
    QAction *actionPoubelle_Ctrl_Q;
    QAction *actionPouet_OMFG;
    QAction *actionTruc_FTG;
    QAction *MenuFichierQuitter;
    QAction *MenuFichierParDefaut;
    QAction *MenuAideOuvrirAide;
    QAction *MenuAideOuvrirCredits;
    QWidget *ZoneCentrale;
    QGraphicsView *LabelIcone;
    QLabel *LabelChoisissez;
    QFrame *FrameModeJeu;
    QLabel *LabelMode;
    QTabWidget *TabMode;
    QWidget *TabTempsLimite;
    QLabel *LabelTempsLimite;
    QLineEdit *EntryTempsLimite;
    QWidget *TabMotLimite;
    QLabel *LabelMotLimite;
    QLineEdit *EntryMotLimite;
    QFrame *FrameModeCorrection;
    QLabel *LabelCorrection;
    QRadioButton *CorrManuValJuste;
    QRadioButton *CorrManuValAll;
    QRadioButton *CorrAuto;
    QFrame *FrameSource;
    QLabel *LabelSource;
    QTabWidget *TabSource;
    QWidget *TabMotsFR;
    QLabel *LabelMotsFR;
    QLineEdit *EntryMotsFR;
    QWidget *TabActu;
    QLineEdit *EntryActu;
    QLabel *LabelActu;
    QWidget *TabPerso;
    QLabel *LabelPerso;
    QTextEdit *EntryPerso;
    QFrame *FrameControles;
    QLabel *LabelLancez;
    QPushButton *BoutonCommencer;
    QPushButton *BoutonQuitter;
    QPushButton *BoutonAide;
    QLineEdit *EntryParam;
    QPushButton *BoutonGenererParam;
    QPushButton *BoutonAppliquerParam;
    QMenuBar *BarreMenu;
    QMenu *MenuFichier;
    QMenu *MenuAide;

    void setupUi(QMainWindow *Menu)
    {
        if (Menu->objectName().isEmpty())
            Menu->setObjectName(QString::fromUtf8("Menu"));
        Menu->resize(1000, 600);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Menu->sizePolicy().hasHeightForWidth());
        Menu->setSizePolicy(sizePolicy);
        Menu->setMinimumSize(QSize(1000, 600));
        Menu->setMaximumSize(QSize(1000, 600));
        actionImprimer_scores = new QAction(Menu);
        actionImprimer_scores->setObjectName(QString::fromUtf8("actionImprimer_scores"));
        actionPoubelle_Ctrl_Q = new QAction(Menu);
        actionPoubelle_Ctrl_Q->setObjectName(QString::fromUtf8("actionPoubelle_Ctrl_Q"));
        actionPouet_OMFG = new QAction(Menu);
        actionPouet_OMFG->setObjectName(QString::fromUtf8("actionPouet_OMFG"));
        actionTruc_FTG = new QAction(Menu);
        actionTruc_FTG->setObjectName(QString::fromUtf8("actionTruc_FTG"));
        MenuFichierQuitter = new QAction(Menu);
        MenuFichierQuitter->setObjectName(QString::fromUtf8("MenuFichierQuitter"));
        MenuFichierParDefaut = new QAction(Menu);
        MenuFichierParDefaut->setObjectName(QString::fromUtf8("MenuFichierParDefaut"));
        MenuAideOuvrirAide = new QAction(Menu);
        MenuAideOuvrirAide->setObjectName(QString::fromUtf8("MenuAideOuvrirAide"));
        MenuAideOuvrirCredits = new QAction(Menu);
        MenuAideOuvrirCredits->setObjectName(QString::fromUtf8("MenuAideOuvrirCredits"));
        ZoneCentrale = new QWidget(Menu);
        ZoneCentrale->setObjectName(QString::fromUtf8("ZoneCentrale"));
        LabelIcone = new QGraphicsView(ZoneCentrale);
        LabelIcone->setObjectName(QString::fromUtf8("LabelIcone"));
        LabelIcone->setGeometry(QRect(40, 40, 921, 101));
        LabelChoisissez = new QLabel(ZoneCentrale);
        LabelChoisissez->setObjectName(QString::fromUtf8("LabelChoisissez"));
        LabelChoisissez->setGeometry(QRect(280, 160, 441, 31));
        QFont font;
        font.setPointSize(20);
        LabelChoisissez->setFont(font);
        LabelChoisissez->setAlignment(Qt::AlignCenter);
        FrameModeJeu = new QFrame(ZoneCentrale);
        FrameModeJeu->setObjectName(QString::fromUtf8("FrameModeJeu"));
        FrameModeJeu->setGeometry(QRect(40, 210, 451, 151));
        FrameModeJeu->setFrameShape(QFrame::StyledPanel);
        FrameModeJeu->setFrameShadow(QFrame::Plain);
        LabelMode = new QLabel(FrameModeJeu);
        LabelMode->setObjectName(QString::fromUtf8("LabelMode"));
        LabelMode->setGeometry(QRect(20, 20, 411, 16));
        QFont font1;
        font1.setPointSize(12);
        LabelMode->setFont(font1);
        TabMode = new QTabWidget(FrameModeJeu);
        TabMode->setObjectName(QString::fromUtf8("TabMode"));
        TabMode->setGeometry(QRect(20, 50, 411, 81));
        TabMode->setFont(font1);
        TabMode->setTabShape(QTabWidget::Rounded);
        TabMode->setDocumentMode(false);
        TabMode->setTabsClosable(false);
        TabMode->setMovable(false);
        TabTempsLimite = new QWidget();
        TabTempsLimite->setObjectName(QString::fromUtf8("TabTempsLimite"));
        LabelTempsLimite = new QLabel(TabTempsLimite);
        LabelTempsLimite->setObjectName(QString::fromUtf8("LabelTempsLimite"));
        LabelTempsLimite->setGeometry(QRect(10, 10, 221, 31));
        QFont font2;
        font2.setPointSize(14);
        LabelTempsLimite->setFont(font2);
        EntryTempsLimite = new QLineEdit(TabTempsLimite);
        EntryTempsLimite->setObjectName(QString::fromUtf8("EntryTempsLimite"));
        EntryTempsLimite->setGeometry(QRect(240, 10, 151, 31));
        TabMode->addTab(TabTempsLimite, QString());
        TabMotLimite = new QWidget();
        TabMotLimite->setObjectName(QString::fromUtf8("TabMotLimite"));
        LabelMotLimite = new QLabel(TabMotLimite);
        LabelMotLimite->setObjectName(QString::fromUtf8("LabelMotLimite"));
        LabelMotLimite->setGeometry(QRect(10, 10, 221, 31));
        LabelMotLimite->setFont(font2);
        EntryMotLimite = new QLineEdit(TabMotLimite);
        EntryMotLimite->setObjectName(QString::fromUtf8("EntryMotLimite"));
        EntryMotLimite->setGeometry(QRect(240, 10, 151, 31));
        TabMode->addTab(TabMotLimite, QString());
        FrameModeCorrection = new QFrame(ZoneCentrale);
        FrameModeCorrection->setObjectName(QString::fromUtf8("FrameModeCorrection"));
        FrameModeCorrection->setGeometry(QRect(40, 380, 451, 151));
        FrameModeCorrection->setFrameShape(QFrame::StyledPanel);
        FrameModeCorrection->setFrameShadow(QFrame::Raised);
        LabelCorrection = new QLabel(FrameModeCorrection);
        LabelCorrection->setObjectName(QString::fromUtf8("LabelCorrection"));
        LabelCorrection->setGeometry(QRect(20, 20, 411, 16));
        LabelCorrection->setFont(font1);
        CorrManuValJuste = new QRadioButton(FrameModeCorrection);
        CorrManuValJuste->setObjectName(QString::fromUtf8("CorrManuValJuste"));
        CorrManuValJuste->setGeometry(QRect(10, 50, 421, 21));
        QFont font3;
        font3.setPointSize(10);
        font3.setBold(true);
        font3.setWeight(75);
        CorrManuValJuste->setFont(font3);
        CorrManuValAll = new QRadioButton(FrameModeCorrection);
        CorrManuValAll->setObjectName(QString::fromUtf8("CorrManuValAll"));
        CorrManuValAll->setGeometry(QRect(10, 80, 411, 21));
        CorrManuValAll->setFont(font3);
        CorrAuto = new QRadioButton(FrameModeCorrection);
        CorrAuto->setObjectName(QString::fromUtf8("CorrAuto"));
        CorrAuto->setGeometry(QRect(10, 110, 411, 21));
        CorrAuto->setFont(font3);
        FrameSource = new QFrame(ZoneCentrale);
        FrameSource->setObjectName(QString::fromUtf8("FrameSource"));
        FrameSource->setGeometry(QRect(510, 210, 451, 151));
        FrameSource->setFrameShape(QFrame::StyledPanel);
        FrameSource->setFrameShadow(QFrame::Raised);
        LabelSource = new QLabel(FrameSource);
        LabelSource->setObjectName(QString::fromUtf8("LabelSource"));
        LabelSource->setGeometry(QRect(20, 20, 411, 16));
        LabelSource->setFont(font1);
        TabSource = new QTabWidget(FrameSource);
        TabSource->setObjectName(QString::fromUtf8("TabSource"));
        TabSource->setGeometry(QRect(20, 50, 411, 81));
        QFont font4;
        font4.setPointSize(11);
        TabSource->setFont(font4);
        TabMotsFR = new QWidget();
        TabMotsFR->setObjectName(QString::fromUtf8("TabMotsFR"));
        LabelMotsFR = new QLabel(TabMotsFR);
        LabelMotsFR->setObjectName(QString::fromUtf8("LabelMotsFR"));
        LabelMotsFR->setGeometry(QRect(10, 10, 151, 31));
        LabelMotsFR->setWordWrap(true);
        EntryMotsFR = new QLineEdit(TabMotsFR);
        EntryMotsFR->setObjectName(QString::fromUtf8("EntryMotsFR"));
        EntryMotsFR->setGeometry(QRect(160, 10, 231, 31));
        TabSource->addTab(TabMotsFR, QString());
        TabActu = new QWidget();
        TabActu->setObjectName(QString::fromUtf8("TabActu"));
        EntryActu = new QLineEdit(TabActu);
        EntryActu->setObjectName(QString::fromUtf8("EntryActu"));
        EntryActu->setGeometry(QRect(160, 10, 231, 31));
        LabelActu = new QLabel(TabActu);
        LabelActu->setObjectName(QString::fromUtf8("LabelActu"));
        LabelActu->setGeometry(QRect(10, 10, 151, 31));
        LabelActu->setWordWrap(true);
        TabSource->addTab(TabActu, QString());
        TabPerso = new QWidget();
        TabPerso->setObjectName(QString::fromUtf8("TabPerso"));
        LabelPerso = new QLabel(TabPerso);
        LabelPerso->setObjectName(QString::fromUtf8("LabelPerso"));
        LabelPerso->setGeometry(QRect(10, 10, 151, 31));
        LabelPerso->setWordWrap(true);
        EntryPerso = new QTextEdit(TabPerso);
        EntryPerso->setObjectName(QString::fromUtf8("EntryPerso"));
        EntryPerso->setGeometry(QRect(160, 10, 231, 31));
        TabSource->addTab(TabPerso, QString());
        FrameControles = new QFrame(ZoneCentrale);
        FrameControles->setObjectName(QString::fromUtf8("FrameControles"));
        FrameControles->setGeometry(QRect(510, 380, 451, 151));
        FrameControles->setFrameShape(QFrame::StyledPanel);
        FrameControles->setFrameShadow(QFrame::Raised);
        LabelLancez = new QLabel(FrameControles);
        LabelLancez->setObjectName(QString::fromUtf8("LabelLancez"));
        LabelLancez->setGeometry(QRect(20, 20, 411, 16));
        LabelLancez->setFont(font1);
        BoutonCommencer = new QPushButton(FrameControles);
        BoutonCommencer->setObjectName(QString::fromUtf8("BoutonCommencer"));
        BoutonCommencer->setGeometry(QRect(240, 70, 191, 61));
        QFont font5;
        font5.setPointSize(16);
        BoutonCommencer->setFont(font5);
        BoutonQuitter = new QPushButton(FrameControles);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(20, 70, 191, 61));
        BoutonQuitter->setFont(font5);
        BoutonAide = new QPushButton(FrameControles);
        BoutonAide->setObjectName(QString::fromUtf8("BoutonAide"));
        BoutonAide->setGeometry(QRect(240, 20, 191, 31));
        BoutonAide->setFont(font1);
        EntryParam = new QLineEdit(ZoneCentrale);
        EntryParam->setObjectName(QString::fromUtf8("EntryParam"));
        EntryParam->setGeometry(QRect(40, 540, 741, 21));
        BoutonGenererParam = new QPushButton(ZoneCentrale);
        BoutonGenererParam->setObjectName(QString::fromUtf8("BoutonGenererParam"));
        BoutonGenererParam->setGeometry(QRect(790, 540, 81, 21));
        BoutonAppliquerParam = new QPushButton(ZoneCentrale);
        BoutonAppliquerParam->setObjectName(QString::fromUtf8("BoutonAppliquerParam"));
        BoutonAppliquerParam->setGeometry(QRect(880, 540, 81, 21));
        Menu->setCentralWidget(ZoneCentrale);
        BarreMenu = new QMenuBar(Menu);
        BarreMenu->setObjectName(QString::fromUtf8("BarreMenu"));
        BarreMenu->setGeometry(QRect(0, 0, 1000, 20));
        MenuFichier = new QMenu(BarreMenu);
        MenuFichier->setObjectName(QString::fromUtf8("MenuFichier"));
        MenuAide = new QMenu(BarreMenu);
        MenuAide->setObjectName(QString::fromUtf8("MenuAide"));
        Menu->setMenuBar(BarreMenu);

        BarreMenu->addAction(MenuFichier->menuAction());
        BarreMenu->addAction(MenuAide->menuAction());
        MenuFichier->addAction(MenuFichierQuitter);
        MenuFichier->addAction(MenuFichierParDefaut);
        MenuAide->addAction(MenuAideOuvrirAide);
        MenuAide->addAction(MenuAideOuvrirCredits);

        retranslateUi(Menu);

        TabMode->setCurrentIndex(1);
        TabSource->setCurrentIndex(2);


        QMetaObject::connectSlotsByName(Menu);
    } // setupUi

    void retranslateUi(QMainWindow *Menu)
    {
        Menu->setWindowTitle(QApplication::translate("Menu", "Menu", 0, QApplication::UnicodeUTF8));
        actionImprimer_scores->setText(QApplication::translate("Menu", "Imprimer scores", 0, QApplication::UnicodeUTF8));
        actionPoubelle_Ctrl_Q->setText(QApplication::translate("Menu", "Poubelle (Ctrl + Q)", 0, QApplication::UnicodeUTF8));
        actionPouet_OMFG->setText(QApplication::translate("Menu", "Pouet (OMFG)", 0, QApplication::UnicodeUTF8));
        actionTruc_FTG->setText(QApplication::translate("Menu", "Truc (FTG)", 0, QApplication::UnicodeUTF8));
        MenuFichierQuitter->setText(QApplication::translate("Menu", "&Quitter (Ctrl + Q)", 0, QApplication::UnicodeUTF8));
        MenuFichierParDefaut->setText(QApplication::translate("Menu", "&Par D\303\251faut (Ctrl + D)", 0, QApplication::UnicodeUTF8));
        MenuAideOuvrirAide->setText(QApplication::translate("Menu", "&Ouvrir le fichier d'aide (Ctrl + H)", 0, QApplication::UnicodeUTF8));
        MenuAideOuvrirCredits->setText(QApplication::translate("Menu", "Ouvrir &les cr\303\251dits (Ctrl + R)", 0, QApplication::UnicodeUTF8));
        LabelChoisissez->setText(QApplication::translate("Menu", "Choisissez vos options !", 0, QApplication::UnicodeUTF8));
        LabelMode->setText(QApplication::translate("Menu", "1. Choisissez votre mode de jeu", 0, QApplication::UnicodeUTF8));
        LabelTempsLimite->setText(QApplication::translate("Menu", "Temps (secondes) :", 0, QApplication::UnicodeUTF8));
        TabMode->setTabText(TabMode->indexOf(TabTempsLimite), QApplication::translate("Menu", "Temps limit\303\251", 0, QApplication::UnicodeUTF8));
        LabelMotLimite->setText(QApplication::translate("Menu", "Nombre de mots :", 0, QApplication::UnicodeUTF8));
        TabMode->setTabText(TabMode->indexOf(TabMotLimite), QApplication::translate("Menu", "Nombre de mots limit\303\251", 0, QApplication::UnicodeUTF8));
        LabelCorrection->setText(QApplication::translate("Menu", "2. Choisissez votre mode de correction", 0, QApplication::UnicodeUTF8));
        CorrManuValJuste->setText(QApplication::translate("Menu", "Correction avec <--- Validation &quand le mot est juste", 0, QApplication::UnicodeUTF8));
        CorrManuValAll->setText(QApplication::translate("Menu", "Correction avec <--- &Validation dans tous les cas", 0, QApplication::UnicodeUTF8));
        CorrAuto->setText(QApplication::translate("Menu", "Co&rrection automatique", 0, QApplication::UnicodeUTF8));
        LabelSource->setText(QApplication::translate("Menu", "3. Choisissez votre source de texte", 0, QApplication::UnicodeUTF8));
        LabelMotsFR->setText(QApplication::translate("Menu", "Nombre de mots les plus utilis\303\251s :", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabMotsFR), QApplication::translate("Menu", "Mots les plus utilis\303\251s", 0, QApplication::UnicodeUTF8));
        LabelActu->setText(QApplication::translate("Menu", "Nombre de lignes :", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabActu), QApplication::translate("Menu", "Texte d'actu", 0, QApplication::UnicodeUTF8));
        LabelPerso->setText(QApplication::translate("Menu", "Lien ou copier-coller du texte :", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabPerso), QApplication::translate("Menu", "Texte perso", 0, QApplication::UnicodeUTF8));
        LabelLancez->setText(QApplication::translate("Menu", "4. Lancez-vous !", 0, QApplication::UnicodeUTF8));
        BoutonCommencer->setText(QApplication::translate("Menu", "Commencer", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Menu", "Quitter", 0, QApplication::UnicodeUTF8));
        BoutonAide->setText(QApplication::translate("Menu", "Aide et Cr\303\251dits", 0, QApplication::UnicodeUTF8));
        BoutonGenererParam->setText(QApplication::translate("Menu", "G\303\251n\303\251rer", 0, QApplication::UnicodeUTF8));
        BoutonAppliquerParam->setText(QApplication::translate("Menu", "Appliquer", 0, QApplication::UnicodeUTF8));
        MenuFichier->setTitle(QApplication::translate("Menu", "Fic&hier", 0, QApplication::UnicodeUTF8));
        MenuAide->setTitle(QApplication::translate("Menu", "Aide", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Menu: public Ui_Menu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MENU_H
