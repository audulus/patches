## Clock
### BPM Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

This clock allows you to dial in a particular BPM value.  The clock signal will correspond to the quarter note beat.

### Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

### Divided Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

This clock demonstrates how to derive a divided clock signal by using the Hz output of the master clock to set the tempo of the slave clock.  The slowest clock should always be connected back to the sync input of the master clock to make sure the clocks stay synced.

### Probability Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

This clock uses a probability module to add some variation to the clock signal.  These are create for triggering drums or just adding some more randomness to you patch to give it a more human feel.

### Pulse Looper
The Pulse Looper will sample and play back gate pulses entered into the central button.  Several loopers can be chained by using the > inputs.  The slaved modules must have their loops knobs turned all the way down.

### Shift Register Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

This clock is attached to a Shift Register module, which allows you to have multiple subdivisions of the clock and their inverses - perfect for triggering drums.

### Smeared Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

The Gate Smear module keeps a gate signal high for the length of time determined by depth.  Great for deriving two different types of clock signals from one probability clock.

### Tap Tempo Clock
Clocks are the heartbeat of a modular patch - they keep tempo and drive sequencers forwards.  Clocks in Audulus create g, or gate signals, which are 0 or 1.  The width modulation (WM) control determines the ratio of on/off time of the gate.  The bottom knob turns the clock on and off.  If you turn the Hz knob all the way down, you can input a Hz value directly at the Hz input.

This clock allows you to directly tap a tempo into a clock.

### Touch Clock
The Touch Feedback Clock allows you to quickly and naturally dial in rhythmic clock sequences, and warp them with the Loop Time knob.  

It works by attaching a trigger to a delay node with the feedback turned all the way up.  If the loop time is set too low, or the delays pile up enough so that they start to smear together, you may end up with an “always on” clock signal that will need to be reset.

The Reset button clears the delays, but it takes the length of the Loop Time to clear them out - that’s why there is a Wait/Ready light above it.  When Ready is lit, you’re clear to enter a new input. 

Really interesting things happen when you start tap a sequence, pull the loop time down, then expand the loop time again.

## Controller
### Touch Me
This controller is optimized for iOS use - in particular the iPhone.

### XY Pad - 8x8
This 8x8 point XY pad produces values between 0 and 1 in steps of 0.125 (1/8) at the X and Y outputs.

To use it, draw a connection down from the output directly above the XY field.  Important: Hold this connection - do not let go, and do not connect it to a point on the XY field.  Instead, wave the connection above the field without letting go.  If you accidentally let go of the connection, it can be difficult finding and disconnecting it - try using the undo function instead.

Connecting in the bottom left corner is a coordinate of (0,0).  Connecting in the upper right corner is a coordinate of (1,1).

To smooth the transitions between each step, connect the outputs of this module to a slew limiter.

Common XY Pairs:

X - Filter Cutoff
Y - Filter Resonance

X - Filter Cutoff
Y - Gate Amplitude

X - Pitch
Y - Gate Amplitude

X - Pitch 1
Y - Pitch 2

## Drum
### Cymbal
This drum module creates a large variety of cymbal sounds - the BPF and HPF controls are very interactive with the sizz (sizzle) control.

### IT'S A TRAP!!
This drum machine is a collection of 3 drum modules into one convenient package.  Modulate the parameters of the individual sounds to create more variety in your drum kit.

### KarPlus
This Karplus-Strong Synthesis drum impulse resonator makes percussive sounds by feeding an impulse through a very short delayed feedback loop.  Drum sounds from kicks to claves are possible with this!

### Kick


### Res
The Res Drum uses an impulse fed into a resonant filter to create drum sounds.  The two peaking filters you see are for noise and tone, respectively.  Draw a connection down from the e (envelope) output to any of the parameters for more organic shaping.

### Snare
This snare drum is based on the 808 snare diagram found in the Sound on Sound Synth Secrets collection.  You can internally adjust the pitch of the snare if you’d like by changing the triangle and sine oscillators.

