import{_ as g}from"./_plugin-vue_export-helper-c27b6911.js";import{k as _,o as s,a as l,F as u,l as f,n as k,t as m}from"./index-08bbd940.js";const y={class:"color-palette"},v=["onClick"],C={__name:"dir-color-info",setup(S){const p=_("");function d(){const e=[];for(let o=0;o<=255;o+=41)for(let t=0;t<=255;t+=51)for(let c=0;c<=255;c+=51){const i=h(o,t,c);e.push(i)}const n=[],r=6;for(let o=0;o<e.length;o+=r){const t=e.slice(o,o+r);n.push(t)}return n}function a(e){return e.toString(16).padStart(2,"0")}function h(e,n,r){return console.log(e,n,r),"#"+a(e)+a(n)+a(r)}const x=_(d());return(e,n)=>(s(),l("section",y,[(s(!0),l(u,null,f(x.value,(r,o)=>(s(),l("div",{class:"color-box",key:o},[(s(!0),l(u,null,f(r,(t,c)=>(s(),l("span",{class:"color-item",style:k({backgroundColor:t}),onClick:i=>p.value=t},m(t),13,v))),256))]))),128))]))}},A=g(C,[["__scopeId","data-v-ad7e41f8"]]);export{A as default};
