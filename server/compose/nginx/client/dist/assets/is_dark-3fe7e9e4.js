import{I as c,_ as r}from"./github-31e6f70a.js";const e=n=>{const{r:t,g:o,b:a}=c.parse(n),s=.2126*r.channel.toLinear(t)+.7152*r.channel.toLinear(o)+.0722*r.channel.toLinear(a);return r.lang.round(s)},i=e,l=n=>i(n)>=.5,u=l,h=n=>!u(n),L=h;export{L as i};
