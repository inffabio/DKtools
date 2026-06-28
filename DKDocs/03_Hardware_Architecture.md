# DK-01
# Hardware Architecture Specification

Document ID: DK01-003

Version: 1.0 Draft

Status: Draft

Project: DK-01

Target CAD: KiCad 10.0.4

Target MCU:
ESP32-S3-WROOM-1-N16R16

Related Documents

DK01-000

DK01-001

DK01-002

---

# 1. Purpose

This document defines every electronic subsystem composing the DK-01 hardware platform.

Every electronic component shall be justified by one or more system requirements.

Every subsystem shall be electrically independent whenever possible.

---

# 2. Hardware Philosophy

The hardware shall follow six principles.

## Reliability

Electrical robustness has priority over minimum cost.

The first prototype shall prioritize functionality and maintainability.

Component reduction may occur only after successful validation.

---

## Modularity

The DK-01 hardware shall be divided into replaceable electronic assemblies.

Main Board

Display Board

Door Boards

Battery Pack

Speaker Module

---

## Manufacturability

Every PCB shall be suitable for SMT automated assembly.

Preferred package sizes:

0603 passive components

0402 only when necessary.

No BGA devices shall be used.

---

## Serviceability

FFC cables shall be removable.

The display shall not be soldered directly to the Main Board.

Battery replacement shall require no soldering.

---

## Expandability

Unused GPIOs shall remain available.

Unused buses shall remain documented.

Power rails shall include expansion margin.

---

## EMC

Signal integrity shall be considered from Revision A.

Ground planes shall remain continuous.

High-speed routing shall be isolated.

USB differential pair shall be impedance controlled.

---

# 3. Hardware Modules

MB-01

Main Board

DB-01

Display Board

PB-01

Door Board

BP-01

Battery Pack

SP-01

Speaker

HP-01

Haptic Motor

---

# 4. Main Board

Responsibilities

System Controller

Power Distribution

Battery Charging

RTC

USB

Wireless

Display Interface

Audio

LED Management

Expansion Interface

Diagnostics

The Main Board shall contain all processing capability.

No application logic shall exist in secondary boards unless justified.

---

# 5. Main Board Dimensions

Geometry

Regular Hexagon

Distance between opposite faces

100 mm

Thickness

1.6 mm

Copper Layers

4

Material

FR4 TG170

Surface Finish

ENIG

Copper Weight

1 oz

---

# 6. Copper Stack

Layer 1

Components

Critical Signals

High-Speed Routing

Layer 2

Continuous GND Plane

Layer 3

Power Plane

VBAT

SYS

5V

3V3

Layer 4

Low-Speed Signals

GPIO

I²C

Configuration

---

# 7. Mechanical Placement

The PCB shall be divided into functional regions.

Top Region

Display Connector

Center

ESP32

Upper Left

RTC

Upper Right

Flash Memory

Lower Left

Battery Charger

Lower Right

Power Supply

Bottom

USB-C

Speaker Connector

Battery Connector

---

# 8. Main Processor

Reference

U1

Component

ESP32-S3-WROOM-1-N16R16

Reason for selection

Integrated Wi-Fi

Bluetooth LE

USB Native

16 MB Flash

16 MB PSRAM

Large software ecosystem

ESP-IDF support

LVGL compatibility

---

# 9. Display Interface

Dedicated FFC connector.

50 pins.

0.5 mm pitch.

Length approximately 80 mm.

Series resistors shall be placed close to the ESP32.

Backlight PWM shall have dedicated routing.

Ground reference shall surround RGB signals.

---

# 10. Power Tree

USB-C

↓

Battery Charger

↓

Battery

↓

Power Path

↓

SYS

↓

3V3 Buck

↓

ESP32

RTC

Logic

↓

5V Boost

↓

Display Backlight

LEDs

Speaker Amplifier

Future Modules

---

# 11. Battery Charger

Reference

U2

Preferred Component

BQ25895

Reasons

Power Path

Battery Protection

USB Detection

I²C Interface

Charge Current Control

Future USB PD compatibility

Alternative Components

MP2762

IP5306

MCP73871

---

# 12. 3V3 Regulator

Reference

U3

Target Current

1 A minimum

Output ripple

Below 20 mV

Efficiency

Above 90%

---

# 13. 5V Converter

Reference

U4

Purpose

RGB LEDs

Audio

Display Backlight

Peak Current

3 A

Preferred Efficiency

Above 90%

---

# 14. RTC

Reference

U5

Preferred

DS3231M

Reason

Temperature compensated oscillator

Backup support

Excellent long-term stability

---

# 15. Audio

Reference

U6

Preferred

MAX98357A

Interface

I²S

Speaker

4 Ω

1~3 W

---

# 16. Haptic Driver

Reference

U7

DRV2605L

Reasons

Programmable waveforms

LRA support

ERM support

Low software complexity

---

# 17. External Flash

Reference

U8

Optional

W25Q256JV

Purpose

Audio

Themes

Future Resources

---

# 18. Protection

Every external connector shall include:

TVS

ESD diode

Series resistor where appropriate

Ground stitching vias

USB shall receive dedicated protection.

---

# 19. RF Design

ESP32 antenna area shall remain free of copper.

No signals shall pass below antenna.

Minimum keep-out

15 mm

Ground stitching around RF section.

---

# 20. Thermal Design

Buck converter

Boost converter

Audio amplifier

Battery charger

shall include copper thermal areas.

Thermal vias shall be used whenever recommended.

---

# 21. Testability

Dedicated test points shall exist for:

VBUS

VBAT

SYS

3V3

5V

GND

EN

BOOT

TX

RX

USB

I²C

SPI

Speaker

Motor

---

# 22. Manufacturing

All polarized parts shall include silk orientation.

Reference designators shall remain visible after assembly.

No component shall obstruct programming connectors.

---

# 23. Design Margin

Power rails shall operate below 70% nominal load.

Temperature rise shall remain below 30°C over ambient.

Mechanical connectors shall support at least 500 insertion cycles.

---

# 24. Revision Policy

Every hardware modification shall update:

BOM

Schematic

PCB

Documentation

Test Plan

Manufacturing Files