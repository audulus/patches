## All Modules
![All Modules](./All Modules.png)



## 5ms Revolving Clock Divider
![5ms Revolving Clock Divider](./Clock/5ms Revolving Clock Divider.png)

This module takes an incoming clock signal and routes it to 8 outputs.  If no Count Clock or Revolve input is applied, the clock signal is pulse-divided by the output number.  Out 1 then is (Clock Hz/1), Output 2 is (Clock Hz/2), …, and Out 8 is (Clock Hz/8).  A blue light turns on when the signal is high.  You’ll notice that for every 8 clock pulses from output 1, you’ll get one pulse from output 8.  

When a clock signal is applied to the Count Clock input, an internal counter counts from 0-7 up or up/down (depending on your selection), and internally switches the output routing as if you were shifting where the output jacks were being routed to.  With a Count of 1, Output 1 becomes Output 8, Output 2 becomes Output 1, etc.  With a Count of 2, Output 1 becomes Output 7, Output 2 becomes Output 8, Output 3 becomes Output 1, etc.  

A red light indicates which output is passing the undivided clock signal.  This light may change to purple if it syncs with the blue high output indicator.

Like Count, Revolve also switches the order of inputs, but it can do so in whatever order you’d like.  Attach a knob or sequencer for direct control.  The Revolve(x) control is an internal multiplier for the revolve signal.  If a triangle wave counts up and down, that triangle wave with Revolve(2) would count up twice, then down twice.

## Clock
![Clock](./Clock/Clock.png)

The clock outputs a pulse.  The higher the Hz value, the faster the pulse.  You can turn it on and off with the button.

Inputs on modules designed to accept a clock pulse are labelled “Clock.”  

The Sync input can be used to synchronize multiple clock sources to a master clock.  The master clock’s Output feeds into the slave clocks’ Sync input.  Every time the master clock pulses, it resets the slave clocks.

## Divided Clock
![Divided Clock](./Clock/Divided Clock.png)

This is a clock and a pulse divider packaged together for convenience.  There’s an On/Off button, a Hz control for the clock speed, a divide by x knob, and a pulse width control.  The Clock Output is the undivided clock signal, and the /x Output is the clock Hz divided by the value set by the /x knob.  The sync input allows this clock to be slaved to a master clock.

## Pulse Divider
![Pulse Divider](./Clock/Pulse Divider.png)



## Tap Tempo
![Tap Tempo](./Clock/Tap Tempo.png)

The tap tempo infers the time between two button presses and outputs that time as a static value in Hz.  You can use it to add a tap tempo control for delays, clocks, tremolos, etc.

## Touch Feedback Clock
![Touch Feedback Clock](./Clock/Touch Feedback Clock.png)

The Touch Feedback Clock allows you to quickly and naturally dial in rhythmic clock sequences, and warp them with the Loop Time knob.  

It works by attaching a trigger to a delay node with the feedback turned all the way up.  If the loop time is set too low, or the delays pile up enough so that they start to smear together, you may end up with an “always on” clock signal that will need to be reset.

The Reset button clears the delays, but it takes the length of the Loop Time to clear them out - that’s why there is a Wait/Ready light above it.  When Ready is lit, you’re clear to enter a new input. 

Really interesting things happen when you start tap a sequence, pull the loop time down, then expand the loop time again.

## Bitcrusher
![Bitcrusher](./Effects/Distortion/Bitcrusher.png)

This Bitcrusher represents one two ways to “crush” a wave to add digital distortion.

This method uses resolution reduction by reducing the precision of the 32-bit floating point input.

The Crush knob decreases resolution as its value is increased.  The Mix knob mixes the dry and wet signals 
together.


## Distortion
![Distortion](./Effects/Distortion/Distortion.png)

This is a repackaging of the distortion node as a module.  For more info, see the Audulus node documentation.

The trim knob decreases the Output level.

## Ms. Torsion Distortion
![Ms. Torsion Distortion](./Effects/Distortion/Ms. Torsion Distortion.png)

This is a simple distortion with 4 variables.  

