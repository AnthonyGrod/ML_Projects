# ML_Projects
Set of my private and university ML course problems. Tasks which I have solved are given below:

1. Chi squared test
Problem 5c (Chi-square independence test).

    You are given the results of IPSOS exit polls for 2015 parliamentary elections in Poland in table **data**. Decide if we can assume that gender and voting preferences are independent. To this end:
    Compute row totals $r_i$, column totals $c_j$, and overall total $N$.
    If the variables are independent, we expect to see $f_{ij} = r_i c_j / N$ in $i$-th row $j$-th column.
    Compute the test statistic as before, i.e. \n
    $S = \\sum_{ij} \\frac{\\left(f_{ij}-X_{ij}\\right)^2}{f_{ij}}.$ \n
    Again test vs $\\chi^2$ CDF. However, if the variables are independent, we only have $(r-1)(c-1)$ degrees of freedom here (we only need to know the row and column totals).
    The KORWiN party looks like an obvious outlier. Note, when we work with categorical variables we should not just remove a category -- it is better to aggregate them. Introduce an aggregated category by summing the votes for the parties with less than 5% total votes and repeat the experiment.
  

