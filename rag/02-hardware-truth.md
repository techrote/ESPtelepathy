---
rag_id: ESPT-RAG-HW
title: Target hardware truth and pin ownership
status: normative
scope: hardware
---

# Target hardware truth

## Target module

User-selected target listing: `https://www.aliexpress.com/item/1005006962940633.html`.

The working reference design is Waveshare **ESP32-S3-Matrix**, SKU 27119. Waveshare documents a 25.00 mm × 25.00 mm board with an ESP32-S3, 8×8 RGB matrix, QMI8658 6-axis IMU, USB-C, DOUT expansion pad, and 17 exposed GPIOs. The schematic identifies the RGB devices as **WS2812B-0807** and the IMU as **QMI8658C**.

The physical boards received for this project are authoritative. Record photographs, silkscreen, USB identity, chip/package markings where visible, pinout behavior, and firmware-reported chip data before relying on reference-design assumptions.

## Exposed edge GPIO geometry

Waveshare's pinout image shows:

- left edge: 5V, GND, 3V3, then GPIO7 through GPIO1;
- right edge: GPIO33 through GPIO40, TX, RX.

ESP32-S3 native touch channels are GPIO1 through GPIO14. Therefore GPIO1-7 are unusually convenient **stock edge-accessible touch inputs**, while GPIO33-40 are useful **stock edge-accessible digital transmitters** but are not touch channels.

This asymmetry is a feature for control experiments, but it also means the stock board does **not** provide four edges of spatially distributed touch electrodes. Four-edge pose sensing may require copper-foil/wire electrodes connected to the available touch GPIOs or may need to exploit global/LED-field fingerprints.

## Onboard ownership to verify

Reference schematic nets indicate onboard use of touch-capable pins including the QMI8658C I2C/interrupt signals and the LED matrix input. Do not repurpose GPIO8-14 until pin ownership is verified from the schematic and on the actual board.

Known reference facts to verify in ETP-002:

- QMI8658C is connected by I2C plus interrupt nets.
- LED matrix DIN is driven from a touch-capable ESP32-S3 GPIO on the reference design.
- DOUT from the final RGB device is exposed as a pad/test point.
- the matrix is a 64-device serial chain with intermediate row-chain nets in the schematic.
- the board uses an ME6217C33M5G 3.3 V LDO; the vendor page warns against excessive LED brightness due to heating.

## ESP32-S3 touch capabilities relevant to research

Espressif documents 14 external capacitive touch GPIOs (GPIO1-14), raw/smoothed/benchmark/proximity data, an internal denoise channel, digital filtering, proximity sensing, and TOUCH14 as the shield-driver-capable channel. Proximity sensing accumulates multiple scans because proximity-induced capacitance change is much smaller than direct touch.

The project must retain raw values; boolean touch events are insufficient for system identification.

## Hardware augmentation policy

Escalate in this order:

1. completely stock board and exposed plated holes;
2. removable jumper/copper tape electrodes;
3. simple laser-cut/3D-printed alignment fixture plus repeatable foil geometry;
4. only after quantified evidence, propose a purpose-built PCB/electrode revision.

Every augmentation must have a drawing/photo/measurement sufficient to reproduce it.
