# DK-01
# System Architecture Specification

**Document ID:** DK01-002

**Version:** 1.0 Draft

**Status:** Draft

**Classification:** Engineering

**Project:** DK-01 Defusal Kit

**Target Hardware:** ESP32-S3-WROOM-1-N16R16

**Target CAD:** KiCad 10.0.4

---

# 1. Purpose

This document defines the complete architecture of the DK-01.

It describes every subsystem, their responsibilities, interfaces, dependencies and communication paths.

No electronic circuit shall be developed before this architecture is approved.

---

# 2. Design Philosophy

The DK-01 is designed around a modular architecture.

Every subsystem must be replaceable without redesigning the remaining hardware.

The system shall separate:

• Power

• Processing

• Communication

• User Interface

• Game Interface

• Diagnostics

• Future Expansion

---

# 3. High Level Architecture

                        USER

                          │

              ┌───────────┴───────────┐

              │                       │

          DISPLAY                 LEDS / AUDIO

              │                       │

              └───────────┬───────────┘

                          │

                  MAIN CONTROLLER

                 ESP32-S3-WROOM

                          │

        ┌─────────────────┼─────────────────┐

        │                 │                 │

     POWER            GAME PORTS        DEBUG

        │                 │                 │

   BATTERY USB-C      12 MODULES       USB SERIAL

---

# 4. Hardware Subsystems

The system is divided into independent hardware modules.

MB-01 Main Board

DB-01 Display Board

PB-01 Port Board

BP-01 Battery Pack

SP-01 Speaker Module

HP-01 Haptic Module

---

# 5. Main Board Responsibilities

The Main Board is responsible for:

Central Processing

Power Management

Battery Charging

RTC

Display Control

Audio Playback

Vibration

Game Logic

OTA Update

USB Communication

Diagnostics

Configuration Storage

---

# 6. Display Board Responsibilities

The Display Board contains:

Display

FFC Connector

Backlight Driver

Mechanical Mount

ESD Protection

It shall contain no application logic.

---

# 7. Port Board Responsibilities

Each Port Board shall contain:

Three RGB LEDs

Three pogo contacts

Protection devices

Mechanical fixation

Connection to Main Board

Optional identification circuitry

---

# 8. Power Architecture

Power enters the system through:

USB Type-C

or

Battery Pack

↓

Battery Charger

↓

Power Path Controller

↓

System Rails

↓

3V3

↓

5V

↓

Subsystems

---

# 9. Voltage Rails

VBUS_USB

5V from USB

VBAT

Battery voltage

SYS

System Power

+5V

LED Supply

Audio

Backlight

+3V3

ESP32

RTC

Logic

Sensors

Display Logic

---

# 10. Processing Architecture

Single Master Architecture

ESP32-S3

↓

Game Engine

↓

Drivers

↓

Peripherals

No secondary CPU shall exist during Revision A.

Future revisions may include auxiliary controllers.

---

# 11. Memory Architecture

Internal Flash

Firmware

Configuration

Resources

Internal PSRAM

Frame Buffers

LVGL

Game Memory

Optional External Flash

Audio Files

Themes

Future Expansions

---

# 12. Communication Architecture

Internal buses

SPI

Display

Flash

I²C

RTC

Battery Charger

Haptic

Expansion

I²S

Audio

USB

Programming

Diagnostics

OTA

Wireless

Wi-Fi

BLE

---

# 13. Display Architecture

Display Module

↓

FFC Cable

↓

RGB Interface

↓

ESP32 LCD Peripheral

↓

LVGL

The Display Board contains no intelligence.

---

# 14. Audio Architecture

Audio Files

↓

Decoder

↓

I²S

↓

MAX98357A

↓

Speaker

---

# 15. Haptic Architecture

Game Event

↓

Driver

↓

DRV2605L

↓

ERM Motor

or

LRA Motor

---

# 16. LED Architecture

Game Engine

↓

LED Manager

↓

Port Module

↓

Three RGB LEDs

Every LED animation shall be non-blocking.

---

# 17. Battery Architecture

Battery Pack

↓

Protection

↓

NTC

↓

Fuel Measurement

↓

Power Path

↓

System

The battery shall never be directly connected to system loads.

---

# 18. USB Architecture

USB-C

↓

ESD Protection

↓

CC Detection

↓

ESP32 Native USB

↓

CDC

MSC

Firmware Update

Diagnostics

---

# 19. Firmware Architecture

Bootloader

↓

HAL

↓

Drivers

↓

Services

↓

Game Engine

↓

GUI

↓

Application

Each layer shall only communicate with adjacent layers.

---

# 20. Mechanical Architecture

The enclosure consists of:

One Main Board

One Display Board

Twelve Port Boards

Battery Holder

Speaker Mount

Internal Structural Frame

The Main Board shall remain mechanically independent from the display.

---

# 21. Expandability

Reserved interfaces:

SPI Expansion

I²C Expansion

UART Expansion

GPIO Expansion

Debug Connector

Unused GPIOs shall remain documented.

---

# 22. Diagnostics

The firmware shall continuously monitor:

Battery

Charging

Temperature

RTC

Memory

Display

LEDs

Speaker

Wireless

---

# 23. Reliability

The architecture shall tolerate:

Unexpected reset

Battery removal

USB insertion

OTA interruption

Watchdog reset

Brownout

without permanent corruption.

---

# 24. Safety

The system shall include:

Battery protection

Reverse polarity protection

USB ESD protection

Connector ESD protection

Power sequencing

Current limitation

Thermal monitoring

---

# 25. Architecture Revision Policy

No subsystem shall be modified without updating:

System Requirements

Architecture

Hardware Documentation

Firmware Documentation

Manufacturing Documentation

---

# 26. Future Revisions

The architecture reserves support for:

LoRa

GPS

NFC

RFID

BLE Mesh

CAN

RS-485

Ethernet

Cloud Synchronization

Additional Sensors

without redesigning the Main Board whenever possible
