## PBIL algorithm

In PBIL, genes are represented as real values in the range [0,1], indicating the probability that any particular allele appears in that gene.

**The PBIL algorithm is as follows:**   
1.A population is generated from the probability vector.  
2.The fitness of each member is evaluated and ranked.  
3.Update population genotype (probability vector) based on fittest individual.  
4.Mutate.  
5.Repeat steps 1–4  

PBIL can use either positive learning or negative learning to update probability vector. In positive learning the probability vector is moved towards the best solution vector and in negative learning the probability vector moves away from the worst solution vector. Typical value of learning rate lies between 0.1 and 0.4. The mutation probability is low as too high mutation rate prevents population to converge to any optimum solution
