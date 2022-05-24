import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit


FILE = 'results.png'

EMISSION_INTENSITIES = [69, 79, 75, 84, 104, 110, 109, 113, 73, 82, 101, 87, 81, 95, 77]
EMISSION_INTENSITY_FILTER_THRESHOLD = 75

DISTANCE_INTERVAL = 1
LOWER_BOUND = -10
UPPER_BOUND = 25


def gaussian_model(x, a, x0, sigma):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


def filter_data(x, y):
    filtered_x = []
    filtered_y = []

    for x, y in zip(x, y):
        if y >= EMISSION_INTENSITY_FILTER_THRESHOLD:
            filtered_x.append(x)
            filtered_y.append(y)

    return filtered_x, filtered_y


def main():
    # Store the data
    x = range(0, DISTANCE_INTERVAL * len(EMISSION_INTENSITIES), DISTANCE_INTERVAL)
    y = EMISSION_INTENSITIES

    # Throw out noisy data
    x, y =  filter_data(x, y)

    # Initialize the figure
    fig = plt.figure()
    ax = plt.gca()

    # Fit the model and calculate the predicted y data
    popt, _ = curve_fit(gaussian_model, x, y, maxfev=5000)
    predicted_x = range(DISTANCE_INTERVAL * LOWER_BOUND, DISTANCE_INTERVAL * UPPER_BOUND, DISTANCE_INTERVAL)
    print(list(predicted_x))
    predicted_y = gaussian_model(predicted_x, popt[0], popt[1], popt[2])

    # Calculate the half maximum value
    mean = popt[1]
    maximum = gaussian_model(mean, popt[0], popt[1], popt[2])
    half_maximum = maximum / 2
    print("HM", half_maximum)

    # Calculate the full width maximum value
    spline = UnivariateSpline(predicted_x, predicted_y - np.max(predicted_y) / 2, s=0)
    root1, root2 = spline.roots() 
    full_width_half_maximum = abs(root2 - root1)
    print("FWHM:", full_width_half_maximum)

    # Plot the data, the model, and the full width half maximum
    ax.scatter(x, y)
    ax.plot(predicted_x, predicted_y, c='r', label='Gaussian Model')
    plt.axvspan(root1, root2, facecolor='g', alpha=0.5)
    plt.axhline(y=half_maximum, color='g', linestyle='-')

    # Add labels and text to the plot
    plt.xlabel("x (nm)")
    plt.ylabel("Emission Intensity")
    ax.text(0.4, 0.05, f'FWHM = {full_width_half_maximum}', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=16)

    # Save the figure
    fig.savefig(FILE)


if __name__ == '__main__':
    main()
