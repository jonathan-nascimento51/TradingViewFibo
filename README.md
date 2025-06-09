# TradingView Fibo/Fractal Indicators

This repository contains a set of Pine Script files used to plot Fibonacci levels
and fractal information on TradingView charts. The main indicator is
`fiboFractais.pine` which relies on several custom libraries.

## Files

| File | Purpose |
| ---- | ------- |
| `fiboFractais.pine` | Main indicator combining fractal detection, Fibonacci levels and drawing. |
| `BiasUtils_library.pine` | Provides bias filtering based on moving average crossover. |
| `DrawingHelpers_library.pine` | Helper routines for drawing Fibonacci lines, labels and zones. |
| `FiboUtils_library.pine` | Maths utilities for Fibonacci weights, z-score and cluster management. |
| `FractalUtils_library.pine` | Utilities for recording fractal points and distance calculations. |
| `SwingDetection_library.pine` | Detects swing points and determines Fibonacci mode. |

## Loading in TradingView

1. **Create the libraries**
   - In TradingView open the Pine Script editor and create a new script for each
     `*_library.pine` file. The first line of each library defines its name, for
     example `library('BiasUtils', overlay=false)`.
   - Save the script under your account and publish it as a library (public or
     invite only). Note the version number assigned by TradingView.

2. **Import the libraries**
   - In the main indicator (`fiboFractais.pine`) update the `import` statements
     with your TradingView username and the published library version. The file
     currently imports them as:
     ```pine
     import joostraders/FractalUtils/1 as fractals
     import joostraders/FiboMath/1 as fibomath
     import joostraders/SwingDetection/5 as swing
     import joostraders/DrawingHelpers/1 as draw
     import joostraders/BiasUtils/1 as bias
     ```
   - Replace `joostraders` with your TradingView username and the version
     numbers with the ones from your published libraries.

3. **Add the indicator**
   - Create a new script in TradingView and paste the contents of
     `fiboFractais.pine`.
   - Save and add the script to the chart. When the libraries are published and
     the `import` paths are correct the indicator will plot Fibonacci levels,
     fractal points and additional diagnostics.

## Example

Below is a simple screenshot illustrating the indicator output (blue dashed lines
represent Fibonacci levels).

![Example output](docs/indicator_sample.png)

The indicator draws Fibonacci retracements or extensions based on detected
swings while colouring the lines according to their weight and cluster
confluence.
