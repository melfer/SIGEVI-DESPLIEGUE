import{u,r as _,e as p,k as h,l as m,o,c as n,a as t,F as f,m as v,t as e,b as g}from"./index-7e2ab289.js";const y={id:"pdf"},k={class:"card"},x={class:"card-body"},B=t("h5",{class:"card-title"},"Reporte de Existencias",-1),F={class:"card-text"},D=t("h6",null,"A continuación, se listarán los productos con pocas existencias",-1),P={class:"container-fluid"},b=t("strong",null,"referencia:",-1),E=t("hr",{style:{color:"white"}},null,-1),N={__name:"PDFReportContainer",setup(R){const d=u(),r=_("");p(async()=>{const a=await h();r.value=a.data,l()});const l=()=>{const a=document.getElementById("pdf"),c={margin:.5,filename:"reporte_restock.pdf",html2canvas:{scale:2},jsPDF:{unit:"in",format:"letter",orientation:"portrait"}};m().from(a).set(c).save(),d.push({name:"home"})};return(a,c)=>(o(),n("div",y,[t("div",k,[t("div",x,[B,t("p",F,[D,(o(!0),n(f,null,v(r.value,(s,i)=>(o(),n("div",{key:i},[t("div",P,[t("h5",null,e(i+1)+" - "+e(s.nombre),1),t("p",null,"Quedan "+e(s.cantidad)+" "+e(s.unidad),1),t("p",null,[b,g(" "+e(s.referencia[0].marca)+" - "+e(s.referencia[0].categoria),1)])])]))),128)),E])])])]))}};export{N as default};
