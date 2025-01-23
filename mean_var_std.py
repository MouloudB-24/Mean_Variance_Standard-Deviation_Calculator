import numpy as np

# mean, variance, standard deviation, max, min, and sum


def calculate(list):
    # Results
    calculations = {
        "mean": "",
        "variance": "",
        "standard deviation": "",
        "max": "",
        "min": "",
        "sum": ""
    }
    # if a list containing less 9 elements
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 Numpy array
    arr = np.array(list).reshape(3, 3)

    # Calculate averages
    averages = []
    averages.append([float(arr[:, 0].mean()), float(arr[:, 1].mean()), float(arr[:, 2].mean())])
    averages.append([float(arr[0, :].mean()), float(arr[1, :].mean()), float(arr[2, :].mean())])
    averages.append(float(arr.mean()))
    calculations["mean"] = averages

    # Calculate variances
    vraiances = []
    vraiances.append([float(arr[:, 0].var()), float(arr[:, 1].var()), float(arr[:, 2].var())])
    vraiances.append([float(arr[0, :].var()), float(arr[1, :].var()), float(arr[2, :].var())])
    vraiances.append(float(arr.var()))
    calculations["variance"] = vraiances

    # Calculate standard deviation
    standard_deviation = []
    standard_deviation.append([float(arr[:, 0].std()), float(arr[:, 1].std()), float(arr[:, 2].std())])
    standard_deviation.append([float(arr[0, :].std()), float(arr[1, :].std()), float(arr[2, :].std())])
    standard_deviation.append(float(arr.std()))
    calculations["standard deviation"] = standard_deviation

    # Calculate maximums
    maximums = []
    maximums.append([int(arr[:, 0].max()), int(arr[:, 1].max()), int(arr[:, 2].max())])
    maximums.append([int(arr[0, :].max()), int(arr[1, :].max()), int(arr[2, :].max())])
    maximums.append(int(arr.max()))
    calculations["max"] = maximums

    # Calculate minimums
    minimums = []
    minimums.append([int(arr[:, 0].min()), int(arr[:, 1].min()), int(arr[:, 2].min())])
    minimums.append([int(arr[0, :].min()), int(arr[1, :].min()), int(arr[2, :].min())])
    minimums.append(int(arr.min()))
    calculations["min"] = minimums

    # Calculate sums
    sums = []
    sums.append([int(arr[:, 0].sum()), int(arr[:, 1].sum()), int(arr[:, 2].sum())])
    sums.append([int(arr[0, :].sum()), int(arr[1, :].sum()), int(arr[2, :].sum())])
    sums.append(int(arr.sum()))
    calculations["sum"] = sums

    return calculations


if __name__ == "__main__":
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
