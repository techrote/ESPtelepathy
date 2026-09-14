---
rag_id: ESPT-RAG-FW
title: Firmware architecture and timing model
status: normative
scope: firmware
---

# Firmware architecture

## Platform

Primary target: ESP-IDF with a repository-pinned supported version. **ETP-001 pins ESP-IDF v6.1 for the v0 baseline in `toolchain/versions.env`**, using Espressif's official versioned Docker image for CI/default reproducible builds. Change the major/minor baseline only through an explicit migration PR with successful firmware CI.

Prefer native drivers/components for touch sensing, ESP-NOW/Wi-Fi, RMT or equivalent accurately timed LED/probe generation, timers, USB/serial logging, and I2C/QMI8658C access.

## Components

Keep responsibilities separable:

- `board`: verified pin map, capabilities, board identity;
- `telemetry`: versioned records and loss accounting;
- `touch_rx`: raw/benchmark/smooth/proximity acquisition and denoise configuration;
- `led_matrix`: visible framebuffer plus deterministic physical-order mapping;
- `led_probe`: controlled serial/probe sequences, including feasibility tests for post-frame extra traffic;
- `gpio_probe`: coded edge excitation on safe exposed GPIOs;
- `espnow_link`: peer discovery/identity, sequence transport, RSSI metadata, schedule coordination;
- `imu`: QMI8658C acquisition and motion state;
- `scheduler`: radio/stimulus/capture slots with explicit guard intervals;
- `experiment`: declarative protocol runner driven by IDs/seeds rather than ad-hoc loops.

## Timing policy

Separate coordination from precision timing:

1. peers negotiate experiment/probe ID and a future epoch over ESP-NOW;
2. each board arms a local schedule;
3. precision stimulus and acquisition run using local timer/peripheral timing;
4. radio can be kept quiet during sensitive windows when the protocol requires it;
5. results/status are exchanged after the window.

Every slot must record scheduled vs actual timestamps and late/missed state.

## LED probe caution

A key hypothesis is that additional WS2812-compatible serial symbols sent after the 64 visible pixel words but before the reset/latch interval can traverse the chain and exit DOUT without changing the intended displayed frame. Treat this as **unproven on the purchased hardware**.

The implementation must first provide a bounded conformance test:

- verify the visible 64-pixel frame remains unchanged across probe payload lengths/patterns;
- observe DOUT where practical;
- detect/reset on anomalies;
- impose payload/time limits;
- do not use the mechanism in later experiments until ETP-007 records a pass on actual boards.

## Resource ownership

The board profile is the only place allowed to declare GPIO ownership. Conflicts between touch, IMU, LED DIN, USB/JTAG/UART, probe outputs, and boot-strapping behavior must fail at compile/configuration time where practical.