### Weather Patterns
This drum machine combines several drum modules with a matrix of probability triggers.  The first control A or B passes gate A or B based on the chance set by the control.  0/1 is the chance that the selected trigger will pass on further.  And the replicated drums on either side are picked between with the A/B control in between them.  If this seems confusing, just check out the demo for this drum machine under Instruments -> Demo, or search the “demo” tag.

## Effect
### Analog Delay+Chorus
This is an analog-modelling delay that uses a z-1 filter in the delay’s feedback loop along with a tanh(x) drive function to simulate the gritty, low-passed sound of a real analog delay.  The speed and depth controls affect how deep and fast the chorus effect is applied to the delays.  This delay can sound very huge when used in stereo with slightly different settings on the Left and Right channels.

### Art D'Echo Dub Delay
This delay is specially made to get that spring reverb tape echo drum sound.  The tens control is the tension of the spring, and the drive, cut, and color, all change the qualities of the over all effect.

### Icebox Audio Freezer
This effect will grab bits of incoming audio and freeze them, playing them indefinitely until a new signal comes in to take its place.  This effect is specifically crafted for electric guitar, but it works great on synthesizers and voice as well.

### Multi-Tap Filter Delay
This delay has 3 taps that can be panned, individually leveled, and filtered.  Great for adding variety to percussive sounds.

### Stereo Digital Delay
This delay is a repackaging of the delay node and will accept a stereo or mono signal and create a stereo echo from that.  When the Mono switch is engaged (red), only the L input passes signal to the delay nodes.

### Asymmetrical Clipper
This effect will asymmetrically clip your signal in a way reminiscent of many famous diode clipping distortion pedals.  The bottom knob sets the clip type - if only the top light is illuminated, the clipping mode is symmetrical.  If both lights are illuminated, then you can adjust the positive and negative clip points independently.

### Bit Crush
Bit Crush reduces the bit length of the numbers running through it, resulting in a distinctly distorted 80s digital synth sound.

### Distortion
This module is a repackaging of the distortion node with an added tanh(x) drive function to limit the gain of the audio and further shape the distortion.

### Down Sample
This Downsample Effect allows you to reduce the sample rate of the audio passing through it.

### Drive
The Drive control applies a tanh(x) expression to the signal passing through it to give a tube-like soft clipping distortion sound.

### Wavefolder
Distorts a signal via wave-folding. Gain determines the number of folds. Mix mixes in the folded version of the wave.

### Ducker
Ducking is a type of very noticeable compression, and is very popular right now especially in genres like Chillwave.  Washed Out’s first album has a lot of ducking effect across it.

The Ducker uses an input signal at a (usually a kick drum) to compress the LR signal throughput.  It is essentially a side-chain compressor, but instead of being frequency dependent, the easily selectable routing of Audulus makes it simple to just plug in whatever you want to cause the “ducking” effect.  This gives you a much cleaner and more selective ducking sound, as you can isolate the specific instrument you want to cause the ducking effect, rather than an entire frequency band, as it’s usually done.

### miniPress
Simple lightweight compressor with variable curve.

### RMS Compressor
RMS compression is perfect for applying compression without destroying the dynamics of the attack of a signal.

The RMS compressor takes samples of the audio coming through it and compresses the audio based on the root mean square of those samples.  This unit can use a Zero Cross to try to estimate the frequency of the incoming signal and sync the sample rate to that frequency (for more accurate readings) or, for even greater accuracy, you can set the sampling rate with an Octave (o) signal directly).

### Tube Limiter
crossfades to soft clip tanh distortion when input > threshold knob

### Auto Pan
This module will pan between two audio signals based on the speed of the LFO applied at the m input.  The width control adjusts how wide the panning effect is.

### Tremolo
Tremolo is an amplitude modulation effect.  The m input of this module is optimized with a slew limiter so that sharp waveforms like saw and square can be used without causing popping in the audio signal (similar to how Audulus automatically crossfades a new connection).

