/********************************************************************************
** Form generated from reading UI file 'score.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SCORE_H
#define UI_SCORE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>
#include <QtWebKit/QWebView>

QT_BEGIN_NAMESPACE

class Ui_Score
{
public:
    QLabel *LabelScore;
    QLabel *LabelMPM;
    QLabel *LabelCPM;
    QLabel *LabelRang;
    QLabel *LabelScoreV;
    QLabel *LabelMPMV;
    QLabel *LabelCPMV;
    QLabel *LabelRangV;
    QLabel *LabelScoreT;
    QPushButton *BoutonQuitter;
    QLabel *LabelIcone;
    QPushButton *BoutonScoresLigne;
    QLabel *LabelLienSite;
    QWebView *ViewScore;

    void setupUi(QWidget *Score)
    {
        if (Score->objectName().isEmpty())
            Score->setObjectName(QString::fromUtf8("Score"));
        Score->resize(1000, 730);
        Score->setMinimumSize(QSize(1000, 730));
        Score->setMaximumSize(QSize(1000, 730));
        LabelScore = new QLabel(Score);
        LabelScore->setObjectName(QString::fromUtf8("LabelScore"));
        LabelScore->setGeometry(QRect(40, 110, 231, 41));
        QFont font;
        font.setPointSize(15);
        font.setItalic(true);
        LabelScore->setFont(font);
        LabelScore->setFrameShape(QFrame::Box);
        LabelScore->setAlignment(Qt::AlignCenter);
        LabelMPM = new QLabel(Score);
        LabelMPM->setObjectName(QString::fromUtf8("LabelMPM"));
        LabelMPM->setGeometry(QRect(270, 110, 231, 41));
        LabelMPM->setFont(font);
        LabelMPM->setFrameShape(QFrame::Box);
        LabelMPM->setAlignment(Qt::AlignCenter);
        LabelCPM = new QLabel(Score);
        LabelCPM->setObjectName(QString::fromUtf8("LabelCPM"));
        LabelCPM->setGeometry(QRect(500, 110, 231, 41));
        LabelCPM->setFont(font);
        LabelCPM->setFrameShape(QFrame::Box);
        LabelCPM->setAlignment(Qt::AlignCenter);
        LabelRang = new QLabel(Score);
        LabelRang->setObjectName(QString::fromUtf8("LabelRang"));
        LabelRang->setGeometry(QRect(730, 110, 231, 41));
        LabelRang->setFont(font);
        LabelRang->setFrameShape(QFrame::Box);
        LabelRang->setAlignment(Qt::AlignCenter);
        LabelScoreV = new QLabel(Score);
        LabelScoreV->setObjectName(QString::fromUtf8("LabelScoreV"));
        LabelScoreV->setGeometry(QRect(40, 150, 231, 41));
        QFont font1;
        font1.setPointSize(20);
        LabelScoreV->setFont(font1);
        LabelScoreV->setFrameShape(QFrame::WinPanel);
        LabelScoreV->setAlignment(Qt::AlignCenter);
        LabelMPMV = new QLabel(Score);
        LabelMPMV->setObjectName(QString::fromUtf8("LabelMPMV"));
        LabelMPMV->setGeometry(QRect(270, 150, 231, 41));
        LabelMPMV->setFont(font1);
        LabelMPMV->setFrameShape(QFrame::WinPanel);
        LabelMPMV->setAlignment(Qt::AlignCenter);
        LabelCPMV = new QLabel(Score);
        LabelCPMV->setObjectName(QString::fromUtf8("LabelCPMV"));
        LabelCPMV->setGeometry(QRect(500, 150, 231, 41));
        LabelCPMV->setFont(font1);
        LabelCPMV->setFrameShape(QFrame::WinPanel);
        LabelCPMV->setAlignment(Qt::AlignCenter);
        LabelRangV = new QLabel(Score);
        LabelRangV->setObjectName(QString::fromUtf8("LabelRangV"));
        LabelRangV->setGeometry(QRect(730, 150, 231, 41));
        QFont font2;
        font2.setPointSize(16);
        LabelRangV->setFont(font2);
        LabelRangV->setFrameShape(QFrame::WinPanel);
        LabelRangV->setAlignment(Qt::AlignCenter);
        LabelScoreT = new QLabel(Score);
        LabelScoreT->setObjectName(QString::fromUtf8("LabelScoreT"));
        LabelScoreT->setGeometry(QRect(40, 30, 921, 61));
        QFont font3;
        font3.setPointSize(36);
        LabelScoreT->setFont(font3);
        LabelScoreT->setAlignment(Qt::AlignCenter);
        BoutonQuitter = new QPushButton(Score);
        BoutonQuitter->setObjectName(QString::fromUtf8("BoutonQuitter"));
        BoutonQuitter->setGeometry(QRect(710, 620, 251, 71));
        BoutonQuitter->setFont(font1);
        LabelIcone = new QLabel(Score);
        LabelIcone->setObjectName(QString::fromUtf8("LabelIcone"));
        LabelIcone->setGeometry(QRect(40, 620, 251, 71));
        BoutonScoresLigne = new QPushButton(Score);
        BoutonScoresLigne->setObjectName(QString::fromUtf8("BoutonScoresLigne"));
        BoutonScoresLigne->setGeometry(QRect(309, 620, 371, 31));
        QFont font4;
        font4.setPointSize(15);
        BoutonScoresLigne->setFont(font4);
        LabelLienSite = new QLabel(Score);
        LabelLienSite->setObjectName(QString::fromUtf8("LabelLienSite"));
        LabelLienSite->setGeometry(QRect(310, 660, 371, 31));
        LabelLienSite->setFont(font1);
        LabelLienSite->setTextFormat(Qt::RichText);
        LabelLienSite->setAlignment(Qt::AlignCenter);
        ViewScore = new QWebView(Score);
        ViewScore->setObjectName(QString::fromUtf8("ViewScore"));
        ViewScore->setGeometry(QRect(40, 210, 921, 391));
        ViewScore->setUrl(QUrl(QString::fromUtf8("about:blank")));

        retranslateUi(Score);

        QMetaObject::connectSlotsByName(Score);
    } // setupUi

    void retranslateUi(QWidget *Score)
    {
        Score->setWindowTitle(QApplication::translate("Score", "Score", 0, QApplication::UnicodeUTF8));
        LabelScore->setText(QApplication::translate("Score", "Votre Score", 0, QApplication::UnicodeUTF8));
        LabelMPM->setText(QApplication::translate("Score", "Nb de mots par min", 0, QApplication::UnicodeUTF8));
        LabelCPM->setText(QApplication::translate("Score", "Nb de car par min", 0, QApplication::UnicodeUTF8));
        LabelRang->setText(QApplication::translate("Score", "Votre Rang", 0, QApplication::UnicodeUTF8));
        LabelScoreV->setText(QApplication::translate("Score", "3000", 0, QApplication::UnicodeUTF8));
        LabelMPMV->setText(QApplication::translate("Score", "56.4", 0, QApplication::UnicodeUTF8));
        LabelCPMV->setText(QApplication::translate("Score", "334.7", 0, QApplication::UnicodeUTF8));
        LabelRangV->setText(QApplication::translate("Score", "Dieu", 0, QApplication::UnicodeUTF8));
        LabelScoreT->setText(QApplication::translate("Score", "Scores", 0, QApplication::UnicodeUTF8));
        BoutonQuitter->setText(QApplication::translate("Score", "Quitter", 0, QApplication::UnicodeUTF8));
        LabelIcone->setText(QString());
        BoutonScoresLigne->setText(QApplication::translate("Score", "SCORES EN LIGNE", 0, QApplication::UnicodeUTF8));
        LabelLienSite->setText(QApplication::translate("Score", "<html><head/><body><p><a href=\"http://bagrel.ddns.net\"><span style=\" font-style:italic; text-decoration: underline; color:#0000ff;\">bagrel.ddns.net</span></a></p></body></html>", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Score: public Ui_Score {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SCORE_H
