# Developing a Comprehensive Taxonomy for REST API Faults: Insights from Real-World Bug Reports

## Authors: [Aakash Kulkarni, Soon Song Cheok, Shreyes Joshi]


## Abstract

The increasing reliance on REST APIs in modern web applications has highlighted the need for effective fault localization techniques. Existing taxonomies for REST API faults, primarily based on automated test generation tools, focus on error messages and status codes. However, these taxonomies often fail to account for real-world issues that can occur in REST APIs, leading to a gap in fault classification. In this study, we analyze real-world bug reports from GitHub to develop a comprehensive taxonomy that encompasses a wider range of fault types. By examining 24 bug reports, we identified 12 distinct categories of faults that are not adequately represented in current taxonomies. Our findings indicate that combining test suite-based taxonomies with bug report-based taxonomies can bridge the gap, providing a more holistic understanding of faults in REST APIs. This new taxonomy aims to enhance fault localization, improve API robustness, and better align with real-world scenarios encountered by developers. Alongside this taxonomy, we created a benchmark for evaluating these 24 bugs, which are real-world bugs.


## Introduction

REST APIs (Representational State Transfer) have become backbone of the modern web and cloud applications. 
They facilitate seamless interactions between client and server through stateless communication, enabling services to be scalable, reliable, and easily integrateable. 
Basically, REST APIs are a set of rules and standards  defined by OpenAPI used to enable communication between different software applications over the internet. They are built around the use of standard HTTP methods such as GET, POST, PUT, and DELETE to interact with resources, which are any kind of data or service that can be named on a network.
Given their critical role, the effective identification and resolution of faults within REST APIs remain a significant challenge ~\cite{barbir2007}, prompting the need for research on how well the existing taxonomy align with real-world scenarios.

As systems that rely on REST APIs grow in scale and complexity , minor faults can escalate into major disruptions, impacting user experience and business operations. 
So it is important to understand the real-world faults, but there are many faults that can be existing in the context of REST APIs. And we need a detailed taxonomy to cluster these real-world bugs into meaningful categories. So, that we can prioritize and diagnose the critical faults in REST APIs.

Our initial assumption was that the existing taxonomy, developed from automated test generation tools, would align well with real-world bug reports from GitHub. 
To empirically test this assumption, we conducted a study analyzing a set of bug reports from various REST API projects on GitHub. 
Our findings revealed that the existing taxonomy failed to account for real world issues that can occur under successful response codes (e.g., 200 OK). Also, the paper "On the Faults Found in REST APIs by Automated Test Geneation" ~\cite{automatedTestTaxonomy} was limited to the test suite based results and they made a taxonomy based on those results. 
This significant misalignment between the test suite based taxonomy and with real world bugs highlighted the need for a new, comprehensive taxonomy.


Given the shortcomings of the existing taxonomy, our primary objective was to develop a new taxonomy that better represents the faults encountered in real-world scenarios. 
Alongside this taxonomy, we aimed to create a benchmark for evaluating these faults, providing a structured framework for assessing and improving REST API reliability.

And the combining the test-suite based taxonomy and the bug report-based taxonomy, we created a comprehensive taxonomy that encompasses a wider range of faults. 
This new taxonomy aims to provide a more holistic understanding of faults in REST APIs, improving API robustness, and better align with real-world scenarios.


Our Assumptions:
1. We assume that the findings and the new taxonomy can be generalized to other REST API projects beyond the ones specifically analyzed in this study.
2. We assume that the new taxonomy will provide better diagnostic capability for developers, allowing them to identify, categorize, and prioritize faults more effectively.




The motivation for this research stems from the critical need to address the gap between theoretical fault models derived from automated test generation tools and the practical issues encountered in real-world REST API applications. 
Existing taxonomies primarily focus on certain types of errors, such as 500-based errors, and often fail to account for faults that occur under successful response codes like 200 OK. 
This misalignment limits the ability of developers to effectively diagnose, categorize, and prioritize faults. By creating a new, comprehensive taxonomy based on real-world bug reports, we aim to provide a more accurate and practical framework for understanding REST API faults. 
This taxonomy will enhance  fault understanding process, improve system reliability, and better support developers in maintaining robust and resilient REST API-based systems.

To guide our investigation and address the identified gaps, we formulated the following research questions:

RQ1: What categories of faults are most prevalent in real-world REST API bug reports?
RQ2: How does the new taxonomy improve our understanding and classification of REST API faults compared to the existing taxonomy?



For the evaluation dataset, we will manually select the issues from the GitHub services and their fixes from REST API projects that utilize Spring Boot or Jersey frameworks. These GitHub services are used in the paper  "Generating REST API Specifications through Static Analysis" by Manish et al. This dataset will encompass various categories of faults identified in REST APIs. By analyzing repositories and commit histories, we will extract specific instances where bugs have been documented and subsequently fixed. 


Our analysis of bug reports led us to create a benchmark of 24 bugs which were classified with a taxonomy based on bug reports.

> To read our full findings, here is the pdf version of the whole paper: [pdf](https://github.com/aakashkulkarni36/CS563-Project/blob/main/CS563-Project/Paper/paper.pdf)



