from scipy.stats import norm


def dnorm(x,mean=0,sd =1):
    
    result=norm.pdf(x,loc=mean,scale=sd)
    return result

x= 0

print(dnorm(x,mean=0,sd = 1))
