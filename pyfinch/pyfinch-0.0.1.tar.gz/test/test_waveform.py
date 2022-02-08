from pyfinch.analysis import get_half_width
from pyfinch.analysis import *
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from util.draw import remove_right_top

# Waveform timestamp

sample_rate = 30000

wf_ts = np.array([0., 0.03333333, 0.06666667, 0.1, 0.13333333,
                  0.16666667, 0.2, 0.23333333, 0.26666667, 0.3,
                  0.33333333, 0.36666667, 0.4, 0.43333333, 0.46666667,
                  0.5, 0.53333333, 0.56666667, 0.6, 0.63333333,
                  0.66666667, 0.7, 0.73333333, 0.76666667, 0.8,
                  0.83333333, 0.86666667, 0.9, 0.93333333, 0.96666667,
                  1., 1.03333333])

# Waveform amplitude
avg_wf = np.array([-9.91791626e-01, -8.55132914e-01, -1.02833678e+00, 8.01205079e-02,
                   4.74665806e+00, 3.86554012e+00, -2.74373732e+01, -1.10136806e+02,
                   -2.17142476e+02, -2.38522371e+02, -1.54319306e+02, -2.80894907e+01,
                   8.17856855e+01, 1.51194696e+02, 1.76124484e+02, 1.68719967e+02,
                   1.44641930e+02, 1.14128504e+02, 8.25849625e+01, 5.38338621e+01,
                   2.95948129e+01, 1.07553402e+01, -2.64718039e+00, -1.17432163e+01,
                   -1.71871690e+01, -1.88745941e+01, -1.89317849e+01, -1.82560554e+01,
                   -1.70392679e+01, -1.53594069e+01, -1.32369995e+01, -1.14193823e+01])

interp_factor = 100  # factor by which to increase the sampling frequency
f = interpolate.interp1d(wf_ts, avg_wf)
wf_ts_new = np.arange(0, wf_ts[-1], ((wf_ts[1] - wf_ts[0]) * (1 / interp_factor)))
assert (np.diff(wf_ts_new)[0] * interp_factor) == np.diff(wf_ts)[0]
avg_wf_new = f(wf_ts_new)  # use interpolation function returned by `interp1d`

deflection_range, half_width = get_half_width(wf_ts, avg_wf)
deflection_range_new, half_width_new = get_half_width(wf_ts_new, avg_wf_new)

fig, ax = plt.subplots()
ax.plot(wf_ts, avg_wf, 'ko')
ax.plot(wf_ts_new, avg_wf_new, 'b')
ax.legend(['raw', 'interp'])

for ind in deflection_range_new:
    ax.axvline(x=wf_ts_new[ind], color='r', linewidth=1, ls='--')

plt.text(0.8, avg_wf.max() * 0.6, 'Half width = {:.2f} µs'.format(half_width_new), fontsize=12)  # measured from the peak deflection

remove_right_top(ax)

plt.show()
