#!/usr/bin/env python
#coding: utf-8

import pyttsx

engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()