---
rag_id: ESPT-RAG-ANALYSIS
title: Analysis, system identification, and pose inference
status: normative
scope: host-analysis
---

# Analysis and pose inference

## Signal model

Use a model of the form

`y(t) = self_led(t) + H(pose) * probe_peer(t) + environment(t) + noise(t)`

without assuming the terms are perfectly linear. The purpose is to structure experiments:

- estimate predictable self-interference from the receiver's own LED state;
- identify response to a known peer stimulus;
- determine whether response changes consistently with pose;
- quantify residual/environmental variability.

## First analyses

Before ML, implement:

- per-channel baseline/drift plots;
- robust variance/MAD and outlier rates;
- PSD/FFT and stimulus-triggered averages;
- cross-channel covariance/correlation;
- stimulus/code cross-correlation;
- effect-size distributions with bootstrap confidence intervals where useful;
- confusion matrices for simple held-out classifiers;
- ablations by LED state, radio state, IMU motion, board identity and power source.

## Coded probes

Use deterministic PRBS and orthogonal/Hadamard-like code families where timing permits. Estimate the effective coupling matrix from source modes to touch channels.

Do not equate the number of physical LEDs with independent field dimensions. Measure singular values/effective rank of the recovered coupling matrix. If the 64-pixel matrix collapses to a few observable electrical modes, use those modes rather than forcing a 64-source interpretation.

## Response volume

If pose-dependent coupling is repeatable, construct a calibrated response surface indexed by controlled variables such as:

- facing edge/configuration;
- quarter-turn rotation;
- lateral offset;
- gap;
- optional tilt/height;
- board pair and operating condition.

A runtime estimator may begin as nearest-template / regularized linear discriminant / small tree model. A more complex model must beat transparent baselines on held-out board-pair evaluation.

## Confidence and rejection

Pose output must include confidence/quality and support `unknown` / `ambiguous`. The system should reject out-of-distribution or low-margin states rather than force a quarter-turn answer.

## Sensor fusion

IMU and RSSI are secondary features/priors, not ground truth. IMU is useful for coplanarity, motion events, and short-term yaw change; RSSI may weakly constrain proximity/peer association. Evaluate their incremental value with ablation tests.