- Crush is a dry/wet mix knob.
- Gnash raises the cutoff point of the LPF on the distortion.
- Bite increases the Q value of the LFP curve
- Grind shifts the distortion an octave up.

## Rate Reduction
![Rate Reduction](./Effects/Distortion/Rate Reduction.png)

Sample Rate Reduction is a type of digital distortion, usually found working in concert with a Bitcrusher.

This method reduces the sample rate on an input from the default 44.1k (or your host’s sample rate) to a lower sample rate.

## Wavefolder
![Wavefolder](./Effects/Distortion/Wavefolder.png)



## Waveshaper
![Waveshaper](./Effects/Distortion/Waveshaper.png)



## Pitch Shift
![Pitch Shift](./Effects/Modulation/Frequency/Pitch Shift.png)

This is a repackaging of the pitch shift node as a module.  For more info, see the Audulus node documentation.

## Ring Modulator
![Ring Modulator](./Effects/Modulation/Frequency/Ring Modulator.png)

Ring modulation multiplies a signal (Input) with a carrier signal (Mod Input).  In most pedal-based ring modulators, the carrier is a sine wave, but this design allows you to plug in whatever signal you’d like.

The Depth knob controls the amount of modulated signal mixed back in with the original dry signal.

The Trim knob controls the output level.

## Unison
![Unison](./Effects/Modulation/Frequency/Unison.png)

Unison takes an input signal and turns it into a 4-channel polyphonic signal with 1 unaffected channel and 3 detuned channels.  The Spread knob controls how detuned the 3 channels are.

Its output is polyphonic, as indicated by the /P.  All modules in a signal chain after this module will run in polyphonic mode.

## Pan Scan
![Pan Scan](./Effects/Modulation/Level/Pan Scan.png)

This is an autopanner.  It will swap the left and right signals back and forth according to either the internal LFO (Int) or an external modulation signal (Mod).  The Hz of the internal LFO can be adjusted with the Speed knob.

## Tremolo
![Tremolo](./Effects/Modulation/Level/Tremolo.png)



## Reverb (Mono to Stereo)
![Reverb (Mono to Stereo)](./Effects/Reverb/Reverb (Mono to Stereo).png)



## Reverb (Stereo to Stereo)
![Reverb (Stereo to Stereo)](./Effects/Reverb/Reverb (Stereo to Stereo).png)



## Envelope Generator
![Envelope Generator](./Envelope Generator/Envelope Generator.png)



## High:Low Pass Filter
![High:Low Pass Filter](./Filter/Filter/High:Low Pass Filter.png)



## Attenuator
![Attenuator](./Level/Attenuators/Attenuator.png)



## Crossfader
![Crossfader](./Level/Attenuators/Crossfader.png)



## Mapper
![Mapper](./Level/Attenuators/Mapper.png)



## Range
![Range](./Level/Attenuators/Range.png)



## Scaler
![Scaler](./Level/Attenuators/Scaler.png)



## Slew Limiter
![Slew Limiter](./Level/Attenuators/Slew Limiter.png)



## Spline
![Spline](./Level/Attenuators/Spline.png)



## Master Output (L:R Meters)
![Master Output (L:R Meters)](./Level/Master Output/Master Output (L:R Meters).png)



## Pan - Mono to Stereo
![Pan - Mono to Stereo](./Level/Pan/Pan - Mono to Stereo.png)



## Invert
![Invert](./Math/Arithmetic/Invert.png)



## Multiply
![Multiply](./Math/Arithmetic/Multiply.png)



## Sum
![Sum](./Math/Arithmetic/Sum.png)



## Count Up
![Count Up](./Math/Count/Count Up.png)



## Count Up:Down
![Count Up:Down](./Math/Count/Count Up:Down.png)



## Comparator
![Comparator](./Math/Logic/Comparator.png)



## 1:0 Trigger
![1:0 Trigger](./Math/Probability/1:0 Trigger.png)



## Either:Or Switch
![Either:Or Switch](./Math/Probability/Either:Or Switch.png)



