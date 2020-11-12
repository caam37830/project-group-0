# Checkpoint Report - Group 0

This mideterm checkpoint report has 4 sections:

1. A brief introduction to the SIR model, and notation you will use.  You can use [`SIR.md`](SIR.md), as well as other resources (cite any other resources that contribute to your discussion).
2. A brief description of how you are structuring the Python package `sir`.
3. Report on your preliminary investigations using the agent-based and continuous models.
4. Your proposed variations/improvements for the final project.

## Section 1 - Introduction to SIR model

   The SIR (susceptible-infected-removed) model, contributed by Kermack, W. O., McKendrick, A. G, Ronald Ross and others, was formed in the early twenties and made a big breakthrough in modeling the trend of the possibile disease outbreak as well as providing key information for the public and policymakers regarding severeness and control work. The establishment of the simiplied model is implemented here in this project. Under a fixed homogeneous population, three distinct subpopulations are divided, with `S` representing those who are susceptible, `I` denoting those who are infected and `R` standing for those who have recovered. These groups are divided in a way that during an epidemic, people are interested in the amount of infected patients that can transmit the disease, the number of agents who are immuned against the disease and the portions who are not yet being infected and are susceptible. Denote the sizes of these groups at time t by S(t), I(t), and R(t). Moreover, introduce notation `b` to be the fixed number of interactions that spread the disease per day per infected individual and `k` to be a fixed fraction of the infected subpopulation that recovers per day. Altogether, the SIR model consists of a system of three ordinary differential equations (ODEs) that be written by
   
                $$ \frac{ds}{dt} = -b*s(t)*i(t) $$
                $$ \frac{dr}{dt} = k*i(t) $$
                $$ \frac{di}{dt} = b*s(t)*i(t)- k * i(t) $$,
                
where `s`,`i` and `r` here are the percentage of each group over the total population. 

   Besides a closed population with no social structure, the SIR model also assumes that `R` subpopulation is permanently immuned and the `I` subpopulation is contagious at the moment of infection. Moreover, the model assumes a mass-action mixing, meaning the the the fraction of interactions between `S` and `I` is proportional to the product of their population sizes. In other words, every agent will have equal probability in interacting with every other agents per unit time. This implies that an increase in the size of the subpopulations will lead to an increase in the infections and that `I` and `S` are homogeneously distributed in space. This might be problematic in real-world cases, as people tends to encounter within a small community. While these assumptions can sometimes be strong and adversely affecting the prediction in applications, they can be adjusted and in various forms to bring complexity and create extended SIR models. 



## Section 2 - Decription of sir package

## Section 3 - Preliminary investigations

## Section 4 - Improvements proposal