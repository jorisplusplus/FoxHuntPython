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

questionsDiff = ["""Electromagnetics II (hard):
Consider the time-harmonic electric field component of a uniform plane wave, given by E=E0sin(ωt−k0x+ϕ)azV/m
Give an expression for the corresponding magnetic field component.
  A: H=−Z−10E0cos(ωt−k0x+ϕ)ayA/m
  B: H=−Z−10E0sin(ωt−k0x+ϕ)ayA/m
  C: H=−Z0E0sin(ωt−k0x+ϕ)ayA/m
  D: the specified electric field is not consistent with Maxwell’s equations""",

"""Mathematics II(hard):
Random variableXis uniform(−1,3) distributed.  Furthermore, letY=X2. For 1≤y≤9, the probability P(Y≤y) is given by
  A:12√y
  B:12(√y−1)
  C:14(√y−1)
  D:14(√y+ 1)""",

"""Electronic Circuits II(hard):
Calculate the effective capacitance and give the connections of the Miller capacitance. The Miller capacitance is 10uF and the gain of the MOSFET is 10x.
  A:Gate-Drain,110uF
  B:Source-Drain,110uF
  C:Gate-Drain,11uF
  D:Source-Drain,100uF""",

"""Control Systems(hard):
Consider a feedback control scheme , where G(s) =1s2+ 8s+ 7.A. Consider the controller D(s) = 1s(s+ 10).Compute the steady-state tracking error of the resulting closed loop system for a parabolic input.  Hint: use the final value theorem.
  A:55
  B:20
  C:70
  D:2]""",

"""Electromechanics(hard):
A series dc motor that can be treated as magnetically linear is operating at 1200 rpm with
Vt = 250 V and Ia = 50 A. It is known that Ra + Rs = 0.2 Ω. If torque is increased until the speed is reduced to 750 rpm while Vt remains constant in value, determine the new value for Td.
  A:180.11Nm
  B:259.20Nm
  C:161.61Nm
  D:233.14Nm""",

"""Wireless Components and Technlogies(hard):
Consider two celltowers 3 kilometers apart. One towers sends a message with a signals strength of 500mW at 5GHz. The antenna's have unit gain. What is the power received at the other antenna?
  A:1.00pW
  B:1.25pW
  C:2.00pW
  D.3.14pW""",

"""Computation II(hard):
Imagine that you have trained your St. Bernard, Korg, to carry all Iron Man movies on Blu-Ray DVD's instead of Batman's. Each Blu-Ray DVD contains 5e10 bytes. The alien runs at 36 km/hour, but because he is made of stone and perpetually out of shape, every 10 seconds he needs to stop and rest for 5 seconds.

What is the average datarate if Korg runs for 4000 meters? For simplicity, also take the last 5 seconds break when he reached his destination into account.
  A:2Gb/s
  B:1Gb/s
  C:3Gb/s
  D:5Gb/s""",

"""Power Electonics(hard):
Figure https://imgur.com/qU709gu shows a step-up converter.  The input voltage Vd = 30V.  The converter is controlled to give a constant output voltage Vo= 80 V.  The inductance is L= 275μH. The switching frequency is 50kHz. The load resistance is 420Ω, in what mode of operation is this converter?
  A: CCM
  B: BCM
  C: DCM
  D: None""",

"""Transmissionslines(hard):
Consider a transmissionline with lenght L. The line impedance is 25Ω and it is terminated by a 75Ω load. The frequency is 3THz. What is the reflection coefficient?
  A:1
  B:0.5
  C:0
  D:π""",

"""Thor(hard):
In the Marvel movies, what is the name of the guy with the red suit powered by a miniaturized Arc Reactor?
  A: Captain America
  B: Thor
  C: Iron Man
  D: The Hulk"""]





answerEasy = ["B", "B", "A", "A", "C", "B", "D", "C", "C", "D"]
answerDiff = ["B", "D", "A", "C", "D", "B", "A", "C", "B", "D"]
codes = ["forecast", "neighbour", "pledge", "drawing", "attitude", "proclaim", "judgment", "mother", "forestry", "disorder"]

routes = list()
currentRoute = 0
maxRoutes = 0

def initRoute():
    global currentRoute
    global maxRoutes
    global routes
    file = open("routes.txt", "r")
    for line in file:
        points = line.split(",")
        routes.append(list(map(int, points)))
        maxRoutes += 1

def getRoute():
    global currentRoute
    global maxRoutes
    global routes
    route = routes[currentRoute]
    currentRoute += 1
    if currentRoute == maxRoutes:
        currentRoute = 0
    return route

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
    return codes[checkpoint].lower() == code.lower()
