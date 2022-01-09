#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>

from distutils.core import setup

setup(name='weather',
      version='1.0',
      description="CLI tool to get weather of a location using OpenWeatherAPI.",
      author='Aryan Sinha',
      author_email='sinha.aryan03@gmail.com',
      url='https://github.com/techyminati/weather',
      packages=['weatherapp'],
      scripts=['weather']
)
