# Firmware component boundaries

ETP-001 intentionally implements only the `main` identity/bootstrap application. The functional component boundaries below are reserved by the normative firmware architecture and will be introduced by their owning issues rather than as speculative implementations here.

| Component | Responsibility | Owning work |
|---|---|---|
| `board` | verified pin map, capabilities, board identity | ETP-002 |
| `telemetry` | versioned records and loss accounting | ETP-003 |
| `touch_rx` | raw/smooth/benchmark/proximity acquisition | ETP-005 |
| `led_matrix` | framebuffer and physical LED mapping | ETP-004/006 |
| `led_probe` | bounded WS2812 serial-probe experiments | ETP-007 |
| `gpio_probe` | coded edge excitation | ETP-008 |
| `espnow_link` | peer identity, schedules, RSSI metadata | ETP-009 |
| `imu` | QMI8658C acquisition and motion state | ETP-004/016 |
| `scheduler` | guarded local timing slots | ETP-009 onward |
| `experiment` | declarative protocol execution | characterization phases |

No GPIO ownership or hardware behavior is declared by this placeholder document. `board` becomes the canonical owner when ETP-002 is implemented.
