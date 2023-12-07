import{_ as K,Z as U,a as x,T,c as L,b as X}from"./util.time-c6be59b0.js";import{G as R,k as V,r as b,o,a as r,c as l,w as s,I as W,Z,H as G,g as w,t as d,d as J,f as i,W as F,X as Q,p as ee,m as te,Y as ne,F as C,_ as M,y as p,e as A,b as oe,$ as O,l as N}from"./index-d5fdc465.js";import{a as $}from"./server-73acdb05.js";import{Z as se}from"./ZySearchForm-0a7e225a.js";import{_ as Y}from"./_plugin-vue_export-helper-c27b6911.js";import"./axios-707ed124.js";const ae=e=>$.post("/v1/blog/messages/get-list/",e),ie=e=>$.post("/v1/blog/messages/create-message/",e),le=e=>$.post("/v1/blog/messages/update-message/",e),ce=e=>$.post("/v1/blog/messages/delete-message/",e),me=e=>$.post("/v1/blog/messages/client/reply/",e),re=e=>$.post("/v1/blog/messages/client/like/",e),de=e=>$.post("/v1/blog/messages/client/opposeNum/",e),ue={class:"zy-get"},fe={__name:"get-messages-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(e,{emit:t}){const a=e,c={style:{width:"100px"}},_={span:14},h=R({form:{}}),k=V(),y=V(!a.updateData);y.value||(h.form=a.updateData||{});const D=async()=>{try{const u=await k.value.validateFields();y.value||delete h.form.password,(y.value?ie:le)(W(h.form)).then(n=>{Z.success("操作成功"),t("close",!0)}).catch(n=>{Z.error(n||"操作失败")})}catch(u){console.log("Failed:",u)}},S=()=>{G("还没保存数据，确认退出?").then(u=>{u&&t("close")})};return(u,f)=>{const n=b("a-textarea"),m=b("a-form-item"),v=b("a-form");return o(),r("section",ue,[l(v,{model:h.form,class:"zy-form","label-col":c,ref_key:"formRef",ref:k,"wrapper-col":_},{default:s(()=>[l(m,{label:"留言内容",name:"content",rules:[{required:!0,message:"请输入留言内容!"}]},{default:s(()=>[l(n,{value:h.form.content,"onUpdate:value":f[0]||(f[0]=g=>h.form.content=g),allowClear:"",placeholder:"请输入留言内容",rows:4},null,8,["value"])]),_:1})]),_:1},8,["model"]),l(K,{onSave:D,onClose:S})])}}},pe={class:"zy-view"},ge={__name:"view-messages-info",props:{viewData:{type:Object,default:()=>{}}},emits:["close"],setup(e,{emit:t}){return(a,c)=>(o(),r("section",pe,[l(x,null,{default:s(()=>[l(U,{label:"留言内容"},{default:s(()=>[w(d(e.viewData.content),1)]),_:1})]),_:1}),l(x,null,{default:s(()=>[l(U,{label:"是否隐藏"},{default:s(()=>[w(d(e.viewData.hidden),1)]),_:1})]),_:1}),l(x,null,{default:s(()=>[l(U,{label:"关联的用户ID"},{default:s(()=>[w(d(e.viewData.user),1)]),_:1})]),_:1}),l(x,null,{default:s(()=>[l(U,{label:"replies"},{default:s(()=>[w(d(e.viewData.replies),1)]),_:1})]),_:1}),l(x,null,{default:s(()=>[l(U,{label:"留言创建时间"},{default:s(()=>[w(d(e.viewData.createdAt),1)]),_:1})]),_:1}),l(x,null,{default:s(()=>[l(U,{label:"updatedAt"},{default:s(()=>[w(d(e.viewData.updatedAt),1)]),_:1})]),_:1})]))}};const he=e=>(ee("data-v-ce3ed6f5"),e=e(),te(),e),_e={class:"zy-form"},ye=he(()=>i("div",{class:"text-center"},[i("button",{type:"submit",class:"site-btn","data-wow-delay":"0.2s",id:"send-form"},"Send Massege ")],-1)),ve={__name:"ZyForm",props:{defaultUser:{type:Object}},emits:["submit-form"],setup(e,{emit:t}){const a=J.get("userInfo"),c=R({form:{name:"",email:"",website:"",content:""}});a&&(c.form.name=a.nickname,c.form.email=a.email,c.form.website=a.website);const _=h=>{h.preventDefault(),t("submit-form",c.form)};return(h,k)=>(o(),r("section",_e,[i("form",{onSubmit:_,class:"cont-form",id:"contact-form",method:"POST"},[F(i("textarea",{id:"massage","onUpdate:modelValue":k[0]||(k[0]=y=>c.form.content=y),required:"",placeholder:"留言内容"},null,512),[[Q,c.form.content]]),ye],32)]))}},E=Y(ve,[["__scopeId","data-v-ce3ed6f5"]]),j=function(e,t,a){let c="";if(a){const _=new Date;_.setTime(_.getTime()+a*24*60*60*1e3),c=`; expires=${_.toUTCString()}`}document.cookie=`${e}=${encodeURIComponent(t)}${c}; path=/`},B=function(e){const t=document.cookie.split("; ").find(a=>a.startsWith(`${e}=`));return t?decodeURIComponent(t.split("=")[1]):null};const ke={key:0,class:"comment"},we=["href"],be={class:"nickname"},Ie={key:0,class:"author"},Ce=["href"],De={class:"nickname"},Se={key:0,class:"author"},$e=["href"],Ue={class:"nickname"},xe={key:0,class:"author"},Ae=["href"],qe={class:"nickname"},Re={key:0,class:"author"},Te=["href"],Ze={class:"nickname"},Fe={key:0,class:"author"},ze=["href"],Le={class:"nickname"},Ve={key:0,class:"author"},Me={class:"date"},Oe={class:"reply-box"},Ne={class:"reply-box"},P={__name:"ZyComment",props:{comment:{type:Object},pid:{type:String}},emits:["reply","like","oppose","delete","edit"],setup(e,{emit:t}){const a=e,c=R({show:{replies:!1},likeActive:B(`admin-comment-like-${a.comment._id}`),opposeActive:B(`admin-comment-oppose-${a.comment._id}`)}),_=u=>{c.likeActive||(c.likeActive=!0,t("like",u))},h=u=>{c.opposeActive||(c.opposeActive=!0,t("oppose",u))},k=()=>{c.show.replies=!c.show.replies},y=u=>{t("delete",{_id:u,pid:a.pid})},D=u=>{t("edit",{...a.comment,pid:a.pid})},S=u=>{let f={...a.comment,pid:a.pid};t("reply",[f,u])};return(u,f)=>{const n=b("a-popover"),m=b("a-image"),v=b("a-comment"),g=ne("permission");return e.comment.userInfo.length?(o(),r("section",ke,[l(v,{id:"comment-"+e.comment._id},{actions:s(()=>[i("span",null,"来自："+d(e.comment.userInfo[0].userIp||"未知"),1),i("span",null,"城市："+d(e.comment.userInfo[0].address||"未知"),1),i("span",null,"操作平台："+d(e.comment.userInfo[0].platform||"未知"),1),e.comment.toUser?p("",!0):(o(),r(C,{key:0},[i("span",{class:M({active:c.likeActive}),onClick:f[0]||(f[0]=q=>_(e.comment._id))},"赞同("+d(e.comment.likeNum||0)+")",3),i("span",{class:M({active:c.opposeActive}),onClick:f[1]||(f[1]=q=>h(e.comment._id))},"反对("+d(e.comment.opposeNum||0)+")",3)],64)),i("span",{onClick:k},"回复"),F((o(),r("span",{onClick:f[2]||(f[2]=q=>y(e.comment._id))},[w("删除")])),[[g,"blog:messages:delete"]]),F((o(),r("span",{onClick:f[3]||(f[3]=q=>D(e.comment._id))},[w("修改")])),[[g,"blog:messages:update"]])]),author:s(()=>[e.comment.toUser?p("",!0):(o(),r(C,{key:0},[e.comment.userInfo[0].website?(o(),A(n,{key:0},{content:s(()=>[i("p",null,"点击访问 "+d(e.comment.userInfo[0].nickname)+" 的主页",1)]),default:s(()=>[i("a",{href:e.comment.userInfo[0].website,target:"_blank"},[i("span",be,d(e.comment.userInfo[0].nickname),1),e.comment.userInfo[0].username==="admin"?(o(),r("span",Ie)):p("",!0)],8,we)]),_:1})):(o(),r("a",{key:1,href:e.comment.userInfo[0].website,target:"_blank"},[i("span",De,d(e.comment.userInfo[0].nickname),1),e.comment.userInfo[0].username==="admin"?(o(),r("span",Se)):p("",!0)],8,Ce))],64)),e.comment.toUser?(o(),r(C,{key:1},[e.comment.userInfo[0].website?(o(),r(C,{key:0},[l(n,null,{content:s(()=>[i("p",null,"点击访问 "+d(e.comment.userInfo[0].nickname)+" 的主页",1)]),default:s(()=>[i("a",{href:e.comment.userInfo[0].website,target:"_blank"},[i("span",Ue,d(e.comment.userInfo[0].nickname),1),e.comment.userInfo[0].username==="admin"?(o(),r("span",xe)):p("",!0)],8,$e)]),_:1}),w(" @ "),l(n,null,{content:s(()=>[i("p",null,"点击访问 "+d(e.comment.toUserInfo[0].nickname)+" 的主页",1)]),default:s(()=>[i("a",{href:e.comment.toUserInfo[0].website,target:"_blank"},[i("span",qe,d(e.comment.toUserInfo[0].nickname),1),e.comment.toUserInfo[0].username==="admin"?(o(),r("span",Re)):p("",!0)],8,Ae)]),_:1})],64)):(o(),r(C,{key:1},[i("a",{href:e.comment.userInfo[0].website,target:"_blank"},[i("span",Ze,d(e.comment.userInfo[0].nickname),1)],8,Te),e.comment.userInfo[0].username==="admin"?(o(),r("span",Fe)):p("",!0),w(" @ "),i("a",{href:e.comment.toUserInfo[0].website,target:"_blank"},[i("span",Le,d(e.comment.toUserInfo[0].nickname),1),e.comment.toUserInfo[0].username==="admin"?(o(),r("span",Ve)):p("",!0)],8,ze)],64))],64)):p("",!0),i("div",Me,"在 "+d(oe(T).formatRelativeTime(e.comment.createdAt))+" 说:",1)]),avatar:s(()=>[l(m,{previewMask:!1,width:40,src:e.comment.userInfo[0].avatar,alt:"匿名"},null,8,["src"])]),content:s(()=>[i("p",null,d(e.comment.content),1)]),default:s(()=>[e.comment.toUser?(o(),r(C,{key:0},[i("div",Oe,[O(u.$slots,"default")]),c.show.replies?(o(),A(E,{key:0,onSubmitForm:S})):p("",!0)],64)):p("",!0),e.comment.toUser?p("",!0):(o(),r(C,{key:1},[c.show.replies?(o(),A(E,{key:0,onSubmitForm:S})):p("",!0),i("div",Ne,[O(u.$slots,"default")])],64))]),_:3},8,["id"])])):p("",!0)}}};const Ee={key:0,class:"ad-comment-box"},je={class:"box-title"},Be={key:0,class:"pagination"},Pe={__name:"dir-messages-info",setup(e){const t=R({show:{add:!1,edit:!1,view:!1},total:0,editTitle:"编辑",activeComponent:null,updateData:{},resetData:{},viewData:{},query:{params:{},pagination:{current:1,pageSize:20,total:0,hideOnSinglePage:!0},sort:{columnKey:"createdAt",order:"descend"}},dataList:[],loading:{spinning:!1,tip:"加载中"}}),a=(n=1)=>{t.query.pagination.current=n,y(),u(".ad-comment-box")},c=()=>{a()},_=n=>{re({_id:n}).then(m=>{m.status&&(j(`admin-comment-like-${n}`,!0,30),y())})},h=n=>{de({_id:n}).then(m=>{m.status&&(j(`admin-comment-oppose-${n}`,!0,30),y())})},k=([n,m])=>{let v={message:n.pid?n.pid:n._id,toUser:n.userInfo[0]._id,...m};me(v).then(g=>{g.status&&y()})},y=()=>{t.loading.spinning=!0;let n=W(t.query);ae(n).then(m=>{t.loading.spinning=!1;let v=m.data.result;for(const g of v)g.createdAt=T.formatTime(g.createdAt),g.updatedAt=T.formatTime(g.updatedAt),g.repliesInfo.length===0?delete g.children:g.children=g.repliesInfo;t.dataList=v,t.total=m.data.total+m.data.repliesCount,t.query.pagination.total=m.data.total,t.query.pagination.current=m.data.current,t.query.pagination.pageSize=m.data.pageSize}).catch(m=>{t.loading.spinning=!1,console.log(m)})},D=n=>{t.show.edit=!0,n&&n._id?t.editTitle="修改留言":t.editTitle="添加留言",t.updateData=n},S=n=>{G("确认删除该条数据?").then(m=>{m&&ce(n).then(v=>{Z.success("删除成功"),a()})})},u=n=>{document.querySelector(n)&&document.querySelector(n).scrollIntoView({behavior:"smooth"})},f=n=>{t.show.reset=!1,t.show.view=!1,t.show.edit=!1,n&&a()};return a(),(n,m)=>{const v=b("a-input"),g=b("a-form-item"),q=b("a-pagination"),H=b("a-empty");return o(),r("section",null,[l(se,{formValue:t.query.params,onSubmit:a,onReset:c},{default:s(()=>[l(g,{name:"content"},{default:s(()=>[l(v,{value:t.query.params.content,"onUpdate:value":m[0]||(m[0]=I=>t.query.params.content=I),allowClear:"",placeholder:"请输入留言内容",onPressEnter:a,autocomplete:"off"},null,8,["value"])]),_:1})]),_:1},8,["formValue"]),l(X,{onAdd:D,addAuth:"blog:messages:create",showDelete:!1}),t.dataList.length?(o(),r("section",Ee,[i("div",je,"共有 "+d(t.total)+" 条留言",1),(o(!0),r(C,null,N(t.dataList,I=>(o(),A(P,{comment:I,key:I._id,class:"comment-item",onReply:k,onLike:_,onOppose:h,onDelete:S,onEdit:D},{default:s(()=>[I.repliesInfo.length?(o(!0),r(C,{key:0},N(I.repliesInfo,z=>(o(),A(P,{pid:I._id,key:z._id,comment:z,onLike:_,onOppose:h,onReply:k,onDelete:S,onEdit:D},null,8,["pid","comment"]))),128)):p("",!0)]),_:2},1032,["comment"]))),128)),t.query.pagination.total>t.query.pagination.pageSize?(o(),r("div",Be,[l(q,{current:t.query.pagination.current,"onUpdate:current":m[1]||(m[1]=I=>t.query.pagination.current=I),pageSize:t.query.pagination.pageSize,total:t.query.pagination.total,onChange:a,"show-less-items":""},null,8,["current","pageSize","total"])])):p("",!0)])):p("",!0),t.dataList.length?p("",!0):(o(),A(H,{key:1})),l(L,{minWidth:650,show:t.show.edit,title:t.editTitle,key:"GetMessagesInfo",onClose:f},{default:s(()=>[l(fe,{updateData:t.updateData,onClose:f},null,8,["updateData"])]),_:1},8,["show","title"]),l(L,{minWidth:650,show:t.show.view,title:"查看留言",key:"ViewMessagesInfo",onClose:f},{default:s(()=>[l(ge,{viewData:t.viewData,onClose:f},null,8,["viewData"])]),_:1},8,["show"])])}}},Je=Y(Pe,[["__scopeId","data-v-74ae4398"]]);export{Je as default};