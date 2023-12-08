import{G as S,x as Q,r,o as f,a as $,c as e,w as o,F as X,l as ee,e as q,g as D,t as R,k as E,f as ae,y as F,I as L,Z as V,H as T,Y as te,b as se,W as oe}from"./index-5c3da7d5.js";import{i as N,h as le}from"./util.common-c875ddf2.js";import{_ as j,Z as U,a as A,c as Z,T as O,b as ne}from"./util.time-8d93a08e.js";import{_ as re}from"./ZyUpload-d4f69f99.js";import{r as ue}from"./api.roles-04ceb26d.js";import{_ as B}from"./_plugin-vue_export-helper-c27b6911.js";import{u as ie,a as K,b as de,c as ce,d as me}from"./api.users-f1a7068d.js";import{_ as pe}from"./ZyToolButton-29924eec.js";import{Z as fe}from"./ZySearchForm-e8e0544b.js";import"./server-a3264348.js";import"./axios-707ed124.js";const _e={class:"zy-role-select"},ve={__name:"ZyRoleSelect",props:{value:{type:String,default:()=>""}},emits:["update:value"],setup(d,{emit:y}){const a=d,u=S({dataList:[],roleValue:[],query:{params:{},pagination:{current:1,pageSize:100},sort:{columnKey:"createdAt",order:"ascend"}}}),g=c=>{console.log(`selected ${c}`),y("update:value",c)};Q(()=>{a.value&&(u.roleValue=[a.value])});function t(){ue(u.query).then(c=>{u.dataList=c.data.result||[]})}return t(),(c,_)=>{const k=r("a-select-option"),m=r("a-select");return f(),$("section",_e,[e(m,{value:u.roleValue,"onUpdate:value":_[0]||(_[0]=i=>u.roleValue=i),placeholder:"请选择角色",onChange:g},{default:o(()=>[(f(!0),$(X,null,ee(u.dataList,(i,n)=>(f(),q(k,{value:i._id,key:n},{default:o(()=>[D(R(i.roleName),1)]),_:2},1032,["value"]))),128))]),_:1},8,["value"])])}}},we=B(ve,[["__scopeId","data-v-c981ac5c"]]);const ye={class:"zy-get"},ge={class:"upload-box"},he={__name:"get-users-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(d,{emit:y}){const a=d,u={style:{width:"100px"}},g={span:14},t=S({form:{avatar:"https://gravatar.kuibu.net/avatar/5c04c6164bbf04f3e6bcbd01dfd00e03?s=100"}}),c=E(),_=E(!a.updateData);_.value||(t.form=a.updateData||{});const k=async()=>{try{const i=await c.value.validateFields();_.value||delete t.form.password,(_.value?ie:K)(L(t.form)).then(C=>{V.success("操作成功"),y("close",!0)})}catch(i){console.log("Failed:",i)}},m=()=>{T("还没保存数据，确认退出?").then(i=>{i&&y("close")})};return(i,n)=>{const C=r("a-textarea"),z=r("a-image"),p=r("a-form-item"),v=r("a-input"),l=r("a-form");return f(),$("section",ye,[e(l,{model:t.form,class:"zy-form","label-col":u,ref_key:"formRef",ref:c,"wrapper-col":g},{default:o(()=>[e(p,{label:"头像",name:"avatar",rules:[{required:!0,message:"请上传头像!"}]},{default:o(()=>[ae("div",ge,[e(C,{value:t.form.avatar,"onUpdate:value":n[0]||(n[0]=s=>t.form.avatar=s),allowClear:"",placeholder:"在线地址"},null,8,["value"]),t.form.avatar?(f(),q(z,{key:0,style:{margin:"1rem 0"},width:"80px",src:t.form.avatar},null,8,["src"])):F("",!0),e(re,{url:t.form.avatar,"onUpdate:url":n[1]||(n[1]=s=>t.form.avatar=s)},null,8,["url"])])]),_:1}),e(p,{label:"昵称",name:"nickname",rules:[{required:!0,message:"请输入昵称!"}]},{default:o(()=>[e(v,{value:t.form.nickname,"onUpdate:value":n[2]||(n[2]=s=>t.form.nickname=s),allowClear:"",placeholder:"请输入昵称"},null,8,["value"])]),_:1}),e(p,{label:"用户名",name:"username",rules:[{required:!0,message:"请输入用户名!"}]},{default:o(()=>[e(v,{value:t.form.username,"onUpdate:value":n[3]||(n[3]=s=>t.form.username=s),allowClear:"",placeholder:"请输入用户名"},null,8,["value"])]),_:1}),t.form._id?F("",!0):(f(),q(p,{key:0,label:"密码",name:"password",rules:[{required:!0,message:"请输入密码!"}]},{default:o(()=>[e(v,{value:t.form.password,"onUpdate:value":n[4]||(n[4]=s=>t.form.password=s),allowClear:"",placeholder:"请输入密码"},null,8,["value"])]),_:1})),e(p,{label:"邮箱",name:"email"},{default:o(()=>[e(v,{value:t.form.email,"onUpdate:value":n[5]||(n[5]=s=>t.form.email=s),allowClear:"",placeholder:"请输入邮箱"},null,8,["value"])]),_:1}),e(p,{label:"备注",name:"remark"},{default:o(()=>[e(C,{value:t.form.remark,"onUpdate:value":n[6]||(n[6]=s=>t.form.remark=s),allowClear:"",placeholder:"请输入备注"},null,8,["value"])]),_:1}),e(p,{label:"角色",name:"roleId",rules:[{required:!0,message:"请选择角色!"}]},{default:o(()=>[e(we,{value:t.form.roleId,"onUpdate:value":n[7]||(n[7]=s=>t.form.roleId=s)},null,8,["value"])]),_:1})]),_:1},8,["model"]),e(j,{onSave:k,onClose:m})])}}},be=B(he,[["__scopeId","data-v-a812fdfb"]]),ke={class:"zy-view"},Ce={__name:"view-users-info",props:{viewData:{type:Object,default:()=>{}}},emits:["close"],setup(d,{emit:y}){return console.log(d.viewData),(u,g)=>{const t=r("a-image"),c=r("a-tag"),_=r("a-textarea");return f(),$("section",ke,[e(A,null,{default:o(()=>[e(U,{label:"头像"},{default:o(()=>[e(t,{width:40,src:d.viewData.avatar},null,8,["src"])]),_:1}),e(U,{label:"昵称"},{default:o(()=>[D(R(d.viewData.nickname),1)]),_:1})]),_:1}),e(A,null,{default:o(()=>[e(U,{label:"用户名"},{default:o(()=>[D(R(d.viewData.username),1)]),_:1}),e(U,{label:"密码"},{default:o(()=>[D(R(d.viewData.password),1)]),_:1})]),_:1}),e(A,null,{default:o(()=>[e(U,{label:"角色"},{default:o(()=>[D(R(d.viewData.roleName),1)]),_:1}),e(U,{label:"状态"},{default:o(()=>[e(c,{color:"#f70"},{default:o(()=>[D(R(d.viewData.status===1?"正常":"禁用"),1)]),_:1})]),_:1})]),_:1}),e(A,null,{default:o(()=>[e(U,{label:"备注"},{default:o(()=>[e(_,{value:d.viewData.remark,"onUpdate:value":g[0]||(g[0]=k=>d.viewData.remark=k),style:{width:"500px"},disabled:"",placeholder:"Autosize height based on content lines","auto-size":""},null,8,["value"])]),_:1})]),_:1})])}}},De={class:"zy-get"},xe={__name:"reset-users-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(d,{emit:y}){const a=d,u={style:{width:"100px"}},g={span:14},t=S({form:{}}),c=E();t.form=a.updateData||{};const _=async()=>{try{const m=await c.value.validateFields();de(L(t.form)).then(i=>{V.success("密码重置成功"),y("close",!0)}).catch(i=>{V.error(i||"操作失败")})}catch(m){console.log("Failed:",m)}},k=()=>{T("还没保存数据，确认退出?").then(m=>{m&&y("close")})};return(m,i)=>{const n=r("a-input"),C=r("a-form-item"),z=r("a-form");return f(),$("section",De,[e(z,{model:t.form,class:"zy-form","label-col":u,ref_key:"formRef",ref:c,"wrapper-col":g},{default:o(()=>[e(C,{label:"密码",name:"password",rules:[{required:!0,message:"请输入密码!"}]},{default:o(()=>[e(n,{value:t.form.password,"onUpdate:value":i[0]||(i[0]=p=>t.form.password=p),type:"password",disabled:"",allowClear:"",placeholder:"请输入密码"},null,8,["value"])]),_:1}),e(C,{label:"新密码",name:"newPassword",rules:[{required:!0,message:"请输入新密码!"}]},{default:o(()=>[e(n,{value:t.form.newPassword,"onUpdate:value":i[1]||(i[1]=p=>t.form.newPassword=p),allowClear:"",placeholder:"请输入新密码"},null,8,["value"])]),_:1})]),_:1},8,["model"]),e(j,{onSave:_,onClose:k})])}}},Fe={__name:"dir-users-info",setup(d){const y=[{title:"头像",dataIndex:"avatar",key:"avatar",align:"center"},{title:"昵称",dataIndex:"nickname",key:"nickname",align:"center"},{title:"用户名",dataIndex:"username",key:"username",align:"center"},{title:"类型",dataIndex:"type",key:"type",align:"center"},{title:"备注",dataIndex:"remark",key:"remark",align:""},{title:"账号状态",dataIndex:"status",key:"status",align:"center"},{title:"创建时间",dataIndex:"createdAt",key:"createdAt",sorter:(l,s)=>{},align:"center"},{title:"操作",width:225,key:"action",align:"center",fixed:"right"}],a=S({show:{add:!1,edit:!1,view:!1},editTitle:"编辑用户",activeComponent:null,expandedRowKeys:[],updateData:{},resetData:{},viewData:{},query:{params:{},pagination:{current:1,pageSize:10,total:0,hideOnSinglePage:!0},sort:{columnKey:"type",order:"ascend"}},dataList:[],loading:{spinning:!1,tip:"加载中"}}),u=(l=1)=>{a.query.pagination.current=l,m()},g=()=>{u()},t=(l,s)=>{},c=l=>{K({_id:l._id,status:l.status}).then(s=>{V.success(l.status?"启用成功":"停用成功"),u()})},_=({current:l,pageSize:s})=>{a.query.pagination=S({current:l,pageSize:s}),m()},k=({columnKey:l,order:s})=>{a.query.sort=S({current:l,order:s}),m()},m=()=>{a.loading.spinning=!0;let l=L(a.query);ce(l).then(s=>{a.loading.spinning=!1;let h=s.data.result;for(const x of h)x.createdAt=O.formatTime(x.createdAt),x.updatedAt=O.formatTime(x.updatedAt);a.dataList=h,a.query.pagination.total=s.data.total,a.query.pagination.current=s.data.current,a.query.pagination.pageSize=s.data.pageSize}).catch(s=>{a.loading.spinning=!1,console.log(s)})},i=(l,s,h)=>{N(l)||_(l),N(h)||k(h)},n=l=>{a.show.view=!0,a.viewData=l},C=l=>{a.show.edit=!0,l&&l._id?a.editTitle="修改用户":a.editTitle="添加用户",a.updateData=l},z=l=>{T("确认删除该条数据?").then(s=>{s&&me(l).then(h=>{V.success("删除成功"),u()}).catch(h=>{V.error("操作失败"),console.log(h)})})},p=l=>{a.resetData=l||{},a.show.reset=!0},v=l=>{a.show.add=!1,a.show.reset=!1,a.show.view=!1,a.show.edit=!1,l&&u()};return u(),(l,s)=>{const h=r("a-input"),x=r("a-form-item"),P=r("a-select-option"),W=r("a-select"),G=r("a-image"),Y=r("a-switch"),H=r("a-button"),M=r("a-table"),J=te("permission");return f(),$("section",null,[e(fe,{formValue:a.query.params,onSubmit:u,onReset:g},{default:o(()=>[e(x,{name:"name"},{default:o(()=>[e(h,{value:a.query.params.username,"onUpdate:value":s[0]||(s[0]=b=>a.query.params.username=b),allowClear:"",placeholder:"请输入用户名",onPressEnter:u,autocomplete:"off"},null,8,["value"])]),_:1}),e(x,{name:"type"},{default:o(()=>[e(W,{allowClear:"",placeholder:"选择用户类型",class:"input-one",value:a.query.params.type,"onUpdate:value":s[1]||(s[1]=b=>a.query.params.type=b),onChange:u},{default:o(()=>[e(P,{value:"admin"},{default:o(()=>[D("admin")]),_:1}),e(P,{value:"user"},{default:o(()=>[D("user")]),_:1})]),_:1},8,["value"])]),_:1})]),_:1},8,["formValue"]),e(ne,{onAdd:C,addAuth:"sys:user:create",showDelete:!1}),e(M,{bordered:"",resizable:!0,loading:a.loading,columns:y,"row-key":b=>b._id,pagination:a.query.pagination,expandedRowRender:a.expandedRowKeys,onExpand:t,onChange:i,"row-class-name":(b,w)=>w%2===1?"table-striped":null,"data-source":a.dataList},{bodyCell:o(({column:b,record:w})=>[b.key==="avatar"?(f(),q(G,{key:0,width:40,src:w.avatar},null,8,["src"])):b.key==="status"?(f(),q(Y,{key:1,checked:w.status,"onUpdate:checked":I=>w.status=I,disabled:!se(le)("sys:users:update"),"checked-children":"正常","un-checked-children":"停用",onChange:I=>c(w)},null,8,["checked","onUpdate:checked","disabled","onChange"])):b.key==="action"?(f(),q(pe,{key:2,viewAuth:"sys:user:list",editAuth:"sys:user:update",deleteAuth:"sys:user:delete",showView:!1,onView:I=>n(w),showEdit:w.status,onEdit:I=>C(w),onDelete:I=>z(w)},{default:o(()=>[oe((f(),q(H,{type:"primary",size:"small",onClick:I=>p(w)},{default:o(()=>[D("重置密码 ")]),_:2},1032,["onClick"])),[[J,"sys:users:reset"]])]),_:2},1032,["onView","showEdit","onEdit","onDelete"])):F("",!0)]),_:1},8,["loading","row-key","pagination","expandedRowRender","row-class-name","data-source"]),e(Z,{minWidth:650,show:a.show.edit,title:a.editTitle,key:"GetUserInfo",onClose:v},{default:o(()=>[e(be,{updateData:a.updateData,onClose:v},null,8,["updateData"])]),_:1},8,["show","title"]),e(Z,{minWidth:650,show:a.show.view,title:"查看用户",key:"ViewUserInfo",onClose:v},{default:o(()=>[e(Ce,{viewData:a.viewData,onClose:v},null,8,["viewData"])]),_:1},8,["show"]),e(Z,{minWidth:650,show:a.show.reset,title:"重置密码",key:"ResetUserInfo",onClose:v},{default:o(()=>[e(xe,{updateData:a.resetData,onClose:v},null,8,["updateData"])]),_:1},8,["show"])])}}};export{Fe as default};
