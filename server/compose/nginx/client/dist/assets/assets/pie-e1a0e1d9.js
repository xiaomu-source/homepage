import{Z as c}from"./ZyEchart-f1a44242.js";import{j as d,G as h,x as p,z as g,o as i,a as m,e as u}from"./index-dca43598.js";import{a as s}from"./util.common-1af15359.js";import"./index-1d2d62c5.js";import"./_plugin-vue_export-helper-c27b6911.js";const y={__name:"pie",setup(b){const o=d(),e=h({key:1,chartOptions:{backgroundColor:s(o.theme.value.infoColor,10),tooltip:{trigger:"item",formatter:"{a} <br/>{b}: {c} ({d}%)"},legend:{data:["Direct","Marketing","Search Engine","Email","Union Ads","Video Ads","Baidu","Google","Bing","Others"]},series:[{name:"Access From",type:"pie",selectedMode:"single",radius:[0,"30%"],label:{position:"inner",fontSize:14},labelLine:{show:!1},data:[{value:1548,name:"Search Engine"},{value:775,name:"Direct"},{value:679,name:"Marketing",selected:!0}]},{name:"Access From",type:"pie",radius:["45%","60%"],labelLine:{length:30},label:{formatter:`{a|{a}}{abg|}
{hr|}
  {b|{b}：}{c}  {per|{d}%}  `,backgroundColor:"#F6F8FC",borderColor:"#8C8D8E",borderWidth:1,borderRadius:4,rich:{a:{color:"#6E7079",lineHeight:22,align:"center"},hr:{borderColor:"#8C8D8E",width:"100%",borderWidth:1,height:0},b:{color:"#4C5058",fontSize:14,fontWeight:"bold",lineHeight:33},per:{color:"#fff",backgroundColor:"#4C5058",padding:[3,4],borderRadius:4}}},data:[]}]}}),r=["Direct","Marketing","Search Engine","Email","Union Ads","Video Ads","Baidu","Google","Bing","Others"],n=()=>{let t=[];for(let a=0;a<r.length;a++){const l={value:Math.round(Math.random()*1e3),name:r[a]};t.push(l)}e.chartOptions.series[1].data=t,e.key+=1};return n(),p(()=>{const t=o.theme;e.chartOptions.backgroundColor=s(t.value.primaryColor,10)}),g(()=>{setInterval(()=>{n()},3e3)}),(t,a)=>(i(),m("section",null,[(i(),u(c,{chartOptions:e.chartOptions,key:e.key,height:"calc(100vh - 130px)"},null,8,["chartOptions"]))]))}};export{y as default};