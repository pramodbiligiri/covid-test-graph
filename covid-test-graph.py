#!/usr/bin/env python
# Program that plots a graph that shows how accuracy of a Covid test improves
# as a larger fraction of the population gets infected
# Uses matplotlib

import matplotlib.pyplot as plt

# Assuming Specificity and Sensitivity values from Cellex Antibody test
# https://www.centerforhealthsecurity.org/resources/COVID-19/serology/Serology-based-tests-for-COVID-19.html 
# (search for Cellex)
missed=0.062
falsePositive=0.044

totalPopulation = 1400000000 # India's population is 1.4 billion
maxInfectedFraction = 0.4 # Stop drawing the graph beyond this point

infectedPopulation = [i for i in range(100000, totalPopulation, 1000000)]

# Graph different sample sizes, to emphasize that it doesn't make a difference
# because perfectly random sample is assumed
sampleSizes=[100000,1000000,2000000,10000000,20000000,100000000]

for sampleSize in sampleSizes:
    X = []
    Y = []
    for actualInfected in infectedPopulation:
        infectedFraction = float(actualInfected) / totalPopulation
        if infectedFraction >= maxInfectedFraction:
            break    
        infectedInSample = infectedFraction * sampleSize
        testedTruePositivePopulation = infectedInSample * (1.0-missed)
        testedFalsePositivePopulation = (sampleSize - testedTruePositivePopulation) * falsePositive
        successPercentage = float(100 * infectedInSample) / (testedTruePositivePopulation + testedFalsePositivePopulation)
        X.append(100 * infectedFraction)
        Y.append(successPercentage)
    plt.plot(X,Y, label="sample size = " + str(sampleSize))

plt.title("Accuracy of a disease test (with 6.2% misses and 4.4% false positives) ")
plt.xlabel("Percentage of population that is infected")
plt.ylabel("Probability that Positive Tested person is Infected")

plt.legend()
plt.show()
