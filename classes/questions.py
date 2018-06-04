#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
questionsEasy = ["""Computation I (easy):
A CPU runs at 2 GHz with a CPI of 1.5. If a program runs for 15 seconds, how many instructions are then executed?
  A: 10*10^9
  B: 20*10^9
  C: 10*10^6
  D: 20*10^6""",

"""Mathematics I (easy):
The limit lim(x,y)->(1,1) (x^(2)*y-x*y^(2))/(x^(2)-y^(2))
  A: has value 0
  B: has value 1/2
  C: has value 1
  D: does not exist""",

"""USE (easy):
What engineering intervention was part motorist advocates' vision?
  A: Fast lanes for motorized vehicles
  B: New traffic laws
  C: Driving tests and licenses for motorists
  D: Educational campaigns for pedestrians and cyclists""",

"""Signals (easy):
What is the frequency of 3*sin(7*pi*t+3/8*pi)?
  A: 3.5 Hz
  B: 3.5 MHz
  C: 7 Hz
  D: 7 MHz""",

"""Circuits (easy):
What is the total capacitance when two capacitors with a capacitance of 100uF are placed in parallel?
  A: 50uF
  B: 100uF
  C: 200uF
  D: 400uF""",

"""Electronic circuits I (easy):
What formula is used to calculate the base current of a transistor?
  A: Ibase = (Vbase-emitter - Vbasebias)/Rbase
  B: Ibase = (Vbasebias - Vbase-emitter)/Rbase
  C: Ibase = Rbase/(Vbase-emitter - Vbasebias)
  D: Ibase = Rbase/(Vbasebias - Vbase-emitter)""",

"""Calculus (easy):
What is the function of the tangent line of x^(3)+2x at x = 5?
  A: 2x
  B: x
  C: 36x - 125
  D: 77x - 250""",

"""Engineering Design (easy):
When does the Engineering Design robot usually break?
  A: 3 days before the demo
  B: 1 day before the demo
  C: On the day of the demo
  D: It didn't break""",

"""Physics (easy):
How long does it take for a rock to hit the ground if it rolls off a cliff that is 30m high with a starting vertical velocity of 0m/s?
  A: 1.98432664372s
  B: 2.03285746782s
  C: 2.47309683415s
  D: 3.23428983287s""",

"""Electromagnetics I (easy):
What is the general expression for the lorentz force that is exerted by an electromagnetic field on a particle?
  A: F = qE + qv + B
  B: F = qE * qv * B
  C: F = qE * qv + B
  D: F = qE + qv * B"""]
questionsDiff = []
answerEasy = ["B", "B", "A", "A", "C", "B", "D", "C", "C", "D"]
answerDiff = []
codes = ["forecast", "neighbour", "pledge", "drawing", "attitude", "proclaim", "judgment", "mother", "forestry", "disorder"]

def getQuestion(checkpoint, diff):
    if diff:
        return questionsDiff[checkpoint]
    else:
        return questionsEasy[checkpoint]

def checkAnswer(checkpoint, diff, answer):
    if diff:
        return answer == answerDiff[checkpoint]
    else:
        return answer == answerEasy[checkpoint]

def checkCode(checkpoint, code):
    return codes[checkpoint] == code
