# DK-01
# Main Board Engineering Specification

Document ID:
DK01-004

Revision:
A

Version:
1.0 Draft

Board ID:
MB-01

PCB Name:
DK01_MainBoard

Target CAD:
KiCad 10.0.4

Target PCB Manufacturer:
JLCPCB
PCBWay
Screw

Status:
Engineering Draft

---

# 1. Introduction

The Main Board (MB-01) is the central electronic assembly of the DK-01 platform.

Every electronic subsystem is connected directly or indirectly to this board.

The Main Board is responsible for:

• System processing

• Battery charging

• Battery management

• Power distribution

• Display interface

• Wireless communication

• Audio

• Haptic feedback

• External modules

• Diagnostics

This PCB shall never contain application-specific mechanics.

Its purpose is to become a reusable embedded platform.

---

# 2. Mechanical Specification

Board Shape

Regular Hexagon

Nominal Diameter

100.00 mm

Tolerance

±0.10 mm

Thickness

1.60 mm

Layers

4

Material

FR4 TG170

Surface Finish

ENIG

Copper

1 oz

Board Color

Black

Silkscreen

White

Via Finish

Filled only when required.

---

# 3. Coordinate System

The PCB coordinate system shall follow KiCad conventions.

Origin:

Board geometric center.

Positive X

Right.

Positive Y

Top.

Rotation

Clockwise.

Every component shall have documented coordinates.

Future revisions shall never move critical connectors without revision approval.

---

# 4. Functional Zones

To simplify routing and maintenance the PCB is divided into functional regions.

Zone A

Display Interface

Zone B

Processing

Zone C

Power Management

Zone D

Battery Interface

Zone E

Audio

Zone F

USB

Zone G

Expansion Connectors

Zone H

Debug

Each zone shall remain electrically isolated whenever possible.

---

# 5. Placement Philosophy

Large components shall be placed first.

Critical routing shall be completed before low-speed signals.

No connector shall obstruct another connector.

FFC connectors shall always remain accessible after assembly.

Passive components shall be placed close to their respective IC.

Decoupling capacitors shall be placed within 3 mm of power pins whenever possible.

---

# 6. Main Controller Region

Reference

U1

Component

ESP32-S3-WROOM-1-N16R16

Placement

Board Center

Reason

Shortest routing distance to:

Display

USB

Power

Audio

Expansion

Future RF modules

The antenna region shall point toward one edge of the PCB.

No copper shall exist below the antenna.

No vias shall exist below the antenna.

No ground pour shall exist below the antenna.

---

# 7. Display Connector Region

Reference

J1

Type

FFC

Pitch

0.5 mm

Pins

50

Orientation

Top Entry

Position

Upper Edge

Reason

Shortest cable to display board.

Routing rules

RGB signals shall remain grouped.

Ground shall surround RGB buses.

Series resistors shall remain within 10 mm of ESP32.

---

# 8. USB Region

Reference

J2

Connector

USB Type-C

Mechanical reinforcement

Required.

ESD protection

Mandatory.

VBUS fuse

Mandatory.

CC resistors

Mandatory.

USB traces

90 Ω differential impedance.

Maximum skew

50 mil.

No stubs allowed.

---

# 9. Battery Region

Reference

J3

Connector

JST-PH

2 pins

Mechanical lock

Required.

Battery cable shall never cross RF region.

---

# 10. Charger Region

Reference

U2

Component

BQ25895

Placement

Near USB connector.

Reasons

Reduce current path.

Improve thermal dissipation.

Minimize voltage drop.

Copper area

Minimum 400 mm².

Thermal vias

Required.

---

# 11. Power Conversion Region

Contains

Buck

Boost

Filters

Power monitoring

All inductors shall remain grouped.

High current loops shall remain below 25 mm.

Ground return shall be continuous.