### Vibrato - Delayed
Vibrato is a frequency modulation effect.  This effect uses an LFO to simulate the vibrato effect of a violinist’s finger moving back and forth over the string.  This vibrato also has a delay effect, which, when gated, will reset the vibrato to allow for a more natural sound.  Next time you listen to a violin solo, listen closely and you’ll realize that the vibrato effect will generally become more pronounced the longer the note is held - this is done on purpose for emotional emphasis.  Just use whatever gate signal you’re using to trigger your envelope to trigger this delay function.

### Vibrato - Tape Warble
Tape warble is a vibrato effect that combines a low frequency modulation with a high frequency modulation.   Both of these modulations are caused by different types of worn out components in a tape machine’s transport mechanism.  The Wow effect is caused by irregularities in the circumference of the roller and the faster flutter effect is caused by the tape catching and sticking on the playhead and other components.

### Vibrato - Wiggler
This module takes advantage of the resonance of filters to create a wiggling effect during large changes in pitch.  The greater the distance between notes, the larger and longer the wiggling effect will be.

### Pitch Shift
This is a repackaging of the Pitch Shift node, and allows you to shift your audio from 1 octave below (.5), to 1 fifth above (1.5), to an octave above (2).

### Unison
Unison takes an Octave (o) signal and creates a polyphonic signal where each signal is slightly detuned from the other.  This lends your sound a chorusing effect, like multiple people signing around a common pitch, but all slightly off from one another.

### Spring Reverb
This is a spring reverb, created by using the envelope of the incoming audio signal to drive a high-q BPF through a frequency range fed into a delay with a very small range.  It’s not a perfect spring sound, but if you know anything about recreating spring reverb, this has to be one of the most resource-inexpensive ways of doing it.

### Stereo Reverb
This is a repackaging of the Stereo node, and allows you to use either a stereo or mono input signal.

## Envelope
### Envelope
This module is meant to be your one-stop-shop for all your envelope needs.  The envelope generates an e signal that can be plugged into any oscillator.  It is triggered by a g (gate) signal at its input.  The time range for each portion of the envelope is adjustable to 0-1, 0-10, and 0-60 seconds (for a potentially 3 minute long ADR envelope).  The mode control prevents any incoming gate signal from retriggering the envelope until it has completed its entire cycle.  The envelope creates two different signals: one linear, and the other shaped by the shape and drive controls to be exponential or logarithmic.  Use the linear output for your volume envelope and the shaped output for your filter and you can get a great sound with just one envelope and one set of controls.  The ^v control sets the floor of the shaped envelope and the width controls its range - use this to tune the frequency response of the envelope.  If you intend to use the env>0 mode, you can take the Octave (o) signal from the output of this module to prevent legato sliding during the cycle of the envelope.  Inverted outputs of each envelope are provided for convenience.

### One Shot
This module will create a falling and rising m signal whenever it is triggered or tapped.

## Filter
### 1073 EQ (Stereo)
This module is a recreation of the filter curves and cutoff points of the Neve 1073 EQ.  It is a great tone shaping EQ, especially for guitar.

### 1073 EQ
This module is a recreation of the filter curves and cutoff points of the Neve 1073 EQ.  It is a great tone shaping EQ, especially for guitar.

### APF
All-pass filters change the phase relationship of frequencies to one another - they are essential to creating great-sounding reverbs.

### BPF
Bandpass filters pass only a narrowly selected frequency band, cutting off everything above and below.

### High Shelf EQ
High Shelf EQs lift or cut all of the frequencies above its cutoff point in a relatively linear fashion.

### HPF
High pass filters pass frequencies above their cutoff points while rejecting frequencies below it.

### Low Shelf EQ
Low Shelf EQs lift or cut all of the frequencies below its cutoff point in a relatively linear fashion.

### LP-HP
This is a switchable High Pass/Low Pass filter module with resonance control.

### LPF
High pass filters pass frequencies below their cutoff points while rejecting frequencies above it.

### Multimode Filter
This multimode filter is created from only two low-pass filters and some math.  The BPF and NOT filters aren’t very exact, but they have their own sound to them.

### Notch
Notch filters are the opposite of band pass filters, and are also known as band reject filters - they pass every frequency but a selected band.

### Peak EQ
A peak EQ is a combination of a band pass and notch filter that also leaves other frequencies outside the passband unaffected.

