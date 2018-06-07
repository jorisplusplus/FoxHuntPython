#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
from .questions import getQuestion, checkAnswer, checkCode, getRoute
import time

timepenalty = 120

class Group:
    def __init__(self, name):
        self.name = name
        self.diff = False
        self.paid = False
        self.admin = False
        self.order = getRoute()
        self.questionTime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.position = 0
        self.finished = False

    def getName(self):
        return self.name

    def hasPaid(self):
        return self.paid

    def isAdmin(self):
        return self.admin

    def setPaid(self):
        self.paid = True

    def setAdmin(self):
        self.admin = True

    def setDiff(self, newdiff):
        self.diff = newdiff

    def getCheckpoint(self):
        if self.finished:
            return -1
        return self.order[self.position]

    def getPosition(self):
        return self.position

    def getScore(self):
        if self.finished:
            return sum(self.questionTime)
        else:
            return 3600

    def getQuestion(self):
        self.startTime = time.time()
        return getQuestion(self.getCheckpoint(), self.diff)

    def checkAnswer(self, answer):
        if self.paid == False:
            return False
        if self.finished:
            return False
        correct = checkAnswer(self.getCheckpoint(), self.diff, answer)
        if correct:
            self.questionTime[self.position] = time.time() - self.startTime
            self.position = self.position + 1
            if self.position == 10:
                self.finished = True
        else:
            self.startTime = self.startTime - timepenalty
        return correct

    def checkCode(self, code):
        if self.paid == False:
            return False
        if self.finished:
            return False
        return checkCode(self.getCheckpoint(), code)

    def getStats(self):
        return " Name: " + self.name + " Paid: " + str(self.paid) + " DIF: " + str(self.diff) + " POS: " + str(self.position) + " CHK: " + str(self.getCheckpoint()) + "\n"
