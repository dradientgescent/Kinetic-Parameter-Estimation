# Kinetic Parameter Estimation 

## This code implements a parameter estimation pipeline for an MAPK cascade

Two algorithms are implmented - A genetic algorithm and the Nelder-Mead Simplex.
These can be used in conjunction for any generic parameter estimation problem.

## Results using only Nelder-Mead simplex
 <figure>
  <figure>
   <img src="./images/NM_only_estimation.png" alt="drawing" width="300"/>
   <figcaption>Top: Solution from estimated parameters; Bottom: Experimental Solution.</figcaption>
  </figure> 
 
  <figure>
   <img src="./images/NM_only_estimation.png" alt="drawing" width="300"/>
   <figcaption>Top: Solution from estimated parameters; Bottom: Experimental Solution.</figcaption>
  </figure> 

</figure> 
## Results using only Genetic Algorithm

 <figure>
  <img src="./images/NM_only_estimation.png" alt="drawing" width="500"/>
  <figcaption>Top: Solution from estimated parameters; Bottom: Experimental Solution.</figcaption>
</figure> 

## Results using both algorithms

While the Nelder-Mead simplex is a good local search heuristic, Genetic Algorithms are good for global search.
It then makes sense to apply these in sucession, getting global estimates from the Genetic Algorithm and fine-tuning these with the Nelder-Mead simplex

<figure>
  <img src="./images/GA%2BNM_estimation1.png" alt="drawing" width="500"/>
  <figcaption>Top: Solution from estimated parameters; Bottom: Experimental Solution.</figcaption>
</figure> 


As can be seen from the image and table, this results in much better parameter estimates.
