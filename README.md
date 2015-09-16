# Patches

A repository of patches for Audulus 3.0.

## Scale Quantizer

![Scale Quantizer Screenshot](Scale Quantizer.png)

The *Scale Quantizer* snaps pitches (in 1/oct units) to the nearest tone in a scale. The scale is determined by the 12 toggle buttons. The image above is a C blues scale.

## Cartesian Sequencer

![Cartesian Sequencer Screenshot](Cartesian Sequencer.png)

The *Cartesian Sequencer* is a generalization of a 16-step sequencer, with steps arranged in a 4x4 grid. It has two clock inputs, xclk and yclk, which advance the current step horizontally and vertically.

## Unison

![Unison Screenshot](Unison.png)

The *Unison* creates four voices from one according to a *Spread* control. When   spread is 0, all four channels are equal to the input. Increasing spread increases the difference between the voices. Typically, you'll feed a pitch signal in 1/oct units to the input.

## Osc

![Osc Screenshot](Osc.png)

An oscillator. This is a wrapper for the Osc node that makes it more user friendly. Pitch is in 1/oct units.

## JDRaoul/Bidirectional Seq16

![Bidirectional Seq16 Screenshot](JDRaoul/Bidirectional Seq16.png)

## JDRaoul/Envelope Filter

![Envelope Filter Screenshot](JDRaoul/Envelope Filter.png)

## JDRaoul/FM

![FM Screenshot](JDRaoul/FM.png)

## JDRaoul/Clock

![Clock Screenshot](JDRaoul/Clock.png)

## JDRaoul/Euclidean Sequencer

![Clock Screenshot](JDRaoul/Euclidean Sequencer.png)

## JDRaoul/Pulse Divider

![Clock Screenshot](JDRaoul/Pulse Divider.png)