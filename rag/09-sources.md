---
rag_id: ESPT-RAG-SOURCES
title: Canonical external source register
status: normative
scope: references
---

# External source register

Prefer these primary/vendor sources over secondary tutorials when resolving technical questions.

## Target hardware

- User-selected target listing: https://www.aliexpress.com/item/1005006962940633.html
- Waveshare ESP32-S3-Matrix documentation: https://docs.waveshare.com/ESP32-S3-Matrix
- Waveshare resources page: https://docs.waveshare.com/ESP32-S3-Matrix/Resources-And-Documents
- Waveshare schematic PDF: https://files.waveshare.com/wiki/ESP32-S3-Matrix/ESP32-S3-Matrix-Sch.pdf

Verified from the current Waveshare docs/schematic during planning: 25 mm × 25 mm reference board; 8×8 RGB matrix; QMI8658/QMI8658C; exposed DOUT; left-edge GPIO1-7 and right-edge GPIO33-40; schematic RGB part label WS2812B-0807. Re-verify against purchased hardware.

## ESP32-S3

- ESP32-S3 datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
- ESP-IDF ESP32-S3 capacitive touch API (latest/stable): https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/cap_touch_sens.html
- ESP32-S3 hardware design, touch schematic guidance: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- ESP32-S3 PCB/touch layout guidance: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- ESP-NOW API: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/network/esp_now.html
- ESP-NOW FAQ including RSSI receive metadata: https://docs.espressif.com/projects/esp-faq/en/latest/application-solution/esp-now.html

Relevant manufacturer facts: ESP32-S3 has 14 external touch GPIOs, GPIO1-14; only TOUCH14 can drive the shield electrode; Espressif recommends a 470 Ω–2 kΩ series resistor (510 Ω preferred starting point) in purpose-designed touch circuits; proximity sensing accumulates scans because the effect is small; the internal denoise channel and filtering are available; touch has limited interference immunity and must be empirically characterized.

## QMI8658C

- QST QMI8658C datasheet: https://qstcorp.com/upload/pdf/202202/QMI8658C%20datasheet%20rev%200.9.pdf

Use the IMU as a motion/coplanarity/short-term rotational prior, not as an absolute planar-heading oracle unless an independently validated heading source is available.
