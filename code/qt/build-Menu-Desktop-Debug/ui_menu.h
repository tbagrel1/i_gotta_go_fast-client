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
    QFrame *FrameTempsJeu;
    QLabel *LabelTempsJeuT;
    QLabel *LabelTempsJeuMinutes;
    QLabel *LabelTempsJeuSecondes;
    QLabel *LabelTempsColon;
    QSpinBox *SBoxMinutes;
    QSpinBox *SBoxSecondes;
    QFrame *FrameSource;
    QLabel *LabelSource;
    QTabWidget *TabSourceTexte;
    QWidget *TabSpeciaux;
    QFrame *Sep1;
    QLabel *LabelSyll;
    QRadioButton *RadioMotsFR;
    QSpinBox *SBoxMotsFR;
    QLabel *LabelMotsFR1;
    QLabel *LabelMotsFR2;
    QRadioButton *RadioSyll;
    QLineEdit *EntrySyll;
    QWidget *TabExemple;
    QRadioButton *LabelTexteEx1R;
    QRadioButton *LabelTexteEx2R;
    QRadioButton *LabelTexteEx3R;
    QLabel *LabelTexteEx1;
    QLabel *LabelTexteEx2;
    QLabel *LabelTexteEx3;
    QWidget *TabPerso;
    QRadioButton *CollerTexteR;
    QPlainTextEdit *CollerTexteV;
    QRadioButton *NomTexteR;
    QLineEdit *NomTexteV;
    QFrame *FrameControles;
    QLabel *LabelLancez;
    QPushButton *BoutonCommencer;
    QPushButton *BoutonQuitter;
    QPushButton *BoutonAide;
    QLineEdit *EntryParam;
    QPushButton *BoutonGenererParam;
    QPushButton *BoutonAppliquerParam;
    QFrame *FramePseudo;
    QLabel *LabelPseudoT;
    QLabel *LabelPseudo;
    QLineEdit *EntryPseudo;

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
        MenuFichierQuitter->setEnabled(true);
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
        FrameTempsJeu = new QFrame(ZoneCentrale);
        FrameTempsJeu->setObjectName(QString::fromUtf8("FrameTempsJeu"));
        FrameTempsJeu->setGeometry(QRect(510, 210, 451, 91));
        FrameTempsJeu->setFrameShape(QFrame::StyledPanel);
        FrameTempsJeu->setFrameShadow(QFrame::Plain);
        LabelTempsJeuT = new QLabel(FrameTempsJeu);
        LabelTempsJeuT->setObjectName(QString::fromUtf8("LabelTempsJeuT"));
        LabelTempsJeuT->setGeometry(QRect(20, 20, 411, 16));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        LabelTempsJeuT->setFont(font1);
        LabelTempsJeuMinutes = new QLabel(FrameTempsJeu);
        LabelTempsJeuMinutes->setObjectName(QString::fromUtf8("LabelTempsJeuMinutes"));
        LabelTempsJeuMinutes->setGeometry(QRect(120, 50, 101, 31));
        QFont font2;
        font2.setPointSize(14);
        LabelTempsJeuMinutes->setFont(font2);
        LabelTempsJeuSecondes = new QLabel(FrameTempsJeu);
        LabelTempsJeuSecondes->setObjectName(QString::fromUtf8("LabelTempsJeuSecondes"));
        LabelTempsJeuSecondes->setGeometry(QRect(330, 50, 101, 31));
        LabelTempsJeuSecondes->setFont(font2);
        LabelTempsColon = new QLabel(FrameTempsJeu);
        LabelTempsColon->setObjectName(QString::fromUtf8("LabelTempsColon"));
        LabelTempsColon->setGeometry(QRect(190, 50, 41, 31));
        QFont font3;
        font3.setPointSize(16);
        font3.setBold(true);
        font3.setWeight(75);
        LabelTempsColon->setFont(font3);
        LabelTempsColon->setAlignment(Qt::AlignCenter);
        SBoxMinutes = new QSpinBox(FrameTempsJeu);
        SBoxMinutes->setObjectName(QString::fromUtf8("SBoxMinutes"));
        SBoxMinutes->setGeometry(QRect(20, 50, 91, 31));
        QFont font4;
        font4.setPointSize(16);
        SBoxMinutes->setFont(font4);
        SBoxMinutes->setAlignment(Qt::AlignCenter);
        SBoxMinutes->setMaximum(10);
        SBoxMinutes->setSingleStep(1);
        SBoxMinutes->setValue(1);
        SBoxSecondes = new QSpinBox(FrameTempsJeu);
        SBoxSecondes->setObjectName(QString::fromUtf8("SBoxSecondes"));
        SBoxSecondes->setGeometry(QRect(230, 50, 91, 31));
        SBoxSecondes->setFont(font4);
        SBoxSecondes->setAlignment(Qt::AlignCenter);
        SBoxSecondes->setMaximum(50);
        SBoxSecondes->setSingleStep(10);
        FrameSource = new QFrame(ZoneCentrale);
        FrameSource->setObjectName(QString::fromUtf8("FrameSource"));
        FrameSource->setGeometry(QRect(40, 210, 451, 321));
        FrameSource->setFrameShape(QFrame::StyledPanel);
        FrameSource->setFrameShadow(QFrame::Raised);
        LabelSource = new QLabel(FrameSource);
        LabelSource->setObjectName(QString::fromUtf8("LabelSource"));
        LabelSource->setGeometry(QRect(20, 20, 411, 16));
        LabelSource->setFont(font1);
        TabSourceTexte = new QTabWidget(FrameSource);
        TabSourceTexte->setObjectName(QString::fromUtf8("TabSourceTexte"));
        TabSourceTexte->setGeometry(QRect(20, 50, 411, 251));
        QFont font5;
        font5.setPointSize(11);
        TabSourceTexte->setFont(font5);
        TabSpeciaux = new QWidget();
        TabSpeciaux->setObjectName(QString::fromUtf8("TabSpeciaux"));
        Sep1 = new QFrame(TabSpeciaux);
        Sep1->setObjectName(QString::fromUtf8("Sep1"));
        Sep1->setGeometry(QRect(20, 100, 371, 21));
        Sep1->setFrameShape(QFrame::HLine);
        Sep1->setFrameShadow(QFrame::Sunken);
        LabelSyll = new QLabel(TabSpeciaux);
        LabelSyll->setObjectName(QString::fromUtf8("LabelSyll"));
        LabelSyll->setGeometry(QRect(50, 170, 211, 31));
        LabelSyll->setFont(font2);
        RadioMotsFR = new QRadioButton(TabSpeciaux);
        RadioMotsFR->setObjectName(QString::fromUtf8("RadioMotsFR"));
        RadioMotsFR->setGeometry(QRect(20, 20, 131, 31));
        RadioMotsFR->setFont(font2);
        RadioMotsFR->setChecked(true);
        SBoxMotsFR = new QSpinBox(TabSpeciaux);
        SBoxMotsFR->setObjectName(QString::fromUtf8("SBoxMotsFR"));
        SBoxMotsFR->setGeometry(QRect(160, 20, 91, 31));
        SBoxMotsFR->setFont(font2);
        SBoxMotsFR->setAlignment(Qt::AlignCenter);
        SBoxMotsFR->setMinimum(100);
        SBoxMotsFR->setMaximum(5000);
        SBoxMotsFR->setSingleStep(100);
        SBoxMotsFR->setValue(100);
        LabelMotsFR1 = new QLabel(TabSpeciaux);
        LabelMotsFR1->setObjectName(QString::fromUtf8("LabelMotsFR1"));
        LabelMotsFR1->setGeometry(QRect(260, 20, 131, 31));
        LabelMotsFR1->setFont(font2);
        LabelMotsFR2 = new QLabel(TabSpeciaux);
        LabelMotsFR2->setObjectName(QString::fromUtf8("LabelMotsFR2"));
        LabelMotsFR2->setGeometry(QRect(50, 60, 331, 31));
        LabelMotsFR2->setFont(font2);
        LabelMotsFR2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        RadioSyll = new QRadioButton(TabSpeciaux);
        RadioSyll->setObjectName(QString::fromUtf8("RadioSyll"));
        RadioSyll->setGeometry(QRect(20, 130, 371, 31));
        RadioSyll->setFont(font2);
        EntrySyll = new QLineEdit(TabSpeciaux);
        EntrySyll->setObjectName(QString::fromUtf8("EntrySyll"));
        EntrySyll->setGeometry(QRect(240, 170, 81, 31));
        EntrySyll->setFont(font2);
        EntrySyll->setMaxLength(5);
        EntrySyll->setAlignment(Qt::AlignCenter);
        TabSourceTexte->addTab(TabSpeciaux, QString());
        TabExemple = new QWidget();
        TabExemple->setObjectName(QString::fromUtf8("TabExemple"));
        LabelTexteEx1R = new QRadioButton(TabExemple);
        LabelTexteEx1R->setObjectName(QString::fromUtf8("LabelTexteEx1R"));
        LabelTexteEx1R->setGeometry(QRect(20, 20, 371, 21));
        LabelTexteEx1R->setChecked(true);
        LabelTexteEx2R = new QRadioButton(TabExemple);
        LabelTexteEx2R->setObjectName(QString::fromUtf8("LabelTexteEx2R"));
        LabelTexteEx2R->setGeometry(QRect(20, 80, 371, 21));
        LabelTexteEx3R = new QRadioButton(TabExemple);
        LabelTexteEx3R->setObjectName(QString::fromUtf8("LabelTexteEx3R"));
        LabelTexteEx3R->setGeometry(QRect(20, 140, 371, 21));
        LabelTexteEx1 = new QLabel(TabExemple);
        LabelTexteEx1->setObjectName(QString::fromUtf8("LabelTexteEx1"));
        LabelTexteEx1->setGeometry(QRect(20, 40, 371, 31));
        LabelTexteEx2 = new QLabel(TabExemple);
        LabelTexteEx2->setObjectName(QString::fromUtf8("LabelTexteEx2"));
        LabelTexteEx2->setGeometry(QRect(20, 100, 371, 31));
        LabelTexteEx3 = new QLabel(TabExemple);
        LabelTexteEx3->setObjectName(QString::fromUtf8("LabelTexteEx3"));
        LabelTexteEx3->setGeometry(QRect(20, 160, 371, 31));
        TabSourceTexte->addTab(TabExemple, QString());
        TabPerso = new QWidget();
        TabPerso->setObjectName(QString::fromUtf8("TabPerso"));
        CollerTexteR = new QRadioButton(TabPerso);
        CollerTexteR->setObjectName(QString::fromUtf8("CollerTexteR"));
        CollerTexteR->setGeometry(QRect(20, 10, 371, 21));
        CollerTexteR->setChecked(true);
        CollerTexteV = new QPlainTextEdit(TabPerso);
        CollerTexteV->setObjectName(QString::fromUtf8("CollerTexteV"));
        CollerTexteV->setGeometry(QRect(20, 40, 371, 131));
        CollerTexteV->setFont(font5);
        NomTexteR = new QRadioButton(TabPerso);
        NomTexteR->setObjectName(QString::fromUtf8("NomTexteR"));
        NomTexteR->setGeometry(QRect(20, 180, 151, 21));
        NomTexteV = new QLineEdit(TabPerso);
        NomTexteV->setObjectName(QString::fromUtf8("NomTexteV"));
        NomTexteV->setGeometry(QRect(170, 180, 221, 21));
        NomTexteV->setFont(font5);
        TabSourceTexte->addTab(TabPerso, QString());
        FrameControles = new QFrame(ZoneCentrale);
        FrameControles->setObjectName(QString::fromUtf8("FrameControles"));
        FrameControles->setGeometry(QRect(510, 410, 451, 121));
        FrameControles->setFrameShape(QFrame::StyledPanel);
        FrameControles->setFrameShadow(QFrame::Raised);
        LabelLancez = new QLabel(FrameControles);
        LabelLancez->setObjectName(QString::fromUtf8("LabelLancez"));
        LabelLancez->setGeometry(QRect(20, 20, 411, 16));
        LabelLancez->setFont(font1);
        BoutonCommencer = new QPushButton(FrameControles);
        BoutonCommencer->setObjectName(QString::fromUtf8("BoutonCommencer"));
        BoutonCommencer->setGeometry(QRect(240, 50, 191, 61));
        BoutonCommencer->setFont(font4);
        BoutonQuitter = new QPushButton(FrameControles);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(20, 50, 191, 61));
        BoutonQuitter->setFont(font4);
        BoutonAide = new QPushButton(FrameControles);
        BoutonAide->setObjectName(QString::fromUtf8("BoutonAide"));
        BoutonAide->setGeometry(QRect(240, 20, 191, 21));
        QFont font6;
        font6.setPointSize(12);
        BoutonAide->setFont(font6);
        EntryParam = new QLineEdit(ZoneCentrale);
        EntryParam->setObjectName(QString::fromUtf8("EntryParam"));
        EntryParam->setGeometry(QRect(40, 540, 741, 21));
        EntryParam->setMaxLength(5000);
        BoutonGenererParam = new QPushButton(ZoneCentrale);
        BoutonGenererParam->setObjectName(QString::fromUtf8("BoutonGenererParam"));
        BoutonGenererParam->setGeometry(QRect(790, 540, 81, 21));
        BoutonAppliquerParam = new QPushButton(ZoneCentrale);
        BoutonAppliquerParam->setObjectName(QString::fromUtf8("BoutonAppliquerParam"));
        BoutonAppliquerParam->setGeometry(QRect(880, 540, 81, 21));
        FramePseudo = new QFrame(ZoneCentrale);
        FramePseudo->setObjectName(QString::fromUtf8("FramePseudo"));
        FramePseudo->setGeometry(QRect(510, 310, 451, 91));
        FramePseudo->setFrameShape(QFrame::StyledPanel);
        FramePseudo->setFrameShadow(QFrame::Raised);
        LabelPseudoT = new QLabel(FramePseudo);
        LabelPseudoT->setObjectName(QString::fromUtf8("LabelPseudoT"));
        LabelPseudoT->setGeometry(QRect(20, 20, 411, 21));
        LabelPseudoT->setFont(font1);
        LabelPseudo = new QLabel(FramePseudo);
        LabelPseudo->setObjectName(QString::fromUtf8("LabelPseudo"));
        LabelPseudo->setGeometry(QRect(20, 50, 111, 31));
        LabelPseudo->setFont(font2);
        EntryPseudo = new QLineEdit(FramePseudo);
        EntryPseudo->setObjectName(QString::fromUtf8("EntryPseudo"));
        EntryPseudo->setGeometry(QRect(110, 50, 321, 31));
        QFont font7;
        font7.setPointSize(14);
        font7.setItalic(true);
        EntryPseudo->setFont(font7);
        EntryPseudo->setMaxLength(20);
        EntryPseudo->setAlignment(Qt::AlignCenter);
        Menu->setCentralWidget(ZoneCentrale);

        retranslateUi(Menu);

        TabSourceTexte->setCurrentIndex(1);


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
        LabelTempsJeuT->setText(QApplication::translate("Menu", "2. Choisissez votre temps de jeu", 0, QApplication::UnicodeUTF8));
        LabelTempsJeuMinutes->setText(QApplication::translate("Menu", "Minutes", 0, QApplication::UnicodeUTF8));
        LabelTempsJeuSecondes->setText(QApplication::translate("Menu", "Secondes", 0, QApplication::UnicodeUTF8));
        LabelTempsColon->setText(QApplication::translate("Menu", ":", 0, QApplication::UnicodeUTF8));
        LabelSource->setText(QApplication::translate("Menu", "1. Choisissez votre source de texte", 0, QApplication::UnicodeUTF8));
        LabelSyll->setText(QApplication::translate("Menu", "poss\303\251dant la syllabe", 0, QApplication::UnicodeUTF8));
        RadioMotsFR->setText(QApplication::translate("Menu", " Affiche&r les", 0, QApplication::UnicodeUTF8));
        LabelMotsFR1->setText(QApplication::translate("Menu", "mots les plus", 0, QApplication::UnicodeUTF8));
        LabelMotsFR2->setText(QApplication::translate("Menu", "utilis\303\251s de la langue fran\303\247aise", 0, QApplication::UnicodeUTF8));
        RadioSyll->setText(QApplication::translate("Menu", " Afficher uni&quement des mots", 0, QApplication::UnicodeUTF8));
        TabSourceTexte->setTabText(TabSourceTexte->indexOf(TabSpeciaux), QApplication::translate("Menu", "Mots sp\303\251ciaux", 0, QApplication::UnicodeUTF8));
        LabelTexteEx1R->setText(QApplication::translate("Menu", "Tchoupi va &\303\240 la plage", 0, QApplication::UnicodeUTF8));
        LabelTexteEx2R->setText(QApplication::translate("Menu", "Tchoupi &va \303\240 la boulangerie", 0, QApplication::UnicodeUTF8));
        LabelTexteEx3R->setText(QApplication::translate("Menu", "Tchoupi va au &bordel", 0, QApplication::UnicodeUTF8));
        LabelTexteEx1->setText(QApplication::translate("Menu", "Difficult\303\251 *", 0, QApplication::UnicodeUTF8));
        LabelTexteEx2->setText(QApplication::translate("Menu", "Difficult\303\251 **", 0, QApplication::UnicodeUTF8));
        LabelTexteEx3->setText(QApplication::translate("Menu", "Difficult\303\251 ***", 0, QApplication::UnicodeUTF8));
        TabSourceTexte->setTabText(TabSourceTexte->indexOf(TabExemple), QApplication::translate("Menu", "Exemple de texte", 0, QApplication::UnicodeUTF8));
        CollerTexteR->setText(QApplication::translate("Menu", "&Texte (copier-coller) :", 0, QApplication::UnicodeUTF8));
        NomTexteR->setText(QApplication::translate("Menu", "Nom du fichier :", 0, QApplication::UnicodeUTF8));
        TabSourceTexte->setTabText(TabSourceTexte->indexOf(TabPerso), QApplication::translate("Menu", "Texte perso", 0, QApplication::UnicodeUTF8));
        LabelLancez->setText(QApplication::translate("Menu", "4. Lancez-vous !", 0, QApplication::UnicodeUTF8));
        BoutonCommencer->setText(QApplication::translate("Menu", "Commencer", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Menu", "Quitter", 0, QApplication::UnicodeUTF8));
        BoutonAide->setText(QApplication::translate("Menu", "Aide et Cr\303\251dits", 0, QApplication::UnicodeUTF8));
        BoutonGenererParam->setText(QApplication::translate("Menu", "G\303\251n\303\251rer", 0, QApplication::UnicodeUTF8));
        BoutonAppliquerParam->setText(QApplication::translate("Menu", "Appliquer", 0, QApplication::UnicodeUTF8));
        LabelPseudoT->setText(QApplication::translate("Menu", "3. Choisissez votre pseudo (facultatif)", 0, QApplication::UnicodeUTF8));
        LabelPseudo->setText(QApplication::translate("Menu", "Pseudo :", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Menu: public Ui_Menu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MENU_H
