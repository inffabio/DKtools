# DK-01
# Main Board
# Block 01 - Power Input

Document ID:
ELEC-MB-001

Version:
1.0

Revision:
A

Status:
Draft

Board:
MB-01

Related Documents

ELEC-001

REQ-PWR

COMP-BQ25895

---

# 1. Purpose

This block defines every electrical circuit between the USB connector and the battery charger.

This is the first electrical stage of the DK-01.

Its responsibility is to safely receive power from USB-C and deliver clean power to the charger IC.

No system loads shall be connected directly to USB VBUS.

---

# 2. Functional Overview

Responsibilities

• Receive USB power

• Protect against ESD

• Protect against overcurrent

• Detect cable insertion

• Supply charger IC

• Isolate faults

---

# 3. Electrical Diagram

USB-C

↓

TVS Protection

↓

Polyfuse

↓

EMI Filter

↓

VBUS Sense

↓

Battery Charger

---

# 4. Connector

Reference

J1

Component

USB Type-C Receptacle

Mounting

Surface Mount

Reinforced Shield Tabs

Current Rating

Minimum

3A

Voltage Rating

20V

USB Version

USB2.0 High Speed

---

# 5. Pin Assignment

VBUS

Power Input

GND

Ground

CC1

Cable Detection

CC2

Cable Detection

D+

USB Data

D-

USB Data

SHIELD

Mechanical Shield

---

# 6. Protection

Protection shall exist before any active circuit.

Required components

TVS diode

Polyfuse

Ferrite bead

ESD array

USB shield grounding network

---

# 7. TVS Device

Reference

D1

Function

Transient suppression

Location

Immediately behind USB connector

Maximum distance

5 mm

Preferred Devices

USBLC6-2SC6

TPD4EUSB30

Equivalent industrial part

---

# 8. Polyfuse

Reference

F1

Purpose

Current limiting

Hold Current

3A

Trip Current

Approximately 6A

Cold Resistance

Below 40 mΩ

---

# 9. Ferrite Bead

Reference

FB1

Purpose

Reduce conducted EMI

Impedance

600 Ω @100MHz

Current Rating

Above 3A

DC Resistance

Below 50mΩ

---

# 10. VBUS Sense

Reference

R1

R2

Voltage Divider

Purpose

Allow ESP32 to detect USB presence.

Maximum ADC voltage

3.3V

Sampling frequency

Low

Power consumption shall be minimized.

---

# 11. USB Shield

The connector shell shall not be directly shorted to digital ground.

Recommended implementation

Shield

↓

1MΩ resistor

↓

100nF capacitor

↓

Ground

Optional

Spark gap footprint

---

# 12. Layout Rules

USB connector shall remain near PCB edge.

TVS shall remain within 5 mm.

Polyfuse shall remain before charger.

No vias on VBUS path whenever possible.

Copper width

Minimum 2.0 mm

Ground stitching around connector.

Differential pair

90 Ω

Matched length

Maximum mismatch

0.25 mm

---

# 13. Test Points

TP_USB_VBUS

TP_USB_GND

TP_CC1

TP_CC2

---

# 14. Validation

Verify

USB insertion

USB removal

VBUS detection

Voltage drop

ESD robustness

USB communication

---

# 15. Risks

Incorrect shield grounding.

TVS too far from connector.

VBUS copper too thin.

Poor EMI filtering.

Weak connector fixation.

---

# 16. KiCad Notes

Footprints shall follow official manufacturer recommendations.

3D model mandatory.

Connector courtyard shall allow automated assembly.

Mechanical keepout shall prevent enclosure interference.

---

# 17. Future Expansion

USB-PD controller footprint reserved.

VBUS current monitor optional.

External accessory power optional
