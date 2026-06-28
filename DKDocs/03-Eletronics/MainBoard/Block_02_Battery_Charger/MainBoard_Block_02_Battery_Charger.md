# DK-01
# Main Board
# Block 02 - Battery Charger

Document ID:
ELEC-MB-002

Revision:
A

Version:
1.0

Board:
MB-01

Status:
Engineering Draft

Primary Component:
U2

BQ25895RTWR

Manufacturer

Texas Instruments

Datasheet Revision

Latest production revision approved before Design Freeze.

---

# 1. Purpose

This block is responsible for charging the internal battery pack, managing the system power path and supplying energy to the remaining electronic subsystems.

The charger shall operate autonomously while allowing firmware supervision through the I²C interface.

The charging subsystem shall remain operational even when the ESP32 firmware is not running.

---

# 2. Functional Requirements

Related Requirements

REQ-PWR-0001

REQ-PWR-0002

REQ-PWR-0003

REQ-PWR-0004

REQ-PWR-0005

REQ-PWR-0006

REQ-HW-0001

---

# 3. Selected Component

Reference

U2

Component

BQ25895RTWR

Package

WQFN-24

Reasons for Selection

Integrated Buck Charger

Integrated Power Path

I²C Interface

Programmable Charging Current

Thermal Regulation

USB Detection

Battery Protection

Wide software support

---

# 4. Internal Functional Blocks

The charger internally implements:

Input Current Limiter

Buck Converter

Battery Charger

Power Path Controller

OTG Boost

ADC

Thermal Monitor

I²C Interface

Safety Timer

Watchdog

---

# 5. External Components

The following external components are mandatory.

Input Capacitors

Output Capacitors

Battery Capacitors

Inductor

Current Sense Network

NTC Network

I²C Pullups

Power Status LEDs (optional)

Test Points

No optional component shall compromise battery safety.

---

# 6. Power Flow

USB-C

↓

ESD

↓

Polyfuse

↓

BQ25895

↓

Battery

↓

System Rail

↓

3V3

↓

5V

↓

Main Board

The charger shall always prioritize safe battery charging over system performance.

---

# 7. Battery Configuration

Battery Type

Lithium-Ion

Configuration

1S2P

Nominal Voltage

3.7V

Maximum Voltage

4.20V

Minimum Voltage

3.00V

Maximum Recommended Capacity

7000 mAh

Cells shall always be identical.

Mixed cell manufacturers are prohibited.

---

# 8. Charge Current

Default Charge Current

2000 mA

Firmware Adjustable

Yes

Minimum

256 mA

Maximum

3000 mA

Charging current shall be automatically reduced whenever thermal regulation becomes active.

---

# 9. Input Current Limit

USB Default

500 mA

USB High Current

3000 mA

Firmware configurable.

The charger shall never overload the USB source.

---

# 10. Thermal Regulation

Charging temperature shall be monitored continuously.

Internal thermal regulation shall remain enabled.

Firmware shall log every thermal throttling event.

---

# 11. NTC

Battery temperature shall be measured using a dedicated NTC.

Recommended value

10k

B3435

Charging shall automatically stop outside safe limits.

---

# 12. Power Path

The system shall remain powered while charging.

Battery charging shall continue even when the ESP32 is in reset.

Removing the battery while USB is connected shall not interrupt system operation.

---

# 13. I²C Interface

The ESP32 shall monitor

Battery Voltage

Charge Current

Input Current

Temperature

Charging State

Faults

Watchdog

ADC

Every error condition shall be reported to the firmware.

---

# 14. Protection

Input Overvoltage

Battery Overvoltage

Thermal Shutdown

Safety Timer

Watchdog

Current Limit

Reverse Current

Short Circuit

No external circuitry shall disable the integrated protections.

---

# 15. Layout Requirements

The charger shall be located within 20 mm of the USB connector.

Input capacitors shall be placed within 2 mm of VIN.

Inductor shall be placed adjacent to the switching pins.

Power loops shall remain below 20 mm².

Thermal pad shall connect to GND plane through thermal vias.

Copper area under thermal pad

Minimum 100 mm².

---

# 16. Copper Requirements

VIN traces

Minimum 2.0 mm

BAT traces

Minimum 2.0 mm

SYS traces

Minimum 2.0 mm

Ground shall use solid copper polygons.

---

# 17. Test Points

TP_VBUS

TP_BAT

TP_SYS

TP_GND

TP_STAT

TP_INT

---

# 18. Firmware Interface

Driver

drivers/bq25895/

Initialization

System Boot

Monitoring

Every second

Fault Logging

Enabled

Automatic Recovery

Enabled

---

# 19. Failure Modes

USB removed during charging

Battery disconnected

Battery overheating

Input overload

NTC open

NTC short

Thermal shutdown

Watchdog timeout

Each failure mode shall generate a diagnostic event.

---

# 20. Engineering Checklist

[ ] Datasheet reviewed

[ ] Reference design reviewed

[ ] Thermal calculations completed

[ ] Inductor selected

[ ] Capacitors selected

[ ] NTC selected

[ ] Footprint validated

[ ] STEP model available

[ ] LCSC component available

[ ] PCB layout reviewed

[ ] DRC approved

[ ] Prototype validated

[ ] Test report approved