### SVF
SVF filter with crossfader between lp,bp,hp made with z-1 single sample feedback loop.


## Instruments
## Math
### Add
This module adds signals A and B.

### Divide
This module divides signal A by B.

### Multiply
This module multiplies signals A and B.

### Subtract
This module subtracts signal B from signal A.

### -#2#
This module translates a knobs range from 0-1 to a range set by the # input.

### 02#
This module translates a knob signal from 0 to 1 to 0 to the number set at the # input.

### Center Range
This module allows you to define the center value of a knob (a knob’s output when it is set to 50%) and the range the knob covers (the amount of swing left to right).

### Integers - 0-#
This module takes a 0-1 knob signal and translates it into integers 0 through the number set at the # input.

### Integers - 1-#
This module takes a 0-1 knob signal and translates it into integers 1 through the number set at the # input.

### Knob Modify
This module takes a 0-1 knob signal and translates it to the range defined by the H and L signal.  It also will pass the > input when the knob is turned all the way down.

### Knob Switch
This module takes a 0-1 knob signal and turns it into a switch - when the knob is all the way down, it will pass signal A.  When the knob is between 0 and 1, it will pass signal B - this would usually be connected back to the same knob at the k input.  When the knob is all the way up, it will pass signal C.

### Number Maker
This module takes 3 knob signals and uses them to create the 1’s, 10’s, and 100’s digits of a 3 digit number.

### Pulses Per Turn
This module will emit a number of pulses per full turn set by the # input.

### A!=B
Gate if A does not equal B.

### A<=B
Gate if A is less than or equal to B.

### A<B
Gate if A is less than B.

### A==B
Gate if A is exactly equal to B.

### A>=B
Gate if A is greater than or equal to B.

### A>B
Gate if A is greater than B.

### AND
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### Flip-Flop
This is a flipflop module. Flipflops can divide clock pulses and store information.

This module contains a node-by-node tutorial.

Inputs:
g - Clock pulse (0 or 1)

Outputs:
g - Flipflop (0 or 1)

### Gate Smear
Gate Smear keeps a gate high for a longer period of time than normal.  It is great for smoothing modules like the Delta Change Detector, when you only want a high signal during a series of changes rather than many successive high signals.  It is somewhat but not exactly like a debouncer.

### NAND
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### NOR
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### NOT
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### OR
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### Shift Register
A shift register is a series of cascaded flipflops.  This module also provides the inverse of each flipflop for convenience.  It is essentially a clock frequency divider.  

Great module for triggering drums!

### XNOR
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### XOR
A : Top Input
B : Bottom Input

Output 1 if…

and : A and B are both greater than zero.
nand: A and B are not both greater than zero.

or: A or B is greater than zero.
xor: A and B are not simultaneously greater than zero.

nor: A and B are not greater than zero.
xnor: A and B are simultaneously zero or greater than zero.

not: A is not greater than zero.

### 0-99
This module creates integers from 0-99.

### ^ Counter
This module counts up to the number defined by the # input with each gate pulse and then resets to zero.

### ^v Counter
This module counts up or down, or up/down.

### e
This is a convenient package of most of the functions you’d want to accomplish using the special number e.

### Golden Ratio


### Pi
This is a convenient package of most of the functions you’d want to accomplish using the special number pi.

### Audio Peak Detector
This module will output a 1 shot m signal if the audio signal clips.

### Delta Change Detector
This module detects change from one frame to the next (a frame is a chunk of processing time - not the same as a sample).

### Range
This module will clamp the > signal between the H and L values.

### Rectifier
This rectifier provides half and full-wave rectification for any m signal.  It does this by first translating the incoming m signal to an a signal, then rectifying it, then translating it back to an m signal.

### Rectifying Signal Reflector
This module determines which signal is greater than the other and rectifies and returns that signal.  There are also some interesting feedback options to create wild modulation signals from two normal LFOs.

### Return Greater
Passes the greater of the two signals.

### Return Lesser
Passese the lesser of the two signals.

### Sample & Hold
This is a repackaging of the Sample & Hold module in a smaller module.

