import{_ as K,Z as k,a as b,c as z,b as M,T as L}from"./util.time-8d93a08e.js";import{G as O,k as P,r as m,o as c,a as T,c as e,w as s,g as u,I as Y,Z as E,H as F,t as h,Y as J,e as C,b as Q,y as D,F as N,W as j}from"./index-5c3da7d5.js";import{a as X,b as ee,c as te,d as ae,e as B}from"./api.permissions-4bfc4e48.js";import{_ as se}from"./ZyToolButton-29924eec.js";import{Z as ne}from"./ZySearchForm-e8e0544b.js";import{i as W,h as oe}from"./util.common-c875ddf2.js";import"./_plugin-vue_export-helper-c27b6911.js";import"./server-a3264348.js";import"./axios-707ed124.js";const le={class:"zy-get"},ie={__name:"get-permissions-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(p,{emit:x}){const a=p,d={style:{width:"100px"}},V={span:14},l=O({form:{auth:!1,autoSon:!1}}),q=P(),S=P(!a.updateData);S.value||(l.form=a.updateData||{});const I=async()=>{try{const v=await q.value.validateFields();S.value||delete l.form.password,(S.value?X:ee)(Y(l.form)).then(y=>{E.success("操作成功"),x("close",!0)})}catch(v){console.log("Failed:",v)}},U=()=>{F("还没保存数据，确认退出?").then(v=>{v&&x("close")})};return(v,i)=>{const y=m("a-input"),_=m("a-form-item"),g=m("a-radio"),w=m("a-radio-group"),t=m("a-alert"),n=m("a-form");return c(),T("section",le,[e(n,{model:l.form,class:"zy-form","label-col":d,ref_key:"formRef",ref:q,"wrapper-col":V},{default:s(()=>[e(_,{label:"权限名称",name:"name",rules:[{required:!0,message:"请输入权限名称!"}]},{default:s(()=>[e(y,{value:l.form.name,"onUpdate:value":i[0]||(i[0]=o=>l.form.name=o),allowClear:"",placeholder:"权限名称：增加"},null,8,["value"])]),_:1}),e(_,{label:"权限标识",name:"key",rules:[{required:!0,message:"请输入权限标识!"}]},{default:s(()=>[e(y,{value:l.form.key,"onUpdate:value":i[1]||(i[1]=o=>l.form.key=o),allowClear:"",placeholder:"权限标识：sys:user / sys:user:create"},null,8,["value"])]),_:1}),e(_,{label:"父级标识",name:"parent_key"},{default:s(()=>[e(y,{value:l.form.parent_key,"onUpdate:value":i[2]||(i[2]=o=>l.form.parent_key=o),allowClear:"",placeholder:"父级标识：sys"},null,8,["value"])]),_:1}),e(_,{label:"排序",name:"sortOrder"},{default:s(()=>[e(y,{value:l.form.sortOrder,"onUpdate:value":i[3]||(i[3]=o=>l.form.sortOrder=o),allowClear:"",placeholder:"排序:值越大越往后"},null,8,["value"])]),_:1}),e(_,{label:"权限按钮",name:"auth"},{default:s(()=>[e(w,{value:l.form.auth,"onUpdate:value":i[4]||(i[4]=o=>l.form.auth=o),name:"auth"},{default:s(()=>[e(g,{value:!0},{default:s(()=>[u("是")]),_:1}),e(g,{value:!1},{default:s(()=>[u("否")]),_:1})]),_:1},8,["value"])]),_:1}),e(_,{label:"生成子级",name:"autoSon"},{default:s(()=>[e(w,{value:l.form.autoSon,"onUpdate:value":i[5]||(i[5]=o=>l.form.autoSon=o),name:"auth"},{default:s(()=>[e(g,{value:!0},{default:s(()=>[u("是")]),_:1}),e(g,{value:!1},{default:s(()=>[u("否")]),_:1})]),_:1},8,["value"]),e(t,{message:"生成子级:自动生成增删改查权限按钮"})]),_:1})]),_:1},8,["model"]),e(K,{onSave:I,onClose:U})])}}},re={class:"zy-view"},ue={__name:"view-permissions-info",props:{viewData:{type:Object,default:()=>{}}},emits:["close"],setup(p,{emit:x}){return(a,d)=>(c(),T("section",re,[e(b,null,{default:s(()=>[e(k,{label:"权限名称"},{default:s(()=>[u(h(p.viewData.name),1)]),_:1})]),_:1}),e(b,null,{default:s(()=>[e(k,{label:"权限键"},{default:s(()=>[u(h(p.viewData.key),1)]),_:1})]),_:1}),e(b,null,{default:s(()=>[e(k,{label:"父级"},{default:s(()=>[u(h(p.viewData.parent_key),1)]),_:1})]),_:1}),e(b,null,{default:s(()=>[e(k,{label:"按钮"},{default:s(()=>[u(h(p.viewData.auth),1)]),_:1})]),_:1}),e(b,null,{default:s(()=>[e(k,{label:"排序"},{default:s(()=>[u(h(p.viewData.sortOrder),1)]),_:1})]),_:1}),e(b,null,{default:s(()=>[e(k,{label:"状态"},{default:s(()=>[u(h(p.viewData.status),1)]),_:1})]),_:1})]))}},we={__name:"dir-permissions-info",setup(p){const x=[{title:"权限名称",width:275,dataIndex:"name",key:"name"},{title:"权限标识",width:275,dataIndex:"key",key:"key"},{title:"父级标识",dataIndex:"parent_key",key:"parent_key"},{title:"权限按钮",dataIndex:"auth",key:"auth",align:"center"},{title:"排序",dataIndex:"sortOrder",key:"sortOrder",align:"center"},{title:"状态",width:100,dataIndex:"status",key:"status",align:"center"},{title:"创建时间",dataIndex:"createdAt",key:"createdAt",align:"center"},{title:"操作",width:225,key:"action",align:"center",fixed:"right"}],a=O({show:{add:!1,edit:!1,view:!1},editTitle:"编辑",activeComponent:null,updateData:{},resetData:{},viewData:{},query:{params:{},pagination:{current:1,pageSize:10,total:0,hideOnSinglePage:!0},sort:{columnKey:"sortOrder",order:"ascend"}},dataList:[],loading:{spinning:!1,tip:"加载中"}}),d=(t=1)=>{a.query.pagination.current=t,U()},V=()=>{d()},l=({current:t,pageSize:n})=>{a.query.pagination=O({current:t,pageSize:n}),U()},q=({columnKey:t,order:n})=>{a.query.sort=O({current:t,order:n}),U()},S=t=>{ae({_id:t._id}).then(n=>{E.success(t.status?"启用成功":"停用成功"),d()})};function I(t){t.createdAt=L.formatTime(t.createdAt),t.updatedAt=L.formatTime(t.updatedAt),t.children&&t.children.forEach(n=>{I(n)})}const U=()=>{a.loading.spinning=!0;let t=Y(a.query);te(t).then(n=>{a.loading.spinning=!1;let o=n.data.result;o.forEach(Z=>{I(Z)}),a.dataList=o}).catch(n=>{a.loading.spinning=!1,console.log(n)})},v=(t,n,o)=>{W(t)||l(t),W(o)||q(o)},i=t=>{a.show.view=!0,a.viewData=t},y=t=>{a.show.edit=!0,t&&t._id?a.editTitle="修改权限":a.editTitle="添加权限",a.updateData=t};function _(t,n=1){return(t.match(/:/g)||[]).length===n}const g=t=>{_(t.key,0)||_(t.key,1)?F("确认删除该条数据以及所有子级数据?").then(n=>{n&&B(t).then(o=>{E.success("删除成功"),d()})}):F("确认删除该条数据?").then(n=>{n&&B(t).then(o=>{E.success("删除成功"),d()})})},w=t=>{a.show.reset=!1,a.show.view=!1,a.show.edit=!1,t&&d()};return d(),(t,n)=>{const o=m("a-input"),Z=m("a-form-item"),G=m("a-switch"),$=m("a-tag"),H=m("a-table"),R=J("copy");return c(),T("section",null,[e(ne,{formValue:a.query.params,onSubmit:d,onReset:V},{default:s(()=>[e(Z,{name:"name"},{default:s(()=>[e(o,{value:a.query.params.name,"onUpdate:value":n[0]||(n[0]=f=>a.query.params.name=f),allowClear:"",placeholder:"请输入权限名称",onPressEnter:d,autocomplete:"off"},null,8,["value"])]),_:1})]),_:1},8,["formValue"]),e(M,{onAdd:y,addAuth:"syspermissions:create",showDelete:!1}),e(H,{bordered:"",resizable:!0,loading:a.loading,columns:x,"row-key":f=>f._id,pagination:a.query.pagination,onChange:v,"row-class-name":(f,r)=>r%2===1?"table-striped":null,"data-source":a.dataList},{bodyCell:s(({column:f,record:r})=>[f.key==="status"?(c(),C(G,{key:0,checked:r.status,"onUpdate:checked":A=>r.status=A,disabled:!Q(oe)("sys:permissions:stop"),"checked-children":"正常","un-checked-children":"停用",onChange:A=>S(r)},null,8,["checked","onUpdate:checked","disabled","onChange"])):D("",!0),f.key==="auth"?(c(),T(N,{key:1},[r.auth?(c(),C($,{key:0,color:"#87d068"},{default:s(()=>[u("是")]),_:1})):D("",!0)],64)):D("",!0),f.key==="key"?j((c(),C($,{key:2,color:"green"},{default:s(()=>[u(h(r.key),1)]),_:2},1024)),[[R,r.key]]):D("",!0),f.key==="parent_key"?(c(),T(N,{key:3},[r.parent_key?j((c(),C($,{key:0,color:"green"},{default:s(()=>[u(h(r.parent_key),1)]),_:2},1024)),[[R,r.key]]):D("",!0)],64)):f.key==="action"?(c(),C(se,{key:4,viewAuth:"sys:permissions:list",editAuth:"sys:permissions:update",deleteAuth:"sys:permissions:delete",onView:A=>i(r),showEdit:r.status,onEdit:A=>y(r),onDelete:A=>g(r)},null,8,["onView","showEdit","onEdit","onDelete"])):D("",!0)]),_:1},8,["loading","row-key","pagination","row-class-name","data-source"]),(c(),C(z,{minWidth:650,show:a.show.edit,title:a.editTitle,key:a.editTitle,onClose:w},{default:s(()=>[e(ie,{updateData:a.updateData,onClose:w},null,8,["updateData"])]),_:1},8,["show","title"])),e(z,{minWidth:650,show:a.show.view,title:"查看权限",key:"ViewPermissionsInfo",onClose:w},{default:s(()=>[e(ue,{viewData:a.viewData,onClose:w},null,8,["viewData"])]),_:1},8,["show"])])}}};export{we as default};
