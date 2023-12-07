import{_ as x,r as l,o as I,a as p,c as v,b as e,n as b,p as C,d as O,u as E,F as P,e as V,t as w,f as W,g as D,w as F,h as G,i as S,j as m,k as g,l as T,m as R}from"./index-d24bb3a3.js";import{u as N}from"./menus-34c7fcd3.js";import{s as y}from"./setting-27ac477a.js";const z=c=>(C("data-v-643806b3"),c=c(),O(),c),U=z(()=>e("div",{class:"cursor",id:"cursor"},null,-1)),Y={class:"cursor2",id:"cursor2"},A={class:"go-top-progress-wrap"},q={class:"progress-circle svg-content",width:"100%",height:"100%",viewBox:"-1 -1 102 102"},Q=z(()=>e("i",{class:"iconfont icon-top"},null,-1)),j=[Q],J={__name:"ZyGoTop",setup(c){const i=l(!1),u=l(null),s=l(0),f=()=>{i.value=window.scrollY>300},d=()=>{window.scrollTo({top:0,behavior:"smooth"})},o=()=>{let t=u.value;s.value=t.getTotalLength(),t.style.transition=t.style.WebkitTransition="none",t.style.strokeDasharray=s.value+" "+s.value,t.style.strokeDashoffset=s.value,t.getBoundingClientRect(),t.style.transition=t.style.WebkitTransition="stroke-dashoffset 10ms linear"},_=()=>{let t=window.scrollY,r=document.documentElement.scrollHeight-window.innerHeight;u.value.style.strokeDashoffset=s.value-t*s.value/r};return I(()=>{window.addEventListener("scroll",f),o(),_(),document.addEventListener("scroll",_)}),(t,r)=>(p(),v("section",{style:b({opacity:i.value?1:0})},[U,e("div",Y,[e("div",A,[(p(),v("svg",q,[e("path",{ref_key:"progressPathRef",ref:u,d:"M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98"},null,512)]))])]),e("div",{class:"cursor3",id:"cursor3",onClick:d},j)],4))}},K=x(J,[["__scopeId","data-v-643806b3"]]);const X={class:"menu"},ee=["onMouseover","onMouseleave","onClick"],te={__name:"ZyMenuList",setup(c){const i=E(),u=N(),s=[{name:"HOME",id:"home"},{name:"ABOUT",id:"about"},{name:"RESUME",id:"resume"},{name:"BLOG",id:"blog",path:"/blog"},{name:"PORTFOLIO",id:"work",path:"/portfolio"},{name:"CONTACT",id:"contact",path:"/contact"}],f=l(0),d=l(0),o=l(0),_=l(0),t=l(0),r=l([]),L=l(null),B=()=>{const n=r.value[f.value];n&&(d.value=n.offsetLeft,o.value=n.offsetTop,_.value=n.offsetWidth,t.value=n.offsetHeight)},Z=n=>{const a=r.value[n];a&&(d.value=a.offsetLeft,o.value=a.offsetTop,_.value=a.offsetWidth,t.value=a.offsetHeight)},$=(n,a)=>{f.value=n;const h=r.value[n];h&&(d.value=h.offsetLeft,o.value=h.offsetTop,_.value=h.offsetWidth,t.value=h.offsetHeight),a&&(a.path?i.push(a.path):u.page=a.id)};return I(()=>{r.value=[...L.value],$(0)}),(n,a)=>(p(),v("div",X,[(p(),v(P,null,V(s,(h,k)=>e("div",{key:k,class:W(["menu-item",{active:f.value===k}]),onMouseover:M=>Z(k),onMouseleave:M=>B(),onClick:M=>$(k,h),ref_for:!0,ref_key:"menuItem",ref:L},w(h.name),43,ee)),64)),e("div",{class:"overlay",style:b({top:o.value+"px",left:d.value+"px",width:_.value+"px",height:t.value+"px"})},null,4)]))}},oe=x(te,[["__scopeId","data-v-62ae5247"]]);const H=c=>(C("data-v-1619ef18"),c=c(),O(),c),se={class:"zy-layout-all-group",id:"zy-layout-all-group",ref:"layoutGroup"},ne={class:"header-logo"},ae={class:"header-right"},le={class:"zy-theme-container-main",id:"zy-theme-container-main"},ce={key:1,class:"main-footer",ref:"layoutFooter"},re={class:"main-info"},ie={class:"info-item"},ue=H(()=>e("div",{class:"item-title"},"微信",-1)),de={class:"info-item"},_e=H(()=>e("div",{class:"item-title"},"QQ",-1)),he={key:0,class:"copyright"},pe=["href"],ve={target:"_blank",class:"out-link",href:"https://beian.miit.gov.cn/#/Integrated/index"},fe={__name:"index",setup(c){const i=E(),u=l(!0),s=D({lastScrollTop:0,show:{menuList:!0}});F(i.currentRoute,o=>{s.show.menuList=o.path==="/index"});const f=()=>{i.push("/index")},d=()=>{let o=window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop;o===0?u.value=!0:u.value=o<s.lastScrollTop,s.lastScrollTop=o};return I(()=>{window.addEventListener("scroll",d)}),G(()=>{window.removeEventListener("scroll",d)}),(o,_)=>{const t=S("RouterView"),r=S("a-image");return p(),v("main",se,[m(i).currentRoute.value.path==="/index"?(p(),v("section",{key:0,class:"zy-theme-header",style:b({top:u.value?0:"-100%"})},[e("div",ne,[e("span",{class:"logo-text",onClick:f},w(m(y).websiteInfo.name||"ZHOU YI"),1)]),e("div",ae,[g(oe)])],4)):T("",!0),e("section",le,[g(t),g(K)]),m(i).currentRoute.value.path==="/index"?(p(),v("footer",ce,[e("div",re,[e("div",ie,[ue,g(r,{width:80,src:"http://www.askme.do/public/wx.png"})]),e("div",de,[_e,g(r,{width:90,src:"http://www.askme.do/public/qq.png"})])]),m(y).reference.show?(p(),v("div",he,[R(w(` Copyright ©${new Date().getFullYear()} by`)+" ",1),e("a",{target:"_blank",class:"out-link",href:m(y).reference.authorizationUrl}," @"+w(m(y).reference.authorization),9,pe),R(". All rights reserved. | "),e("a",ve,w(m(y).reference.number),1)])):T("",!0)],512)):T("",!0)],512)}}},we=x(fe,[["__scopeId","data-v-1619ef18"]]);export{we as default};
