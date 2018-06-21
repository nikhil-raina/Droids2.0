import numpy as np
import matplotlib.pyplot as mpl
from sklearn import svm

def make_Meshgrid(x, y, h = 0.2):
    '''
    Creates a grid or a space to plot the points on.
    :param x: Data to base for the x-axis
    :param y: Data to base for the y-axis
    :param h: Stepsize for grid
    :return: xx, yy -> ndarray
    '''

    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    return x, y

def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def makeDiff(labelList, label_dictionary):
    '''
    Function responsible to make the 'diff' list for the for the model classification.
    :param labelList: The dictionary containing a key value pair (atoms : ref_flex)
    :return: a list of the differentiating list
    '''

    diffList = list()
    labels = labelList.split()
    count = 0
    for atoms in labels:
        value = label_dictionary.get(atoms)
        for val in value:
            diffList.append(count)
        count += 1
    return diffList


def classification(X, Y, diff):
    '''
    Function responsible of making the entire set of models. Takes in 2 parameters:
    x-coordinates and y-coordinates.
    :param X: list of x-coordinates
    :param y: list of y-coordiantes
    :param diff: list matching the points, differentiating the groups as a whole.
            eg.
                all 'CA' atom points are indicated with a 0 in the list.
                all 'O' atom points are indicated with a 1 in the list.
                etc...

        -----THE NUMBER OF 'diff' AND 'X', 'Y' SHOULD BE THE SAME-----

    :return: ----
    '''
    C = 1.0  # SVM regularization parameter
    models = (svm.SVC(kernel='linear', C=C),
              svm.LinearSVC(C=C),
              svm.SVC(kernel='rbf', gamma=0.7, C=C),
              svm.SVC(kernel='poly', degree=3, C=C))
    models = (clf.fit(X, Y) for clf in models)

    # title for the plots
    titles = ('SVC with linear kernel',
              'LinearSVC (linear kernel)',
              'SVC with RBF kernel',
              'SVC with polynomial (degree 3) kernel')

    fig, sub = mpl.subplots(2, 2)
    mpl.subplots_adjust(wSpace=0.4, hSpace=0.4)

    xx, yy = make_Meshgrid(X, Y)

    for clf, title, ax in zip(models, titles, sub.flatten()):
        plot_contours(ax, clf, xx, yy,
                      cmap=mpl.cm.coolwarm, alpha=0.8)
        ax.scatter(X, Y, c=diff, cmap=mpl.cm.coolwarm, s=20, edgecolors='k')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xlabel('Sepal length')
        ax.set_ylabel('Sepal width')
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)

    mpl.show()
    return None
