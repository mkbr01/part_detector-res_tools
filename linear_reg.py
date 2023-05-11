import numpy as np

def linreg(x, y, sigma):
    # Load data from file
    m = np.loadtxt('...')
    x = m[:, 0]
    y = m[:, 1]
    sigma = 0.924  # Update with your desired value

    # Evaluate various sigma sums
    sigmaTerm = sigma ** (-2)
    s = np.sum(sigmaTerm)
    sx = np.sum(x * sigmaTerm)
    sy = np.sum(y * sigmaTerm)
    sxy = np.sum(x * y * sigmaTerm)
    sxx = np.sum((x ** 2) * sigmaTerm)
    denom = s * sxx - sx ** 2

    # Compute intercept a_fit[0] and slope a_fit[1]
    a_fit = np.zeros(2)
    a_fit[0] = (sxx * sy - sx * sxy) / denom
    a_fit[1] = (s * sxy - sx * sy) / denom

    # Compute error bars for intercept and slope
    sig_a = np.zeros(2)
    sig_a[0] = np.sqrt(sxx / denom)
    sig_a[1] = np.sqrt(s / denom)

    # Evaluate curve fit at each data point and compute Chi^2
    yy = a_fit[0] + a_fit[1] * x
    chisqr = np.sum(((y - yy) / sigma) ** 2)

    return a_fit, sig_a, yy, chisqr