### Up Down Detector
This module detects when a signal is moving upwards or downwards from one frame to another.

## Mixer
### 2x2 Mixer
This mixer sends two a signals to a L/R output.

### 4x1 Mixer
This mixer combines 4 signals and sends them to an output.

### 8x2 Mixer
This mixer sends 8 a signals to a L/R output.  There are also two send/returns, A and B.

### Curve
This module translates a linear 0-1 m signal to exponential (left) to linear (middle) to logarithmic (right).

### Equal Power XFade
This module fades between inputs A and B in equal power mode - good for fading between audio signals so there is no perceptual drop in volume midway through crossfading.

### Infinite XFade
This module scheme allows you to fade between an arbitrary number of inputs with just one knob turn.

### Level
This is an attenuator, which constrains the outer limits of any signal passing through it.  You can think of it like a volume knob.

### Linear XFade
This is a repackaging of the Crossfader node with a linear response.

### Mapper
This is a repackaging of the Mapper node as a module.  For more info, see the Audulus node documentation.

### Pan
This module pans an audio signal to Left or Right without any loss of volume towards the center of the stereo field.

### Stereo Mixer
This sends a stereo signal to the audio output with volume control and a width control that is mono in the middle and swapped left/right when turned all the way up.

### VCA
VCAs aren’t really necessary in Audulus.  All a VCA is, really, is a signal multiplier.  Usually you’d feed an oscillator into a VCA and use an envelope to control the level of amplification of the oscillator, but this is made unnecessary by basically having a “built-in” VCA on every oscillator module in Audulus.  You can also just attach any modulation signal to an Level module to get cross modulations going.  In fact, if you look inside this module, all it is is a level node.  

So, in short, this is an unnecessary module, but it’s here because people who are used to modular synthesizers expect to need one.  If they read this metadata or just generally get used to the library, they’ll understand why it’s not needed.  Just for fun, there’s a drive control on this for some added distortion.

## Oscillator
### 0 to 1 Saw
This is a small utility LFO meant for driving internal modulations in patches.

### Basic
LFO outputs top to bottom: square, saw, triangle, and sine.  Each output also has an inverted output next to it.  The square wave has pulse width modulation.

### Multishape Tap Tempo
This LFO has square, saw, triangle, and sine waves (and their inverses) as well as 3 different distortion modes and an exponential/linear/logarithmic shaper.  You can also adjust the phase of the sine wave independently as well as the pwm of the square wave.

Also includes a tap tempo module for manually setting the tempo of the LFO.

### Multishape
This LFO has square, saw, triangle, and sine waves (and their inverses) as well as 3 different distortion modes and an exponential/linear/logarithmic shaper.  You can also adjust the phase of the sine wave independently as well as the pwm of the square wave.

### Phase Cancel
This LFO combines sine waves in different phase configurations to create more modulation outputs.

### Rectifying
This LFO products rectified versions of saw, triangle, and sine waves.

### White Noise
This white noise module outputs 3 types of random values - one is bipolar and suitable for audio (a), the next is good for modulation (m) and finally another is a random on/off trigger (g).

### String Exciter
This is a bass synthesizer - only works in the lower octaves.  It uses a delay line to model the action of metal strings.

### 3ceeoh
This is a triple oscillator VCO with a sub octave and octave control and individual detune controls for providing some really fat sounds.  Shape control only works for square and saw.

### Crossfade VCO
This oscillator creates sound by crossfading between two oscillators.

### Fossilator
This VCO uses trigonometry to turn sculpt sine waves into fat analog tones.  All of the controls are very interactive with one another, and respond well to having envelopes applied to them.

### H8TED
A 3 waveform 8bit oscillator

### Wind's Cry
This oscillator simulates wind coming from the four directions blowing through your windows, bamboo, and lost canyons.

## Presets
### 8-Bit Bass


### Bass Guitar
A simulated bass guitar synth.

### Blue Man Bass
A simulated slapped tube organ.

### Byte Bass
Teeth grinding digital bass.

### Duck Bass
Bass that simulates a ducking compressor sound.

