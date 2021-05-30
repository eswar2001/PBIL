## PBIL algorithm

In PBIL, genes are represented as real values in the range [0,1], indicating the probability that any particular allele appears in that gene.

**The PBIL algorithm is as follows:**   
1.A population is generated from the probability vector.  
2.The fitness of each member is evaluated and ranked.  
3.Update population genotype (probability vector) based on fittest individual.  
4.Mutate.  
5.Repeat steps 1–4  

PBIL can use either positive learning or negative learning to update probability vector. In positive learning the probability vector is moved towards the best solution vector and in negative learning the probability vector moves away from the worst solution vector. Typical value of learning rate lies between 0.1 and 0.4. The mutation probability is low as too high mutation rate prevents population to converge to any optimum solution


### Note That the algorithm applies the following attacks all at once.
```
blur  
rotate90  
rotate180  
chop5  
chop10  
chop30  
saltnoise  
randline  
cover  

WaterMark PSNR,NCC: 21.60420449520917
0.9360768061019853
Host PSNR,NCC: 51.14947582010238
0.9999912892641288
```
Host  
<img src="https://github.com/eswar2001/PBIL/blob/main/samples/Host%20after%20Resizing.png" width="300" height="300">  
WaterMark  
<img src="https://github.com/eswar2001/PBIL/blob/main/samples/Watermark%20after%20Resizing.png" width="300" height="300">  
Host after PBIL  
<img src="https://github.com/eswar2001/PBIL/blob/main/samples/ImageAfterPBIL.png" width="300" height="300">  
Extracted WaterMatk  
<img src="https://github.com/eswar2001/PBIL/blob/main/samples/Extractedwatermarked.png" width="300" height="300">