## Either:Or Trigger
![Either:Or Trigger](./Math/Probability/Either:Or Trigger.png)



## e
![e](./Math/Special Numbers/e.png)



## Golden Ratio
![Golden Ratio](./Math/Special Numbers/Golden Ratio.png)



## Pi
![Pi](./Math/Special Numbers/Pi.png)



## Fibonacci Sequence
![Fibonacci Sequence](./Math/Special Sequences/Fibonacci Sequence.png)



## Pentatopic Number Sequence
![Pentatopic Number Sequence](./Math/Special Sequences/Pentatopic Number Sequence.png)



## Tetrahedral Number Sequence
![Tetrahedral Number Sequence](./Math/Special Sequences/Tetrahedral Number Sequence.png)



## Triangular Number Sequence
![Triangular Number Sequence](./Math/Special Sequences/Triangular Number Sequence.png)



## 4x1 Mixer
![4x1 Mixer](./Mixer/4x1 Mixer.png)



## Cyclone Matrix
![Cyclone Matrix](./Mixer/Cyclone Matrix.png)




## White Noise
![White Noise](./Noise/White Noise.png)



## Crossfade Oscillator
![Crossfade Oscillator](./Oscillator/Audio/Crossfade Oscillator.png)



## Organ Oscillator
![Organ Oscillator](./Oscillator/Audio/Organ Oscillator.png)



## Oscillator
![Oscillator](./Oscillator/Audio/Oscillator.png)



## Sum Noise Add Synth
![Sum Noise Add Synth](./Oscillator/Audio/Sum Noise Add Synth.png)



## Rectifier
![Rectifier](./Oscillator/Modulation/Rectifier.png)



## Rectifying LFO
![Rectifying LFO](./Oscillator/Modulation/Rectifying LFO.png)



## Reverse Saw LFO
![Reverse Saw LFO](./Oscillator/Modulation/Reverse Saw LFO.png)



## Saw LFO
![Saw LFO](./Oscillator/Modulation/Saw LFO.png)



## Sine LFO
![Sine LFO](./Oscillator/Modulation/Sine LFO.png)



## Square LFO
![Square LFO](./Oscillator/Modulation/Square LFO.png)



## The Longest Time LFO
![The Longest Time LFO](./Oscillator/Modulation/The Longest Time LFO.png)



## Triangle LFO
![Triangle LFO](./Oscillator/Modulation/Triangle LFO.png)



## 1-Shot Bank
![1-Shot Bank](./Sample & Hold/1-Shot Bank.png)



## Sample & Hold
![Sample & Hold](./Sample & Hold/Sample & Hold.png)



## Bass-ic Sequencer
![Bass-ic Sequencer](./Sequencer/Bass-ic Sequencer.png)



## Euclidean Sequencer
![Euclidean Sequencer](./Sequencer/Euclidean Sequencer.png)



## The Warpeggiator
![The Warpeggiator](./Sequencer/The Warpeggiator.png)



## Demultiplexer
![Demultiplexer](./Switching/Demultiplexer.png)



## Momentary Close
![Momentary Close](./Switching/Momentary Close.png)



## Mometary Open
![Mometary Open](./Switching/Mometary Open.png)



## Multiplexer
![Multiplexer](./Switching/Multiplexer.png)



## Toggle Mute
![Toggle Mute](./Switching/Toggle Mute.png)



## DAW Time
![DAW Time](./Utility/DAW/DAW Time.png)



## Keyboard Input (1:oct)
![Keyboard Input (1:oct)](./Utility/MIDI Control/Keyboard Input (1:oct).png)



## Keyboard Input (Hz)
![Keyboard Input (Hz)](./Utility/MIDI Control/Keyboard Input (Hz).png)



## Quantizer
![Quantizer](./Utility/Quantizer/Quantizer.png)



## Lit Via
![Lit Via](./Utility/Vias/Lit Via.png)



## Metered Via
![Metered Via](./Utility/Vias/Metered Via.png)



## Via
![Via](./Utility/Vias/Via.png)



