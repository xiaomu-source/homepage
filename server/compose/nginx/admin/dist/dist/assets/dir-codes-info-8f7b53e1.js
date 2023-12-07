import{_ as P,Z as y,a as v,c as E,T as N,b as W}from"./util.time-117201b0.js";import{G as T,k as G,r as i,o as f,a as V,c as t,w as l,F as H,l as M,e as D,g as m,t as _,I as B,Z,H as L,y as Y}from"./index-dca43598.js";import{a as A}from"./server-b9531d4c.js";import{_ as J}from"./ZyToolButton-379302e5.js";import{Z as Q}from"./ZySearchForm-eb2c604b.js";import{i as U}from"./util.common-1af15359.js";import"./_plugin-vue_export-helper-c27b6911.js";import"./axios-707ed124.js";const X=n=>A.post("/v1/dev/codes/get-list/",n),ee=n=>A.post("/v1/dev/codes/delete-code/",n),te=n=>A.post("/v1/dev/codes/delete-all/",n),ae=n=>A.get("/v1/dev/codes/collections/",n),oe=n=>A.post("/v1/dev/codes/singleCurdFrontAndBack/",n),le={class:"zy-get"},ne={__name:"get-codes-info",props:{updateData:{type:Object,default:()=>{}}},emits:["close"],setup(n,{emit:b}){const e={style:{width:"100px"}},c={span:14},s=T({form:{},collections:[]}),x=G();(()=>{ae().then(u=>{s.collections=u.data||[]})})();const z=async()=>{try{const u=await x.value.validateFields();oe(B(s.form)).then(r=>{Z.success("操作成功"),b("close",!0)}).catch(r=>{Z.error(r||"操作失败")})}catch(u){console.log("Failed:",u)}},k=()=>{L("还没保存数据，确认退出?").then(u=>{u&&b("close")})};return(u,r)=>{const F=i("a-select-option"),q=i("a-select"),C=i("a-form-item"),R=i("a-input"),g=i("a-alert"),o=i("a-form");return f(),V("section",le,[t(o,{model:s.form,class:"zy-form","label-col":e,ref_key:"formRef",ref:x,"wrapper-col":c},{default:l(()=>[t(C,{label:"模型",name:"tableName",rules:[{required:!0,message:"请选择模型!"}]},{default:l(()=>[t(q,{value:s.form.tableName,"onUpdate:value":r[0]||(r[0]=a=>s.form.tableName=a),placeholder:"请选择模型"},{default:l(()=>[(f(!0),V(H,null,M(s.collections,(a,d)=>(f(),D(F,{value:a,key:d},{default:l(()=>[m(_(a),1)]),_:2},1032,["value"]))),128))]),_:1},8,["value"])]),_:1}),t(C,{label:"模型备注",name:"comment",rules:[{required:!0,message:"请输入模型备注（中文）!"}]},{default:l(()=>[t(R,{value:s.form.comment,"onUpdate:value":r[1]||(r[1]=a=>s.form.comment=a),allowClear:"",placeholder:"请输入模型备注"},null,8,["value"]),t(g,{message:"模型备注：主要作为文件内的中文说明",type:"info"})]),_:1}),t(C,{label:"根权限",name:"auth",rules:[{required:!0,message:"请输入根权限!"}]},{default:l(()=>[t(R,{value:s.form.auth,"onUpdate:value":r[2]||(r[2]=a=>s.form.auth=a),allowClear:"",placeholder:"请输入根权限"},null,8,["value"]),t(g,{message:"根权限：例如页面需要建在系统管理下面则填'sys'",type:"info"})]),_:1})]),_:1},8,["model"]),t(P,{onSave:z,onClose:k})])}}},se={class:"zy-view"},ie={__name:"view-codes-info",props:{viewData:{type:Object,default:()=>{}}},emits:["close"],setup(n,{emit:b}){return(e,c)=>(f(),V("section",se,[t(v,null,{default:l(()=>[t(y,{label:"文件名称"},{default:l(()=>[m(_(n.viewData.name),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"文件类型"},{default:l(()=>[m(_(n.viewData.type),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"下载地址"},{default:l(()=>[m(_(n.viewData.url),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"备注"},{default:l(()=>[m(_(n.viewData.remark),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"_id"},{default:l(()=>[m(_(n.viewData._id),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"createdAt"},{default:l(()=>[m(_(n.viewData.createdAt),1)]),_:1})]),_:1}),t(v,null,{default:l(()=>[t(y,{label:"updatedAt"},{default:l(()=>[m(_(n.viewData.updatedAt),1)]),_:1})]),_:1})]))}},ge={__name:"dir-codes-info",setup(n){const b=[{title:"文件名称",dataIndex:"name",key:"name",align:"center"},{title:"文件类型",dataIndex:"type",key:"type",align:"center"},{title:"下载地址",dataIndex:"url",key:"url",align:"center"},{title:"备注",dataIndex:"remark",key:"remark",align:"center"},{title:"创建时间",dataIndex:"createdAt",key:"createdAt",align:"center"},{title:"操作",key:"action",align:"center",fixed:"right"}],e=T({show:{add:!1,edit:!1,view:!1},collections:[],editTitle:"编辑",activeComponent:null,selectedRowKeys:[],updateData:{},resetData:{},viewData:{},query:{params:{},pagination:{current:1,pageSize:10,total:0,hideOnSinglePage:!0},sort:{columnKey:"createdAt",order:"descend"}},dataList:[],loading:{spinning:!1,tip:"加载中"}}),c=(o=1)=>{e.query.pagination.current=o,k()},s=()=>{c()},x=o=>{let a=document.createElement("a");a.href=o,a.click(),window.URL.revokeObjectURL(o)},$=({current:o,pageSize:a})=>{e.query.pagination=T({current:o,pageSize:a}),k()},z=({columnKey:o,order:a})=>{e.query.sort=T({current:o,order:a}),k()},k=()=>{e.loading.spinning=!0;let o=B(e.query);X(o).then(a=>{var S;e.loading.spinning=!1;let d=((S=a.data)==null?void 0:S.result)||[];for(const h of d)h.createdAt=N.formatTime(h.createdAt),h.updatedAt=N.formatTime(h.updatedAt);e.dataList=d,e.query.pagination.total=a.data.total,e.query.pagination.current=a.data.current,e.query.pagination.pageSize=a.data.pageSize}).catch(a=>{e.loading.spinning=!1,console.log(a)})},u=o=>{e.selectedRowKeys=o},r=(o,a,d)=>{U(o)||$(o),U(d)||z(d)},F=o=>{e.show.view=!0,e.viewData=o},q=o=>{e.show.edit=!0,e.editTitle="创建代码生成",e.updateData.back=o},C=()=>{L("确认删除数据?").then(o=>{o&&te({ids:e.selectedRowKeys||[]}).then(a=>{Z.success("删除成功"),c()})})},R=o=>{L("确认删除该条数据?").then(a=>{a&&ee(o).then(d=>{Z.success("删除成功"),c()})})},g=o=>{e.show.reset=!1,e.show.view=!1,e.show.edit=!1,o&&c()};return c(),(o,a)=>{const d=i("a-alert"),S=i("a-input"),h=i("a-form-item"),K=i("a-image"),O=i("a-button"),j=i("a-table");return f(),V("section",null,[t(d,{message:"💥代码生成功能：主要是开发人员使用。可能需要结合代码进行理解功能",type:"info",style:{"margin-bottom":"10px"},closable:""}),t(Q,{formValue:e.query.params,onSubmit:c,onReset:s},{default:l(()=>[t(h,{name:"name"},{default:l(()=>[t(S,{value:e.query.params.name,"onUpdate:value":a[0]||(a[0]=p=>e.query.params.name=p),allowClear:"",placeholder:"请输入文件名称",onPressEnter:c,autocomplete:"off"},null,8,["value"])]),_:1})]),_:1},8,["formValue"]),t(W,{onAdd:q,addText:"创建",onDelete:C,deleteText:"批量删除",addAuth:"dev:codes:singleCurdFrontAndBack",deleteAuth:"dev:codes:deleteAll"}),t(j,{"row-selection":{selectedRowKeys:e.selectedRowKeys,onChange:u},bordered:"",resizable:!0,loading:e.loading,columns:b,"row-key":p=>p._id,pagination:e.query.pagination,onChange:r,"row-class-name":(p,w)=>w%2===1?"table-striped":null,"data-source":e.dataList},{bodyCell:l(({column:p,record:w})=>[p.key==="avatar"?(f(),D(K,{key:0,width:40,src:w.avatar},null,8,["src"])):p.key==="url"?(f(),D(O,{key:1,type:"primary",size:"small",onClick:I=>x(w.url)},{default:l(()=>[m("下载链接")]),_:2},1032,["onClick"])):p.key==="action"?(f(),D(J,{key:2,viewAuth:"dev:codes:list",deleteAuth:"dev:codes:delete",showEdit:!1,showView:!1,onView:I=>F(w),onEdit:I=>q(w),onDelete:I=>R(w)},null,8,["onView","onEdit","onDelete"])):Y("",!0)]),_:1},8,["row-selection","loading","row-key","pagination","row-class-name","data-source"]),(f(),D(E,{minWidth:650,show:e.show.edit,title:e.editTitle,key:e.editTitle,onClose:g},{default:l(()=>[t(ne,{updateData:e.updateData,onClose:g},null,8,["updateData"])]),_:1},8,["show","title"])),t(E,{minWidth:650,show:e.show.view,title:"查看代码生成",key:"ViewCodesInfo",onClose:g},{default:l(()=>[t(ie,{viewData:e.viewData,onClose:g},null,8,["viewData"])]),_:1},8,["show"])])}}};export{ge as default};
