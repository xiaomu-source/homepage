import{Z as M}from"./ZySearchForm-006a0f8b.js";import{_ as P,Z as $,a as T,c as z,T as E,b as J}from"./util.time-11dc32db.js";import{_ as Q}from"./ZyToolButton-ca5b4bfc.js";import{G as K,k as I,L,r as l,o as y,a as x,c as e,w as a,g as C,t as S,e as N,F as G,Z,H as F,Y as X,I as ee,b as te,y as ae,l as oe,W as se}from"./index-08bbd940.js";import{i as V,h as ne}from"./util.common-dbfcb77e.js";import{p as le}from"./api.permissions-72aaaac7.js";import{_ as re}from"./_plugin-vue_export-helper-c27b6911.js";import{a as O,b as ie,r as ue,c as ce}from"./api.roles-9c69269f.js";import"./server-41ad1b27.js";import"./axios-707ed124.js";const de={class:"zy-tree"},me={key:0},pe={__name:"ZyPermTree",props:{value:{type:Array,default:()=>[]}},emits:["update:value"],setup(A,{emit:v}){const t=A,i=K({treeData:[],keysArray:[]}),h=I(),s=I(),u=I(),D={children:"children",title:"name",key:"key"};function g(m){m.forEach(p=>{i.keysArray.push(p.key),p.children&&g(p.children)})}L(u,m=>{v("update:value",m)});function c(){le().then(m=>{i.treeData=m.data.result,t.value.includes("*")?(g(i.treeData),h.value=i.keysArray,s.value=i.keysArray,u.value=i.keysArray):(h.value=t.value,s.value=t.value,u.value=t.value)})}function n(m){h.value=m}function w(m){s.value=m}function _(m){u.value=m}return c(),(m,p)=>{const o=l("IconFont"),r=l("a-tag"),d=l("a-tree");return y(),x("section",de,[e(d,{expandedKeys:h.value,selectedKeys:s.value,checkedKeys:u.value,checkable:"","tree-data":i.treeData,"field-names":D,"onUpdate:expandedKeys":n,"onUpdate:selectedKeys":w,"onUpdate:checkedKeys":_},{title:a(({auth:b,name:U,key:R})=>[b?(y(),x("span",me,[C(S(U)+" ",1),(y(),N(r,{color:"orange",style:{"margin-left":"5px"},key:R},{icon:a(()=>[e(o,{type:"icon-quanxianguanli"})]),default:a(()=>[C(" "+S(R),1)]),_:2},1024))])):(y(),x(G,{key:1},[C(S(U),1)],64))]),_:1},8,["expandedKeys","selectedKeys","checkedKeys","tree-data"])])}}},_e=re(pe,[["__scopeId","data-v-3c8b2c26"]]),fe={class:"zy-get"},ye={__name:"get-roles-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(A,{emit:v}){const t=A,i={style:{width:"100px"}},h={span:14},s=K({form:{}}),u=I();s.form=t.updateData||{};const D=async()=>{try{const c=await u.value.validateFields();c._id=s.form._id,O(c).then(n=>{n&&(Z.success("修改角色成功！"),v("close",!0))})}catch(c){console.log("Failed:",c)}},g=()=>{F("还没保存数据，确认退出?").then(c=>{c&&v("close",!0)})};return(c,n)=>{const w=l("a-input"),_=l("a-form-item"),m=l("a-textarea"),p=l("a-radio"),o=l("a-radio-group"),r=l("a-form");return y(),x("section",fe,[e(r,{model:s.form,ref_key:"formRef",ref:u,class:"zy-form","label-col":i,"wrapper-col":h},{default:a(()=>[e(_,{label:"角色名称",name:"roleName",rules:[{required:!0,message:"请输入角色名称!"}]},{default:a(()=>[e(w,{value:s.form.roleName,"onUpdate:value":n[0]||(n[0]=d=>s.form.roleName=d),allowClear:"",placeholder:"请输入角色名称"},null,8,["value"])]),_:1}),e(_,{label:"角色标识",name:"roleAuth",rules:[{required:!0,message:"请输入角色标识!"}]},{default:a(()=>[e(w,{value:s.form.roleAuth,"onUpdate:value":n[1]||(n[1]=d=>s.form.roleAuth=d),disabled:"",allowClear:"",placeholder:"请输入角色标识"},null,8,["value"])]),_:1}),e(_,{label:"角色备注",name:"remark"},{default:a(()=>[e(m,{value:s.form.remark,"onUpdate:value":n[2]||(n[2]=d=>s.form.remark=d),allowClear:"",placeholder:"请输入角色备注"},null,8,["value"])]),_:1}),e(_,{label:"状态",name:"status",rules:[{required:!0,message:"请选状态!"}]},{default:a(()=>[e(o,{value:s.form.status,"onUpdate:value":n[3]||(n[3]=d=>s.form.status=d)},{default:a(()=>[e(p,{value:!0},{default:a(()=>[C("正常")]),_:1}),e(p,{value:!1},{default:a(()=>[C("禁用")]),_:1})]),_:1},8,["value"])]),_:1}),e(_,{label:"菜单权限",name:"perms",rules:[{required:!0,message:"请选权限!"}]},{default:a(()=>[e(_e,{value:s.form.perms,"onUpdate:value":n[4]||(n[4]=d=>s.form.perms=d)},null,8,["value"])]),_:1})]),_:1},8,["model"]),e(P,{onSave:D,onClose:g})])}}},he={class:"zy-get"},ve={__name:"add-roles-info",props:{},emits:["close"],setup(A,{emit:v}){const t=I(["sys:users"]);L(t,c=>{console.log("Parent component - perms:",c)});const i={style:{width:"100px"}},h={span:14},s=I(),u=K({form:{}}),D=async()=>{try{const c=await s.value.validateFields();ie(c).then(n=>{Z.success("添加角色成功！"),v("close",!0)})}catch(c){console.log("Failed:",c)}},g=()=>{F("还没保存数据，确认退出?").then(c=>{c&&v("close")})};return(c,n)=>{const w=l("a-input"),_=l("a-form-item"),m=l("a-textarea"),p=l("a-form");return y(),x("section",he,[e(p,{model:u.form,style:{"background-color":"#fff"},ref_key:"formRef",ref:s,"label-col":i,"wrapper-col":h},{default:a(()=>[e(_,{label:"角色名称",name:"roleName",rules:[{required:!0,message:"请输入角色名称!"}]},{default:a(()=>[e(w,{value:u.form.roleName,"onUpdate:value":n[0]||(n[0]=o=>u.form.roleName=o),allowClear:"",placeholder:"请输入角色名称"},null,8,["value"])]),_:1}),e(_,{label:"角色标识",name:"roleAuth",rules:[{required:!0,message:"请输入角色标识!"}]},{default:a(()=>[e(w,{value:u.form.roleAuth,"onUpdate:value":n[1]||(n[1]=o=>u.form.roleAuth=o),allowClear:"",placeholder:"请输入角色标识"},null,8,["value"])]),_:1}),e(_,{label:"角色备注",name:"remark"},{default:a(()=>[e(m,{value:u.form.remark,"onUpdate:value":n[2]||(n[2]=o=>u.form.remark=o),allowClear:"",placeholder:"请输入角色备注"},null,8,["value"])]),_:1})]),_:1},8,["model"]),e(P,{onSave:D,onClose:g})])}}},ge={class:"zy-view"},we={__name:"view-roles-info",props:{viewData:{type:Object,default:()=>{}}},emits:["close"],setup(A,{emit:v}){return console.log(A.viewData),(i,h)=>{const s=l("a-tag"),u=l("a-textarea");return y(),x("section",ge,[e(T,null,{default:a(()=>[e($,{label:"角色名称"},{default:a(()=>[e(s,{color:"#f50"},{default:a(()=>[C("超级管理员")]),_:1})]),_:1}),e($,{label:"角色标识"},{default:a(()=>[C(" super admin ")]),_:1})]),_:1}),e(T,null,{default:a(()=>[e($,{label:"备注"},{default:a(()=>[e(u,{style:{width:"500px"},disabled:"",placeholder:"Autosize height based on content lines","auto-size":""})]),_:1})]),_:1})])}}},Re={__name:"dir-roles-info",setup(A){const v=[{title:"角色名称",dataIndex:"roleName",key:"roleName",align:"center"},{title:"角色标识",dataIndex:"roleAuth",key:"roleAuth",align:""},{title:"备注",dataIndex:"remark",key:"remark",align:""},{title:"状态",dataIndex:"status",key:"status",align:"center"},{title:"创建时间",dataIndex:"createdAt",key:"createdAt",align:"center"},{title:"操作",width:225,key:"action",align:"center",fixed:"right"}],t=K({show:{add:!1,edit:!1,view:!1},activeComponent:null,updateData:{},viewData:{},dataList:[],query:{params:{},pagination:{current:1,pageSize:10,total:0,hideOnSinglePage:!0},sort:{columnKey:"createdAt",order:"ascend"}},loading:{spinning:!1,tip:"加载中"}}),i=(o=1)=>{t.query.pagination.current=o,g()},h=()=>{i()},s=({current:o,pageSize:r})=>{t.query.pagination=K({current:o,pageSize:r}),g()},u=({columnKey:o,order:r})=>{t.query.sort=K({current,order:r}),g()},D=o=>{O({_id:o._id,status:o.status}).then(r=>{Z.success(o.status?"启用成功":"停用成功"),i()})},g=()=>{t.loading.spinning=!0;let o=ee(t.query);ue(o).then(r=>{t.loading.spinning=!1;let d=r.data.result;for(const b of d)b.createdAt=E.formatTime(b.createdAt),b.updatedAt=E.formatTime(b.updatedAt);t.dataList=d,t.query.pagination.total=r.data.total,t.query.pagination.current=r.data.current,t.query.pagination.pageSize=r.data.pageSize}).catch(r=>{t.loading.spinning=!1,console.log(r)})},c=(o,r,d)=>{V(o)||s(o),V(d)||u(d)},n=o=>{t.show.view=!0,t.viewData=o},w=()=>{t.show.add=!0},_=o=>{t.show.edit=!0,t.updateData=o},m=o=>{F("确认删除该条数据?").then(r=>{r&&ce(o).then(d=>{Z.success("删除成功"),i()})})},p=o=>{t.show.add=!1,t.show.view=!1,t.show.edit=!1,o&&i()};return i(),(o,r)=>{const d=l("a-input"),b=l("a-form-item"),U=l("a-switch"),R=l("IconFont"),W=l("a-tag"),j=l("a-descriptions-item"),B=l("a-descriptions"),Y=l("a-table"),H=X("copy");return y(),x("section",null,[e(M,{formValue:t.query.params,onSubmit:i,onReset:h},{default:a(()=>[e(b,{name:"name"},{default:a(()=>[e(d,{value:t.query.params.name,"onUpdate:value":r[0]||(r[0]=k=>t.query.params.name=k),allowClear:"",placeholder:"请输入名称",onPressEnter:i,autocomplete:"off"},null,8,["value"])]),_:1})]),_:1},8,["formValue"]),e(J,{onAdd:w,addAuth:"sys:roles:create",showDelete:!1}),e(Y,{bordered:"",resizable:!0,loading:t.loading,columns:v,"row-key":k=>k._id,pagination:t.query.pagination,onChange:c,"row-class-name":(k,f)=>f%2===1?"table-striped":null,"data-source":t.dataList},{bodyCell:a(({column:k,record:f})=>[k.key==="status"?(y(),N(U,{key:0,checked:f.status,"onUpdate:checked":q=>f.status=q,disabled:!te(ne)("sys:role:update"),"checked-children":"正常","un-checked-children":"停用",onChange:q=>D(f)},null,8,["checked","onUpdate:checked","disabled","onChange"])):k.key==="action"?(y(),N(Q,{key:1,showView:!1,viewAuth:"sys:roles:list",editAuth:"sys:roles:update",deleteAuth:"sys:roles:delete",editText:"编辑 / 权限",showEdit:f.status,onView:q=>n(f),onEdit:q=>_(f),onDelete:q=>m(f)},null,8,["showEdit","onView","onEdit","onDelete"])):ae("",!0)]),expandedRowRender:a(({record:k})=>[e(B,{title:"权限信息",bordered:"",layout:"vertical"},{default:a(()=>[e(j,{label:"角色权限",span:3},{default:a(()=>[(y(!0),x(G,null,oe(k.perms,(f,q)=>se((y(),N(W,{color:"#55acee",style:{margin:"5px",cursor:"pointer"},key:q},{icon:a(()=>[e(R,{type:"icon-quanxianguanli"})]),default:a(()=>[C(" "+S(f),1)]),_:2},1024)),[[H,f]])),128))]),_:2},1024)]),_:2},1024)]),_:1},8,["loading","row-key","pagination","row-class-name","data-source"]),e(z,{minWidth:650,show:t.show.add,title:"新增角色",key:"GetRolesInfo",onClose:p},{default:a(()=>[e(ve,{onClose:p})]),_:1},8,["show"]),e(z,{minWidth:650,show:t.show.edit,title:"编辑角色",key:"GetRolesInfo",onClose:p},{default:a(()=>[e(ye,{updateData:t.updateData,onClose:p},null,8,["updateData"])]),_:1},8,["show"]),e(z,{minWidth:650,show:t.show.view,title:"查看角色",key:"GetRolesInfo",onClose:p},{default:a(()=>[e(we,{viewData:t.viewData,onClose:p},null,8,["viewData"])]),_:1},8,["show"])])}}};export{Re as default};