### Fossilized Bass
Smoky analog bass.

### Lit Analog Bass
This bass uses a z-1 filter to simulate an analog bass.

### Razor Bass
A bass to slice through the mix.

### Reverse Vacuum Bass


### Sawsall Bass
Sawing filtered bass.

### Split Valve Bass
Bass with a little spittle at the edges.

### Squanchin' Bass
Get yer squanch on with this squanchy squanchin’ bass!

### Stranger Things Wide Bass


### Trance Stab Bass
Queue up this high-q bass for your next trance dance party.

### Cymbal Presets
Presets for the cymbal module.

### It's a Trap!! Presets
Presets for the IT’S A TRAP!! drum machine.

### KarPlus Presets
KarPlus drum module presets.

### Kick Presets
Kick drum presets.

### Res Drum Presets
An example of the breadth of the Res Drum.

### Snare Presets
Snare drum presets.

### Analog Delay + Spring Reverb
A combination of analog delay and spring reverb tuned for guitar.

### Icebox Enveloped Repeater
An auto-looper great for percussive guitar sounds.

### Syncopated Filtered Delay
A highly syncopated triple tap delay.

### Wasp Sting Stab
A stingy stab

### Zipper Echo
Light and airy stab

### Farfiza Fever
A Farfiza organ sound through a guitar amp.

### The Fire Inside
Fire starter!

### Disintegrating Loops
Basinski-inspired warbly tape patch.

### Doom Poly Pad
A dark and dreary pad

### ET Phone Drone
An outerspace pad.

### Sunbaked Sun Ra Pad
Sunbaked cassette tape pad.

### The Order of the Infinite Triangle Pad
An infinite drone of ultimate secrecy.

### Preset - 16
This module allows you to store 16 presets for sixteen knobs.

### Preset - 2
This module allows you to store 16 presets for two knobs.

### Preset - 4
This module allows you to store 16 presets for four knobs.

### Preset - 8
This module allows you to store 16 presets for eight knobs.

### 8x8 RGB Matrix
This is an arrangement of RGB lights in 8*8 for use in your own custom projects.

### Blank Module
This is an arrangement of common labels and inputs/outputs that give you a quick start to making a module.

### Demux - Light
This is a demux light combination for mode switches.

## Sequencer
### Arranger
This is an advanced sequencer meant for arranging many events at the same time.

### Bassic Sequencer
This is a major upgrade to the Bassic Sequencer module - it has a built in quantizer and pattern buffer for sequencing drum hits.

### Chladni Sequencer
The Chladni (klod-nee) Sequencer is a special type of XY sequencer that produces 3 sequences - X, Y, and when X collides with Y.  It is driven by LFOs instead of clocks.  Try attaching the output of the sequencer back to individual steps!

### Euclidean Sequencer
The Euclidean Sequencer is based on a formula developed by Euclid, and describes all sorts of natural human-made rhythms.  Most of the traditional dance beats can be dialed in with the Euclidean sequencer.

### Gate Sum Sequencer
This sequencer is meant to be an add-on for the Bass-ic sequencer - it allows you to trigger drums efficiently and expressively.

### Pattern Buffer
This sequencer is meant to be an add-on for the Bass-ic sequencer - it allows you to trigger drums efficiently and expressively.  It is a collection of Gate Sum Sequencers.

### Random Melody
This module generates a random melody while displaying the chances of each note happening in a bar graph form.  Whenever you change any of the parameters, the chances are recalculated.

### Spline Sequencer
The spline sequencer uses a spline input to drive note selection - just draw on the spline node to change the sequence!

### Strip Sequencer
The Strip sequencer is a minimalistic step sequencer that outputs gates.

## Utility
### Audio Input
This module outputs a mono a signal (combination of L+R signals), or a stereo output.

### Audio Output
This module outputs audio to the left and right channels.  It includes a drive control for adding overall grit.

### Elapsed Time
This translates a timer into hours, minutes, seconds, and milliseconds.

### MIDI In
This MIDI control input gives you control over your Audulus patches with an external keyboard or internal MIDI input (from another program).

