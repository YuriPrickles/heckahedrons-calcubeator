import math
import os
import random
import sys
import mysql.connector
import csv

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QFileDialog

)
from PyQt6.QtCore import QByteArray
from main_window_ui import Ui_MainWindow
from monster_select_ui import Ui_Dialog
from mainMenu import Ui_MainMenu
from stickerLoad import Ui_StickerLoad
from cstatm import CustomStatMaker

wirral = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="MerLine",
    password="MagikrabsGauntlet",
    database="wirral",
    allow_local_infile=True
)
mycursor = wirral.cursor(prepared=True)


def newLeaf():
    directory = os.getcwd().replace("\\","/") + "/cbCSVs/"
    nameArray = [("Stickers","sticker"),
                 ("Monsters","monster"),
                 ("Tags","tag"),
                 ("stickerTag","sticker_has_tag"),
                 ("monsterTag","monster_has_tag"),
                 ("Characters","characterBattler")
                 ]
    awesomeCursor = wirral.cursor(prepared=True)
    awesomeCursor.execute("DELETE FROM sticker_has_tag WHERE sticker_stickerID > -1")
    awesomeCursor.execute("DELETE FROM monster_has_tag WHERE monster_monsterID > -1")
    awesomeCursor.execute("DELETE FROM tag WHERE tagID > -1")
    awesomeCursor.execute("DELETE FROM sticker WHERE stickerID > -1")
    awesomeCursor.execute("DELETE FROM monster WHERE monsterID > -2")
    awesomeCursor.execute("DELETE FROM characterBattler WHERE characterID > -1")
    awesomeCursor.execute("ALTER TABLE tag auto_increment = 0")
    awesomeCursor.execute("ALTER TABLE sticker auto_increment = 0")
    awesomeCursor.execute("ALTER TABLE characterBattler auto_increment = 0")
    wirral.commit()
    with open(directory + 'Tags.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO tag (tagName) VALUES ( %s )"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()
    with open(directory + 'Monsters.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO monster VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s )"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()
    with open(directory + 'Stickers.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO sticker VALUES ( %s , %s , %s , %s , %s , %s , %s , %s)"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()
    with open(directory + 'stickerTag.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO sticker_has_tag VALUES ( %s , %s )"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()
    with open(directory + 'monsterTag.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO monster_has_tag VALUES ( %s , %s )"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()
    with open(directory + 'Characters.csv', "r") as dataFile:
        read = csv.reader(dataFile)
        header = read.__next__()
        for row in read:
            print(row)
            sql = "INSERT INTO characterBattler VALUES ( %s , %s , %s , %s , %s , %s , %s , %s)"
            wirral.cursor(prepared=True).execute(sql,row)
    print("hi")
    wirral.commit()

    awesomeCursor.execute("SELECT * FROM tag")
    res = awesomeCursor.fetchall()
    for k in res:
        print(k[0] + "hi")

def checkTypeAdv(attacker, defender) -> int:
    advantage = 0
    disadvantage = 0
    match attacker:
        case "Beast":
            match defender:
                case "Glass":
                    advantage += 1
        case "Air":
            match defender:
                case "Fire":
                    advantage += 1
                case "Plant":
                    advantage += 1
                case "Glass":
                    advantage += 1
                case "Astral":
                    disadvantage += 1
                case "Lightning":
                    disadvantage += 1
        case "Astral":
            match defender:
                case "Air":
                    advantage += 1
                case "Fire":
                    advantage += 1
                case "Earth":
                    advantage += 1
                case "Water":
                    advantage += 1
                case "Astral":
                    disadvantage += 1
        case "Earth":
            match defender:
                case "Fire":
                    advantage += 1
                case "Lightning":
                    advantage += 1
                case "Plastic":
                    advantage += 1
                case "Astral":
                    disadvantage += 1
        case "Fire":
            match defender:
                case "Metal":
                    advantage += 1
                case "Plant":
                    advantage += 1
                case "Poison":
                    advantage += 1
                case "Air":
                    disadvantage += 1
                case "Astral":
                    disadvantage += 1
                case "Water":
                    disadvantage += 1
        case "Ice":
            match defender:
                case "Air":
                    advantage += 1
                case "Lightning":
                    disadvantage += 1
        case "Lightning":
            match defender:
                case "Air":
                    advantage += 1
                case "Ice":
                    advantage += 1
                case "Metal":
                    advantage += 1
                case "Water":
                    advantage += 1
                case "Plastic":
                    disadvantage += 1
        case "Metal":
            match defender:
                case "Astral":
                    advantage += 1
                case "Earth":
                    advantage += 1
                case "Ice":
                    advantage += 1
                case "Glass":
                    advantage += 1
                case "Lightning":
                    disadvantage += 1
        case "Plant":
            match defender:
                case "Earth":
                    advantage += 1
                case "Lightning":
                    advantage += 1
                case "Water":
                    advantage += 1
                case "Fire":
                    disadvantage += 1
                case "Poison":
                    disadvantage += 1
        case "Plastic":
            match defender:
                case "Astral":
                    advantage += 1
                case "Lightning":
                    advantage += 1
                case "Fire":
                    disadvantage += 1
        case "Poison":
            match defender:
                case "Astral":
                    advantage += 1
                case "Plant":
                    advantage += 1
                case "Earth":
                    disadvantage += 1
                case "Fire":
                    disadvantage += 1
                case "Metal":
                    disadvantage += 1
        case "Water":
            match defender:
                case "Earth":
                    advantage += 1
                case "Fire":
                    advantage += 1
                case "Plant":
                    advantage += 1
                case "Astral":
                    disadvantage += 1
                case "Ice":
                    disadvantage += 1
                case "Lightning":
                    disadvantage += 1
                case "Plant":
                    disadvantage += 1
        case "Glass":
            match defender:
                case "Lightning":
                    advantage += 1
    return advantage - disadvantage

def getTypeIndex(mtype,noTypeless=False):
    typeArr = ["Typeless","Beast","Air","Astral","Earth","Fire","Ice","Lightning","Metal","Plant","Plastic","Poison","Water","Glass","Glitter"]
    index = typeArr.index(mtype)
    if noTypeless:
        index -= 1
    return index

def typeTagToCheck(currentType):
    currentType = str(currentType).lower()
    match currentType:
        case "beast": return 20
        case "air": return 2
        case "astral": return 15
        case "earth": return 169
        case "fire": return 72
        case "ice": return 172
        case "lightning": return 171
        case "metal": return 103
        case "plant": return 117
        case "plastic": return 170
        case "poison": return 118
        case "water": return 165
        case "glass": return 79
        case "glitter": return 81
    return 20
class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dCalcButton.clicked.connect(self.loadDMGCalc)
        self.sLoadoutButton.clicked.connect(self.loadStickerLoadout)
        self.actionCreate_Reset_Local_Database.triggered.connect(newLeaf)
        uic.loadUi("ui/mainMenu.ui")

    def loadDMGCalc(self):
        self.dmgCalc = Window()
        self.dmgCalc.show()
        pass
    def loadStickerLoadout(self):
        self.party = Party()
        self.party.show()
        pass
class Party(QMainWindow, Ui_StickerLoad):
    tabSelected = 0
    updating = False
    listArray = []
    forceNaturalType = True
    tabHasBeenInitialized = [False, False, False, False, False, False]
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        objNamesIgnore = ["mct_1","mct_2","mct_3","mct_4","mct_5","mct_6"]
        for w in self.findChildren(QtWidgets.QComboBox):
            if not objNamesIgnore.__contains__(w.objectName()):
                w.setEditable(True)
        uic.loadUi("ui/stickerLoadout.ui")
        self.tabSelected = self.tabWidget.currentIndex()
        self.tabWidget.currentChanged.connect(self.tabChange)
        self.actionSecrets.checkableChanged.connect(self.updateMonsterList)
        self.actionUnique_Monsters.checkableChanged.connect(self.updateMonsterList)
        self.actionPost_Game.checkableChanged.connect(self.updateMonsterList)
        self.actionPier_Of_The_Unknown_DLC.checkableChanged.connect(self.updateMonsterList)
        self.actionSunshine_Update.checkableChanged.connect(self.updateMonsterList)
        self.mcb_1.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_1.currentIndexChanged.connect(self.changeStickers)
        self.mct_1.currentIndexChanged.connect(self.changeStickers)
        self.mcb_2.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_2.currentIndexChanged.connect(self.changeStickers)
        self.mct_2.currentIndexChanged.connect(self.changeStickers)
        self.mcb_3.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_3.currentIndexChanged.connect(self.changeStickers)
        self.mct_3.currentIndexChanged.connect(self.changeStickers)
        self.mcb_4.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_4.currentIndexChanged.connect(self.changeStickers)
        self.mct_4.currentIndexChanged.connect(self.changeStickers)
        self.mcb_5.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_5.currentIndexChanged.connect(self.changeStickers)
        self.mct_5.currentIndexChanged.connect(self.changeStickers)
        self.mcb_6.currentIndexChanged.connect(self.setForceNaturalType)
        self.mcb_6.currentIndexChanged.connect(self.changeStickers)
        self.mct_6.currentIndexChanged.connect(self.changeStickers)

        self.actionExport_Party.triggered.connect(self.saveParty)
        self.actionImport_Party.triggered.connect(self.importParty)

        self.updateMonsterList()
        self.changeStickers()
    def setForceNaturalType(self):
        self.forceNaturalType = True
    def createSaveFile(self) -> str:
        text = ""
        finalTextArray = []
        for i in range(6):
            textArray = []
            for w in self.findChildren(QtWidgets.QComboBox):
                if str(w.objectName()).__contains__(f"_{i+1}"):
                    textArray.append(w.currentText())
            textArray[1] = "Beast" if textArray[1] == "" else textArray[1]
            text +=(f"Tape {i+1}\n"
                    f"-------------\n"
                    f"{textArray[0]} ({textArray[1]})\n\n"
                    f"Stickers:\n")
            for stickerIndex in range(8):
                text += f"{textArray[stickerIndex+2]}\n"
            text += "\n\n"
            finalTextArray += textArray
        text = str(finalTextArray) + ("\n\nHeads up!"
                                      "\nThis single line above contains the information"
                                      "\nthat will be used to reimport your party into the editor."
                                      "\n\nI advise that you do not edit it"
                                      "\nif you don't know what you're doing.\n\n\n") + text
        return text

    def saveParty(self):
        fname = QFileDialog.getSaveFileName(
            self,
            "Save Party","My Party.txt","Text files (*.txt)"
        )
        if fname[0] == '': return
        file = open(fname[0], 'w')
        file.write(self.createSaveFile())
        file.close()
    def importParty(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Import Party",
            "", "Text files (*.txt)"
        )
        if fname[0] == '': return
        file = open(fname[0],"r")
        importData = eval(file.readline())
        tabSelSave = self.tabSelected
        for i in range(6):
            cbIndex = 0
            self.tabSelected = i
            self.updateMonsterList()
            self.changeStickers()
            self.tabHasBeenInitialized[self.tabSelected] = True
            for w in self.findChildren(QtWidgets.QComboBox):
                if (str(w.objectName()).__contains__(f"_{i+1}")
                and not str(w.objectName()).__contains__(f"m_{i+1}")):
                    w.setCurrentIndex(w.findText(importData[cbIndex + (i * 10)]))
                    cbIndex += 1
            print(i)
            stickerIndex = 2
            for w in self.findChildren(QtWidgets.QComboBox):
                if str(w.objectName()).__contains__(f"m_{i+1}"):
                    print(stickerIndex)
                    print(importData[stickerIndex + (i * 10)])
                    w.setCurrentIndex(w.findText(importData[stickerIndex + (i * 10)]))
                    stickerIndex += 1
        file.close()
        self.tabSelected = tabSelSave


    def updateMonsterList(self):

        baseStatement = "SELECT name, monsterID FROM monster WHERE monsterID > -1 and monsterID not between 132 and 151"
        mycursor.execute(baseStatement + self.spoilerAvoider())
        items = mycursor.fetchall()
        self.listArray.clear()
        self.mcb_1.clear()
        self.mcb_2.clear()
        self.mcb_3.clear()
        self.mcb_4.clear()
        self.mcb_5.clear()
        self.mcb_6.clear()
        for i in items:
            self.listArray.append(i[0])
            self.mcb_1.addItem(i[0],i[1])
            self.mcb_2.addItem(i[0],i[1])
            self.mcb_3.addItem(i[0],i[1])
            self.mcb_4.addItem(i[0],i[1])
            self.mcb_5.addItem(i[0],i[1])
            self.mcb_6.addItem(i[0],i[1])
        self.mcb_1.repaint()
        self.mcb_2.repaint()
        self.mcb_3.repaint()
        self.mcb_4.repaint()
        self.mcb_5.repaint()
        self.mcb_6.repaint()
    def tabChange(self):
        self.tabSelected = self.tabWidget.currentIndex()
        print(self.tabSelected)
        self.updating = True
        self.updateMonsterList()
        self.updating = False
        if not self.tabHasBeenInitialized[self.tabSelected]:
            self.forceNaturalType = True
            self.changeStickers()
            self.tabHasBeenInitialized[self.tabSelected] = True
    def spoilerAvoider(self) -> str:
        spoiler = ""
        if not self.actionSecrets.isChecked():
            spoiler += " and monsterID != 0"
        if not self.actionUnique_Monsters.isChecked():
            spoiler += " and monsterID != 110 and monsterID != 111 and monsterID != 117 and monsterID != 118 and monsterID != 119 and monsterID != 128"
        if not self.actionPost_Game.isChecked():
            spoiler += " and monsterID != 120"
        if not self.actionPier_Of_The_Unknown_DLC.isChecked():
            spoiler += " and monsterID not between 152 and 163"
        if not self.actionSunshine_Update.isChecked():
            spoiler += " and monsterID not between 129 and 131"
        return spoiler
    def changeStickers(self):
        if self.updating: return
        match self.tabSelected:
            case 0:
                monsterID = self.mcb_1.currentData()
                if not self.listArray.__contains__(self.mcb_1.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_1.itemData(self.mcb_1.findText("Traffikrab"))
                    self.mcb_1.setCurrentIndex(self.mcb_1.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_1.setText(labelText)
                if self.forceNaturalType:
                    self.mct_1.setCurrentIndex(getTypeIndex(mInfo[3],True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ", (monsterID,))
                monsterTags = mycursor.fetchall()
                print(monsterTags)
                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_1.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_1.clear()
                self.c2_m_1.clear()
                self.c3_m_1.clear()
                self.c4_m_1.clear()
                self.c5_m_1.clear()
                self.c6_m_1.clear()
                self.c7_m_1.clear()
                self.c8_m_1.clear()
                print(stickerIDs)
                print(stickers)
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_1.currentIndex() != -1):
                        continue
                    self.c1_m_1.addItem(j[0],j[1])
                    self.c2_m_1.addItem(j[0],j[1])
                    self.c3_m_1.addItem(j[0],j[1])
                    self.c4_m_1.addItem(j[0],j[1])
                    self.c5_m_1.addItem(j[0],j[1])
                    self.c6_m_1.addItem(j[0],j[1])
                    self.c7_m_1.addItem(j[0],j[1])
                    self.c8_m_1.addItem(j[0],j[1])
                self.c1_m_1.setCurrentIndex(-1)
                self.c2_m_1.setCurrentIndex(-1)
                self.c3_m_1.setCurrentIndex(-1)
                self.c4_m_1.setCurrentIndex(-1)
                self.c5_m_1.setCurrentIndex(-1)
                self.c6_m_1.setCurrentIndex(-1)
                self.c7_m_1.setCurrentIndex(-1)
                self.c8_m_1.setCurrentIndex(-1)
            case 1:
                monsterID = self.mcb_2.currentData()
                if not self.listArray.__contains__(self.mcb_2.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_2.itemData(self.mcb_2.findText("Traffikrab"))
                    self.mcb_2.setCurrentIndex(self.mcb_2.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_2.setText(labelText)
                if self.forceNaturalType:
                    self.mct_2.setCurrentIndex(getTypeIndex(mInfo[3], True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ",(monsterID,))
                monsterTags = mycursor.fetchall()

                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_2.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_2.clear()
                self.c2_m_2.clear()
                self.c3_m_2.clear()
                self.c4_m_2.clear()
                self.c5_m_2.clear()
                self.c6_m_2.clear()
                self.c7_m_2.clear()
                self.c8_m_2.clear()
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_2.currentIndex() != -1):
                        continue
                    self.c1_m_2.addItem(j[0], j[1])
                    self.c2_m_2.addItem(j[0], j[1])
                    self.c3_m_2.addItem(j[0], j[1])
                    self.c4_m_2.addItem(j[0], j[1])
                    self.c5_m_2.addItem(j[0], j[1])
                    self.c6_m_2.addItem(j[0], j[1])
                    self.c7_m_2.addItem(j[0], j[1])
                    self.c8_m_2.addItem(j[0], j[1])
                self.c1_m_2.setCurrentIndex(-1)
                self.c2_m_2.setCurrentIndex(-1)
                self.c3_m_2.setCurrentIndex(-1)
                self.c4_m_2.setCurrentIndex(-1)
                self.c5_m_2.setCurrentIndex(-1)
                self.c6_m_2.setCurrentIndex(-1)
                self.c7_m_2.setCurrentIndex(-1)
                self.c8_m_2.setCurrentIndex(-1)
            case 2:
                monsterID = self.mcb_3.currentData()
                if not self.listArray.__contains__(self.mcb_3.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_3.itemData(self.mcb_3.findText("Traffikrab"))
                    self.mcb_3.setCurrentIndex(self.mcb_3.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_3.setText(labelText)
                if self.forceNaturalType:
                    self.mct_3.setCurrentIndex(getTypeIndex(mInfo[3],True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ",(monsterID,))
                monsterTags = mycursor.fetchall()

                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_3.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_3.clear()
                self.c2_m_3.clear()
                self.c3_m_3.clear()
                self.c4_m_3.clear()
                self.c5_m_3.clear()
                self.c6_m_3.clear()
                self.c7_m_3.clear()
                self.c8_m_3.clear()
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_3.currentIndex() != -1):
                        continue
                    self.c1_m_3.addItem(j[0],j[1])
                    self.c2_m_3.addItem(j[0],j[1])
                    self.c3_m_3.addItem(j[0],j[1])
                    self.c4_m_3.addItem(j[0],j[1])
                    self.c5_m_3.addItem(j[0],j[1])
                    self.c6_m_3.addItem(j[0],j[1])
                    self.c7_m_3.addItem(j[0],j[1])
                    self.c8_m_3.addItem(j[0],j[1])
                self.c1_m_3.setCurrentIndex(-1)
                self.c2_m_3.setCurrentIndex(-1)
                self.c3_m_3.setCurrentIndex(-1)
                self.c4_m_3.setCurrentIndex(-1)
                self.c5_m_3.setCurrentIndex(-1)
                self.c6_m_3.setCurrentIndex(-1)
                self.c7_m_3.setCurrentIndex(-1)
                self.c8_m_3.setCurrentIndex(-1)
            case 3:
                monsterID = self.mcb_4.currentData()
                if not self.listArray.__contains__(self.mcb_4.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_4.itemData(self.mcb_4.findText("Traffikrab"))
                    self.mcb_4.setCurrentIndex(self.mcb_4.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_4.setText(labelText)
                if self.forceNaturalType:
                    self.mct_4.setCurrentIndex(getTypeIndex(mInfo[3],True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ",(monsterID,))
                monsterTags = mycursor.fetchall()

                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_4.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_4.clear()
                self.c2_m_4.clear()
                self.c3_m_4.clear()
                self.c4_m_4.clear()
                self.c5_m_4.clear()
                self.c6_m_4.clear()
                self.c7_m_4.clear()
                self.c8_m_4.clear()
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_4.currentIndex() != -1):
                        continue
                    self.c1_m_4.addItem(j[0],j[1])
                    self.c2_m_4.addItem(j[0],j[1])
                    self.c3_m_4.addItem(j[0],j[1])
                    self.c4_m_4.addItem(j[0],j[1])
                    self.c5_m_4.addItem(j[0],j[1])
                    self.c6_m_4.addItem(j[0],j[1])
                    self.c7_m_4.addItem(j[0],j[1])
                    self.c8_m_4.addItem(j[0],j[1])
                self.c1_m_4.setCurrentIndex(-1)
                self.c2_m_4.setCurrentIndex(-1)
                self.c3_m_4.setCurrentIndex(-1)
                self.c4_m_4.setCurrentIndex(-1)
                self.c5_m_4.setCurrentIndex(-1)
                self.c6_m_4.setCurrentIndex(-1)
                self.c7_m_4.setCurrentIndex(-1)
                self.c8_m_4.setCurrentIndex(-1)
            case 4:
                monsterID = self.mcb_5.currentData()
                if not self.listArray.__contains__(self.mcb_5.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_5.itemData(self.mcb_5.findText("Traffikrab"))
                    self.mcb_5.setCurrentIndex(self.mcb_5.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_5.setText(labelText)
                if self.forceNaturalType:
                    self.mct_5.setCurrentIndex(getTypeIndex(mInfo[3],True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ",(monsterID,))
                monsterTags = mycursor.fetchall()

                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_5.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_5.clear()
                self.c2_m_5.clear()
                self.c3_m_5.clear()
                self.c4_m_5.clear()
                self.c5_m_5.clear()
                self.c6_m_5.clear()
                self.c7_m_5.clear()
                self.c8_m_5.clear()
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_5.currentIndex() != -1):
                        continue
                    self.c1_m_5.addItem(j[0],j[1])
                    self.c2_m_5.addItem(j[0],j[1])
                    self.c3_m_5.addItem(j[0],j[1])
                    self.c4_m_5.addItem(j[0],j[1])
                    self.c5_m_5.addItem(j[0],j[1])
                    self.c6_m_5.addItem(j[0],j[1])
                    self.c7_m_5.addItem(j[0],j[1])
                    self.c8_m_5.addItem(j[0],j[1])
                self.c1_m_5.setCurrentIndex(-1)
                self.c2_m_5.setCurrentIndex(-1)
                self.c3_m_5.setCurrentIndex(-1)
                self.c4_m_5.setCurrentIndex(-1)
                self.c5_m_5.setCurrentIndex(-1)
                self.c6_m_5.setCurrentIndex(-1)
                self.c7_m_5.setCurrentIndex(-1)
                self.c8_m_5.setCurrentIndex(-1)
            case 5:
                monsterID = self.mcb_6.currentData()
                if not self.listArray.__contains__(self.mcb_6.currentText()):
                    print("Emergency Traffikrab!")
                    monsterID = self.mcb_6.itemData(self.mcb_6.findText("Traffikrab"))
                    self.mcb_6.setCurrentIndex(self.mcb_6.findText("Traffikrab"))
                mycursor.execute(f"SELECT * FROM monster WHERE monsterID = %s ",(monsterID,))
                mInfo = mycursor.fetchone()
                labelText = (f"Natural Type : {mInfo[3]}\n"
                             f"Max HP       : {mInfo[4]}\n"
                             f"Melee ATK    : {mInfo[5]}\n"
                             f"Melee DEF    : {mInfo[6]}\n"
                             f"Ranged ATK   : {mInfo[7]}\n"
                             f"Ranged DEF   : {mInfo[8]}\n"
                             f"Speed        : {mInfo[9]}\n")
                self.m_info_6.setText(labelText)
                if self.forceNaturalType:
                    self.mct_6.setCurrentIndex(getTypeIndex(mInfo[3],True))
                    self.forceNaturalType = False
                mycursor.execute(f"SELECT tag_tagID FROM monster_has_tag WHERE monster_monsterID = %s ",(monsterID,))
                monsterTags = mycursor.fetchall()

                stickerIDs = []
                for k in monsterTags:
                    mycursor.execute(f"SELECT sticker_stickerID FROM sticker_has_tag WHERE tag_tagID = %s or tag_tagID = 168 or tag_tagID = %s ", (k[0],typeTagToCheck(self.mct_6.currentText())))
                    temp = mycursor.fetchall()
                    for p in temp:
                        stickerIDs.append(p[0])
                mycursor.execute("SELECT name, stickerID, type FROM sticker")
                stickers = mycursor.fetchall()
                self.c1_m_6.clear()
                self.c2_m_6.clear()
                self.c3_m_6.clear()
                self.c4_m_6.clear()
                self.c5_m_6.clear()
                self.c6_m_6.clear()
                self.c7_m_6.clear()
                self.c8_m_6.clear()
                for j in stickers:
                    if (not stickerIDs.__contains__(j[1])
                            and not self.actionAll_Stickers_Compatible.isChecked()
                            and self.mcb_6.currentIndex() != -1):
                        continue
                    self.c1_m_6.addItem(j[0],j[1])
                    self.c2_m_6.addItem(j[0],j[1])
                    self.c3_m_6.addItem(j[0],j[1])
                    self.c4_m_6.addItem(j[0],j[1])
                    self.c5_m_6.addItem(j[0],j[1])
                    self.c6_m_6.addItem(j[0],j[1])
                    self.c7_m_6.addItem(j[0],j[1])
                    self.c8_m_6.addItem(j[0],j[1])
                self.c1_m_6.setCurrentIndex(-1)
                self.c2_m_6.setCurrentIndex(-1)
                self.c3_m_6.setCurrentIndex(-1)
                self.c4_m_6.setCurrentIndex(-1)
                self.c5_m_6.setCurrentIndex(-1)
                self.c6_m_6.setCurrentIndex(-1)
                self.c7_m_6.setCurrentIndex(-1)
                self.c8_m_6.setCurrentIndex(-1)


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        uic.loadUi("ui/DamageCalcCB.ui")
        self.setAttacker.triggered.connect(self.setAttackerFunc)
        self.setDefender.triggered.connect(self.setDefenderFunc)
        self.presetBattler_ATK.triggered.connect(self.setATKChar)
        self.presetBattler_DEF.triggered.connect(self.setDEFChar)
        self.customBattler_ATK.triggered.connect(self.setATKCharCustom)
        self.customBattler_DEF.triggered.connect(self.setDEFCharCustom)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.setWindowTitle("Cassette Beasts Damage Calculator")
    def setAttackerFunc(self):
        dialog = MonsterSelect("mon","Select Attacking Monster")
        dialog.exec()
        self.value_mDMG.setValue(dialog.mDMG)
        self.value_rDMG.setValue(dialog.rDMG)
        self.value_mType.setCurrentIndex(getTypeIndex(dialog.type))
    def setDefenderFunc(self):
        dialog = MonsterSelect("mon","Select Defending Monster")
        dialog.exec()
        self.value_dHP.setValue(dialog.hp)
        self.value_mdStat.setValue(dialog.mDEF)
        self.value_rdStat.setValue(dialog.rDEF)
        self.value_dType.setCurrentIndex(getTypeIndex(dialog.type))

    def setATKChar(self):
        dialog = MonsterSelect("char","Select Attacking Battler")
        dialog.exec()
        self.value_cMStat.setValue(dialog.mDMG)
        self.value_cRStat.setValue(dialog.rDMG)
    def setDEFChar(self):
        dialog = MonsterSelect("char","Select Defending Battler")
        dialog.exec()
        self.d_charHP.setValue(dialog.hp)
        self.value_mdCharStat.setValue(dialog.mDEF)
        self.value_rdCharStat.setValue(dialog.rDEF)

    def setATKCharCustom(self):
        dialog = CustomCharStatMaker()
        dialog.exec()
        self.value_cMStat.setValue(dialog.mDMG)
        self.value_cRStat.setValue(dialog.rDMG)
    def setDEFCharCustom(self):
        dialog = CustomCharStatMaker()
        dialog.exec()
        self.value_mdCharStat.setValue(dialog.mDEF)
        self.value_rdCharStat.setValue(dialog.rDEF)
        self.d_charHP.setValue(dialog.hp)

    def buttonClicked(self):
        damageValueUsed = 0
        defenseValueUsed = 0
        charDMG = 0
        defCharDEF = 0
        if self.Melee.isChecked():
            damageValueUsed = self.value_mDMG.value()
            defenseValueUsed = self.value_mdStat.value()
            charDMG = self.value_cMStat.value()
            defCharDEF = self.value_mdCharStat.value()
        else:
            damageValueUsed = self.value_rDMG.value()
            defenseValueUsed = self.value_rdStat.value()
            charDMG = self.value_cRStat.value()
            defCharDEF = self.value_rdCharStat.value()

        mStatStages_Final = (4 + self.value_mStatStages.value())/4 if self.value_mStatStages.value() >= 0 else 4/(4-self.value_mStatStages.value())
        sigBonus = 1.1 if self.SigTape.isChecked() else 1
        mGradedStat = math.floor(damageValueUsed * (1+(0.02* self.value_mGrade.value())))
        combinedStat = math.floor((charDMG * sigBonus * mGradedStat * (self.value_mLevel.value() + 33))/5000) + 5
        finalAttackerStat = math.floor(combinedStat * (((self.value_pDMG.value()/100) + 100)/100)) * mStatStages_Final

        hasResBonus = 0.5 if self.value_hasRes.isChecked() else 1
        dStatStages_Final = (4 + self.value_dStatStages.value())/4 if self.value_dStatStages.value() >= 0 else 4/(4-self.value_dStatStages.value())
        D_mGradedStat = math.floor(defenseValueUsed * (1 + 0.02 * self.value_dGrade.value()))
        D_combinedStat = math.floor((defCharDEF * D_mGradedStat * (self.value_dLevel.value() + 33)) / 5000) + 5
        finalDefenderStat = math.floor(D_combinedStat * dStatStages_Final)

        typeAdv = checkTypeAdv(self.value_mType.currentText(), self.value_dType.currentText())
        critMult = 1.5 + self.value_pCrit.value()/100 if self.value_doCrits.isChecked() else 1
        STAB_bonus = 1.2 if self.STAB.isChecked() else 1
        randomvalue = random.randint(85, 100) if not self.value_customRand.isChecked() else self.value_customRandVal.value()
        damageDealt = self.value_hits.value() * math.floor(hasResBonus * math.floor((self.value_stickerPower.value() * (finalAttackerStat/finalDefenderStat) * ((self.value_mLevel.value() + 37)/100) * (randomvalue/100) + 1) * STAB_bonus * math.pow(1.3,typeAdv) * critMult))

        damageDealt_worst = self.value_hits.value() * math.floor(hasResBonus * math.floor((self.value_stickerPower.value() * (finalAttackerStat/finalDefenderStat) * ((self.value_mLevel.value() + 37)/100) * (85/100) + 1) * STAB_bonus * math.pow(1.3,typeAdv) * critMult))
        damageDealt_best = self.value_hits.value() * math.floor(hasResBonus * math.floor((self.value_stickerPower.value() * (finalAttackerStat/finalDefenderStat) * ((self.value_mLevel.value() + 37)/100) + 1) * STAB_bonus * math.pow(1.3,typeAdv) * critMult))

        hpd_String = f"Highest possible damage: {damageDealt_best}\n"
        lpd_String = f"Lowest possible damage: {damageDealt_worst}\n"
        otherBits = "It was a Critical Hit!\n" if self.value_doCrits.isChecked() else ""
        if typeAdv > 0:
            otherBits += "The attack had a type advantage!\n"
        if typeAdv == 0:
            otherBits += "The attack had neither a type advantage or disadvantage!\n"
        if typeAdv < 0:
            otherBits += "The attack had a type disadvantage!\n"
        if self.value_hasRes.isChecked():
            otherBits += f"Defender has a Type Resistance sticker, damage is reduced by half."
        D_mHP = math.floor(self.value_dHP.value() * (1 + 0.02 * self.value_dGrade.value()))
        D_combinedHP = math.floor((self.d_charHP.value() * D_mHP * (self.value_dLevel.value() + 33)) / 5000) + 5
        HPLostPercent = round((damageDealt/D_combinedHP) * 100, 2)
        HPLostPercent_BEST = round((damageDealt_best / D_combinedHP) * 100, 2)
        HPLostPercent_WORST = round((damageDealt_worst / D_combinedHP) * 100, 2)
        print("Graded Damage: ",mGradedStat)
        print("Combined Damage: ",combinedStat)
        print("Battle Damage: ",finalAttackerStat)
        print("Graded Defense: ",D_mGradedStat)
        print("Combined Damage: ",D_combinedStat)
        print("Battle Defense: ",finalDefenderStat)
        print("Random Val: ",randomvalue)
        print("Graded HP: ",D_mHP)
        print("Combined HP: ",D_combinedHP)
        print("HP Loss Percent: ",HPLostPercent)
        if self.value_calcHP.isChecked():
            otherBits += f"The attack took away {HPLostPercent}% of the Defender's HP!\n"
            otherBits += f"Highest Possible HP Loss: {HPLostPercent_BEST}%\n"
            otherBits += f"Lowest Possible HP Loss: {HPLostPercent_WORST}%\n"
        if self.value_mType.currentText() == "Lightning" and (self.value_conductive.isChecked() or typeAdv > 0):
            otherBits += (f"Defender is Conductive and hit by a lightning attack!\n"
                          f"It takes damage equal to 8% of its Max HP! ({math.floor(D_combinedHP/8)} HP)")
        trueFinalString = (f"Your Monster dealt {damageDealt} damage!\n" +
                           hpd_String + lpd_String + otherBits)

        print('Calculating Damage...')
        print(trueFinalString)
        dialog = GetResults()
        dialog.setText(trueFinalString)
        dialog.exec()

class MonsterSelect(QDialog, Ui_Dialog):
    mode = ""
    hp = 0
    mDMG = 0
    rDMG = 0
    mDEF = 0
    rDEF = 0
    type = "Beast"
    listArray = []
    def __init__(self, funcMode="mon",windowTitle="",parent=None):
        self.mode = funcMode
        super().__init__(parent)
        print(self.mode)
        self.setupUi(self)
        self.accepted.connect(self.setData)
        uic.loadUi("ui/MonsterSelect.ui")
        if self.mode == "mon":
            mycursor.execute("SELECT name, monsterID FROM monster")
        if self.mode == "char":
            mycursor.execute("SELECT name, characterID FROM characterBattler")
        self.setWindowTitle(windowTitle)
        items = mycursor.fetchall()
        for i in items:
            self.listArray.append(i[0])
            self.comboBox.addItem(i[0],i[1])
    def setData(self):
        monsterID = self.comboBox.currentData()
        if not self.listArray.__contains__(self.comboBox.currentText()):
            print("Emergency Magikrab!")
            monsterID = 0
        colArray = ["maxhp", "matk", "mdef", "ratk", "rdef", "type"]
        if self.mode == "char": colArray.pop(5)
        dataArray = []
        for col in colArray:
            if self.mode == "mon":
                mycursor.execute(f"SELECT {col} FROM monster WHERE monsterID={monsterID}")
            if self.mode == "char":
                mycursor.execute(f"SELECT {col} FROM characterBattler WHERE characterID={monsterID}")
            for i in mycursor.fetchall():
                dataArray.append(i[0])
        print(dataArray)
        self.hp = dataArray[0]
        self.mDMG = dataArray[1]
        self.rDMG = dataArray[2]
        self.mDEF = dataArray[3]
        self.rDEF = dataArray[4]
        if self.mode == "mon":
            self.type = dataArray[5]

class CustomCharStatMaker(QDialog, CustomStatMaker):
    hp=0
    mDMG = 0
    rDMG = 0
    mDEF = 0
    rDEF = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.accepted.connect(self.setData)
        uic.loadUi("ui/CustomStatMaker.ui")
        self.setWindowTitle("Enter Custom Values")
    def setData(self):
        self.hp = self.MaxHP.value()
        self.mDMG = self.MeleeATK.value()
        self.rDMG = self.MeleeDEF.value()
        self.mDEF = self.RangedATK.value()
        self.rDEF = self.RangedDEF.value()
class GetResults(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Damage Results")


app = QtWidgets.QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()