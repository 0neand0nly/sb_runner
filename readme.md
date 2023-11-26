# SA4ByteBERT


## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Notes](#notes)

## About <a name = "about"></a>

SA4ByteBERT (Static Analzyers for ByteBERT) is collection of tools that team BKJ used for comparative reserach. It consists of multiple static anaylzers and machine learning SWs. The main purpose of these tools were to run static analysis on the dataset and to compare the result with our pre-trained ByteBERT.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

- Java 17.0.9
- [spotbugs - 4.8.0](https://spotbugs.readthedocs.io/en/stable/installing.html)
- [weka 3.8](https://waikato.github.io/weka-wiki/downloading_weka/)
- python 3.11.5

```
You must download java and python to run tools which are related to this project. We have used weka 3.8 however it is okay to download higher version of it. spotbug is provided in the repository
```

## Usage <a name = "usage"></a>

### 1. Spotbug runner

if you wish to run spotbug analysis you can checkout the **Spotbug_runner** directory and you make run static analysis by using below command 

```
$python spotbug_runner.py ./path/to_run/analysis
```
It will then generate spotbug reports in xml format within the same directory. You can use for the input for spotbugs GUI. 


### 2. Mali_counter 
Mali_counter is used to count all the spotbug reports that contains category of "MALICIOUS_CODE"

```
$python Mali_counter.py ./path/to_run/analysis
```
By running above command it will return the total number of files that were reviewed and also the number of malicious reports.

### 3. Snyk_runner
To double check the validity of spotbugs analyzer we have used another static analyzer named **Snyk**. By using bellow command you will be able to run static analysis using Snyk. It will provide you with the result in the CLI

```
$python snyk_runner.py ./path/to_run/analysis
```

## Notes <a name = "note"></a>

We left our result using the Weka in the Weka_results directory.