### One Frame Pulse
This module will pulse for the duration of 1 frame.

### Scale Quantizer
This module takes a -4 to 4 octave signal and snaps it to a user-defined scale and applies slew to its output.  Notes are turned off when their corresponding knobs are less than halfway.

### Slew Limiter
This module resists the change from one note to another, causing a glide.  It also has two modes - one with equal time between each note, and another where the larger the interval, the longer the slew time is.

### Tap Tempo
This module allows you to manually enter a tempo into a module.

### Demux - 64
A 64 output Demux switch.

### Demux - 8
A repackaging of the Demux switch.

### Mux - 64
A 64 input Mux switch.

### Mux - 8
A repackaging of the Mux switch.

### On-Off Switch
This module is an on/off switch that will pass the > input signal only when the knob signal is greater than .5. 

### Pass Switch
This module is a bank of 4 momentary open switches.  It can be used to temporarily make a connection while pressing a button.

### Probability Switch
This module is triggered at its gate input and will choose between A or B to send to the > output, and will send input A to either A or B, based on the chance set by the A/B knob.

### a2m
Translates an audio signal to a modulation signal.

### BPM2Hz
Translates an BPM signal to a Hz signal.

### dB2Amp
Translates an decibel rating to a amplitude signal.

### FeedbackDelay2Seconds
Translates a feedback delay frame into seconds.

### Hz2BPM
Translates an Hz signal to a BPM signal.

### Hz2Note#
Translates a Hz signal to a note number signal.

### Hz2o
Translates an Hz signal to a octave signal.

### Hz2Seconds
Translates an Hz signal to a seconds.

### Inverter - AC
Inverts a signal across 0.

### Inverter - DC
Inverts a signal across .5.

### m2a
Translates a modulation signal to an audio signal.

### m2m
Translates a modulation signal to a different modulation signal range.

### m2o
Translates a modulation signal to an octave signal.

### m2Rad
Translates a modulation signal to an radian signal.

### Milliseconds2Samples
Translates a millisecond signal to a number of samples.

### Note#2Hz
Translates a Note # signal to an Hz signal.

### Note#2o
Translates a note number signal to an octave signal.

### o2Hz
Translates an octave signal to an Hz signal.

### o2Note#
Translates an octave signal to an note number signal.

### Rad2a
Translates an radian signal to an audio signal.

### Rad2Deg
Translates an radian signal to an degree signal.

### Rad2m
Translates an radian signal to a modulation signal.

### SampleRate2Seconds
Translates the sample rate to seconds.

### Samples2Milliseconds
Translates the sample rate to milliseconds.

### Samples2Seconds
Translates the samples to seconds.

### Seconds2Samples
Translates the seconds to samples.

### Truncate - .0001
Truncate the input number to the ten thousandths place.

### Truncate - .001
Truncate the input number to the thousandths place.

### Truncate - .01
Truncate the input number to hundredths place.

### Truncate - .1
Truncate the input number to the tenths place.

### Lit Via
This is a via with a light indicator.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


### Reverse Via
This is a via tab.  Use it in finished designs where you want to prevent accidental movement.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


### Text Via
This is a text via.  Use it to name a connection.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


### Value Via
This is a value via.  Use it to display the value of its throughput.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


### Via
This is a via tab.  Use it in finished designs where you want to prevent accidental movement.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


### Waveform Via
This is a waveform via.  Use it to display the waveform of its throughput.  A knob is provided as a zoom in/out control.

Vias are connection tabs that are useful for prototyping and clarifying connections in very large patches or designs.

They are good for prototyping because you can use a knob to tune a patch and then easily swap it for a value expression - effectively using it as an internal trim pot.

They are good for clarifying connections because they can route one node’s output across a patch and then hook up to, say, a mux node, rather than having 8 long connections run all the way across the patch adding visual clutter.


## Visual
### Fractal Generator v1
This patch creates fractals!

### Pong v1
This patch is a game of pong! 

### RGB TV
This patch is 64*64 RGB TV!  Attach audio signals to inputs for a cool visualizer!  Works best on the brightness input.

