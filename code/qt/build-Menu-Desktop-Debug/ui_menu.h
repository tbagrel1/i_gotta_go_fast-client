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
#include <QtGui/QPlainTextEdit>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QSpinBox>
#include <QtGui/QTabWidget>
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
    QLabel *label;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QSpinBox *spinBox;
    QSpinBox *spinBox_2;
    QFrame *FrameSource;
    QLabel *LabelSource;
    QTabWidget *TabSource;
    QWidget *TabMotsFR;
    QFrame *Sep1;
    QLabel *label_3;
    QRadioButton *radioButton;
    QSpinBox *spinBox_3;
    QLabel *label_4;
    QLabel *label_5;
    QRadioButton *radioButton_2;
    QLineEdit *lineEdit;
    QWidget *TabActu;
    QRadioButton *TexteEx1R;
    QRadioButton *TexteEx2R;
    QRadioButton *TexteEx3R;
    QLabel *TexteEx1;
    QLabel *TexteEx2;
    QLabel *TexteEx3;
    QWidget *TabPerso;
    QRadioButton *CollerTexteR;
    QPlainTextEdit *CollerTexteV;
    QRadioButton *NonTexteR;
    QLineEdit *NomTexteV;
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
        FrameModeJeu->setGeometry(QRect(510, 210, 451, 151));
        FrameModeJeu->setFrameShape(QFrame::StyledPanel);
        FrameModeJeu->setFrameShadow(QFrame::Plain);
        LabelMode = new QLabel(FrameModeJeu);
        LabelMode->setObjectName(QString::fromUtf8("LabelMode"));
        LabelMode->setGeometry(QRect(20, 20, 411, 16));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        LabelMode->setFont(font1);
        label = new QLabel(FrameModeJeu);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 50, 151, 41));
        QFont font2;
        font2.setPointSize(14);
        label->setFont(font2);
        label_8 = new QLabel(FrameModeJeu);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(120, 100, 101, 31));
        label_8->setFont(font2);
        label_9 = new QLabel(FrameModeJeu);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(330, 100, 101, 31));
        label_9->setFont(font2);
        label_10 = new QLabel(FrameModeJeu);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(190, 100, 41, 31));
        QFont font3;
        font3.setPointSize(16);
        font3.setBold(true);
        font3.setWeight(75);
        label_10->setFont(font3);
        label_10->setAlignment(Qt::AlignCenter);
        spinBox = new QSpinBox(FrameModeJeu);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setGeometry(QRect(20, 100, 91, 31));
        QFont font4;
        font4.setPointSize(16);
        spinBox->setFont(font4);
        spinBox->setAlignment(Qt::AlignCenter);
        spinBox->setMaximum(10);
        spinBox->setSingleStep(1);
        spinBox->setValue(1);
        spinBox_2 = new QSpinBox(FrameModeJeu);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));
        spinBox_2->setGeometry(QRect(230, 100, 91, 31));
        spinBox_2->setFont(font4);
        spinBox_2->setAlignment(Qt::AlignCenter);
        spinBox_2->setMaximum(50);
        spinBox_2->setSingleStep(10);
        FrameSource = new QFrame(ZoneCentrale);
        FrameSource->setObjectName(QString::fromUtf8("FrameSource"));
        FrameSource->setGeometry(QRect(40, 210, 451, 321));
        FrameSource->setFrameShape(QFrame::StyledPanel);
        FrameSource->setFrameShadow(QFrame::Raised);
        LabelSource = new QLabel(FrameSource);
        LabelSource->setObjectName(QString::fromUtf8("LabelSource"));
        LabelSource->setGeometry(QRect(20, 20, 411, 16));
        LabelSource->setFont(font1);
        TabSource = new QTabWidget(FrameSource);
        TabSource->setObjectName(QString::fromUtf8("TabSource"));
        TabSource->setGeometry(QRect(20, 50, 411, 251));
        QFont font5;
        font5.setPointSize(11);
        TabSource->setFont(font5);
        TabMotsFR = new QWidget();
        TabMotsFR->setObjectName(QString::fromUtf8("TabMotsFR"));
        Sep1 = new QFrame(TabMotsFR);
        Sep1->setObjectName(QString::fromUtf8("Sep1"));
        Sep1->setGeometry(QRect(20, 79, 371, 21));
        Sep1->setFrameShape(QFrame::HLine);
        Sep1->setFrameShadow(QFrame::Sunken);
        label_3 = new QLabel(TabMotsFR);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(50, 130, 211, 31));
        label_3->setFont(font2);
        radioButton = new QRadioButton(TabMotsFR);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));
        radioButton->setGeometry(QRect(20, 10, 131, 31));
        radioButton->setFont(font2);
        radioButton->setChecked(true);
        spinBox_3 = new QSpinBox(TabMotsFR);
        spinBox_3->setObjectName(QString::fromUtf8("spinBox_3"));
        spinBox_3->setGeometry(QRect(160, 10, 91, 31));
        spinBox_3->setFont(font2);
        spinBox_3->setAlignment(Qt::AlignCenter);
        spinBox_3->setMinimum(100);
        spinBox_3->setMaximum(10000);
        spinBox_3->setSingleStep(100);
        spinBox_3->setValue(100);
        label_4 = new QLabel(TabMotsFR);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(260, 10, 131, 31));
        label_4->setFont(font2);
        label_5 = new QLabel(TabMotsFR);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(50, 45, 331, 31));
        label_5->setFont(font2);
        label_5->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        radioButton_2 = new QRadioButton(TabMotsFR);
        radioButton_2->setObjectName(QString::fromUtf8("radioButton_2"));
        radioButton_2->setGeometry(QRect(20, 100, 371, 31));
        radioButton_2->setFont(font2);
        lineEdit = new QLineEdit(TabMotsFR);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(240, 130, 81, 31));
        lineEdit->setFont(font2);
        lineEdit->setMaxLength(5);
        TabSource->addTab(TabMotsFR, QString());
        TabActu = new QWidget();
        TabActu->setObjectName(QString::fromUtf8("TabActu"));
        TexteEx1R = new QRadioButton(TabActu);
        TexteEx1R->setObjectName(QString::fromUtf8("TexteEx1R"));
        TexteEx1R->setGeometry(QRect(20, 20, 371, 21));
        TexteEx1R->setChecked(true);
        TexteEx2R = new QRadioButton(TabActu);
        TexteEx2R->setObjectName(QString::fromUtf8("TexteEx2R"));
        TexteEx2R->setGeometry(QRect(20, 80, 371, 21));
        TexteEx3R = new QRadioButton(TabActu);
        TexteEx3R->setObjectName(QString::fromUtf8("TexteEx3R"));
        TexteEx3R->setGeometry(QRect(20, 140, 371, 21));
        TexteEx1 = new QLabel(TabActu);
        TexteEx1->setObjectName(QString::fromUtf8("TexteEx1"));
        TexteEx1->setGeometry(QRect(20, 40, 371, 31));
        TexteEx2 = new QLabel(TabActu);
        TexteEx2->setObjectName(QString::fromUtf8("TexteEx2"));
        TexteEx2->setGeometry(QRect(20, 100, 371, 31));
        TexteEx3 = new QLabel(TabActu);
        TexteEx3->setObjectName(QString::fromUtf8("TexteEx3"));
        TexteEx3->setGeometry(QRect(20, 160, 371, 31));
        TabSource->addTab(TabActu, QString());
        TabPerso = new QWidget();
        TabPerso->setObjectName(QString::fromUtf8("TabPerso"));
        CollerTexteR = new QRadioButton(TabPerso);
        CollerTexteR->setObjectName(QString::fromUtf8("CollerTexteR"));
        CollerTexteR->setGeometry(QRect(20, 10, 371, 21));
        CollerTexteR->setChecked(true);
        CollerTexteV = new QPlainTextEdit(TabPerso);
        CollerTexteV->setObjectName(QString::fromUtf8("CollerTexteV"));
        CollerTexteV->setGeometry(QRect(20, 40, 371, 131));
        NonTexteR = new QRadioButton(TabPerso);
        NonTexteR->setObjectName(QString::fromUtf8("NonTexteR"));
        NonTexteR->setGeometry(QRect(20, 180, 151, 21));
        NomTexteV = new QLineEdit(TabPerso);
        NomTexteV->setObjectName(QString::fromUtf8("NomTexteV"));
        NomTexteV->setGeometry(QRect(170, 180, 221, 21));
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
        BoutonCommencer->setFont(font4);
        BoutonQuitter = new QPushButton(FrameControles);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(20, 70, 191, 61));
        BoutonQuitter->setFont(font4);
        BoutonAide = new QPushButton(FrameControles);
        BoutonAide->setObjectName(QString::fromUtf8("BoutonAide"));
        BoutonAide->setGeometry(QRect(240, 20, 191, 31));
        QFont font6;
        font6.setPointSize(12);
        BoutonAide->setFont(font6);
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

        TabSource->setCurrentIndex(0);


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
        LabelMode->setText(QApplication::translate("Menu", "2. Choisissez votre temps de jeu", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Menu", "Temps de jeu :", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("Menu", "Minutes", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("Menu", "Secondes", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("Menu", ":", 0, QApplication::UnicodeUTF8));
        LabelSource->setText(QApplication::translate("Menu", "1. Choisissez votre source de texte", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("Menu", "poss\303\251dant la syllabe", 0, QApplication::UnicodeUTF8));
        radioButton->setText(QApplication::translate("Menu", " Affiche&r les", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("Menu", "mots les plus", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("Menu", "utilis\303\251s de la langue fran\303\247aise", 0, QApplication::UnicodeUTF8));
        radioButton_2->setText(QApplication::translate("Menu", " Afficher uni&quement des mots", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabMotsFR), QApplication::translate("Menu", "Mots sp\303\251ciaux", 0, QApplication::UnicodeUTF8));
        TexteEx1R->setText(QApplication::translate("Menu", "Tchoupi va &\303\240 la plage", 0, QApplication::UnicodeUTF8));
        TexteEx2R->setText(QApplication::translate("Menu", "Tchoupi &va \303\240 la boulangerie", 0, QApplication::UnicodeUTF8));
        TexteEx3R->setText(QApplication::translate("Menu", "Tchoupi va au &bordel", 0, QApplication::UnicodeUTF8));
        TexteEx1->setText(QApplication::translate("Menu", "Difficult\303\251 *", 0, QApplication::UnicodeUTF8));
        TexteEx2->setText(QApplication::translate("Menu", "Difficult\303\251 **", 0, QApplication::UnicodeUTF8));
        TexteEx3->setText(QApplication::translate("Menu", "Difficult\303\251 ***", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabActu), QApplication::translate("Menu", "Exemple de texte", 0, QApplication::UnicodeUTF8));
        CollerTexteR->setText(QApplication::translate("Menu", "Texte (copier-coller) :", 0, QApplication::UnicodeUTF8));
        NonTexteR->setText(QApplication::translate("Menu", "Nom du fichier :", 0, QApplication::UnicodeUTF8));
        TabSource->setTabText(TabSource->indexOf(TabPerso), QApplication::translate("Menu", "Texte perso", 0, QApplication::UnicodeUTF8));
        LabelLancez->setText(QApplication::translate("Menu", "3. Lancez-vous !", 0, QApplication::UnicodeUTF8));
        BoutonCommencer->setText(QApplication::translate("Menu", "Commencer", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Menu", "Quitter", 0, QApplication::UnicodeUTF8));
        BoutonAide->setText(QApplication::translate("Menu", "Aide et Cr\303\251dits", 0, QApplication::UnicodeUTF8));
        BoutonGenererParam->setText(QApplication::translate("Menu", "G\303\251n\303\251rer", 0, QApplication::UnicodeUTF8));
        BoutonAppliquerParam->setText(QApplication::translate("Menu", "Appliquer", 0, QApplication::UnicodeUTF8));
        MenuFichier->setTitle(QApplication::translate("Menu", "Fic&hier", 0, QApplication::UnicodeUTF8));
        MenuAide->setTitle(QApplication::translate("Menu", "A&ide", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Menu: public Ui_Menu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MENU_H
