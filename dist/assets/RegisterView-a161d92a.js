import{r as a,u as y,o as d,c as u,a as s,d as w,w as l,v as n,b as o,h as x,S as b,i as I}from"./index-61301723.js";import{C as V}from"./auth.origins-b6f4f6c7.js";const U={class:"col col-lg-5"},k={class:"card"},B={class:"card-body"},C=s("h5",{align:"center",class:"card-title"}," Registrar usuario nuevo ",-1),R=s("h5",{align:"center",class:"card-text"}," Ingrese sus datos para comenzar ",-1),E=["onSubmit"],N={class:"form-floating mb-3"},S=s("label",{for:"floatingInput"},[o("Usuario "),s("i",{class:"bi bi-person-badge"})],-1),q={class:"form-floating mb-3"},T=s("label",{for:"floatingInput"},[o("Contraseña "),s("i",{class:"bi bi-key"})],-1),A={class:"form-floating mb-3"},D=s("label",{for:"floatingInput"},[o("Repita su contraseña "),s("i",{class:"bi bi-key-fill"})],-1),L={key:0,class:"alert alert-primary alert-dismissible fade show",role:"alert"},M=s("strong",null,"Error!",-1),z={class:"form-floating mb-3"},G=s("label",{for:"floatingInput"},[o("Correo "),s("i",{class:"bi bi-envelope-at"})],-1),O={class:"form-floating mb-3"},P=s("label",{for:"floatingInput"},[o("Nombres "),s("i",{class:"bi bi-person"})],-1),j={class:"form-floating mb-3"},F=s("label",{for:"floatingInput"},[o("Apellidos "),s("i",{class:"bi bi-person"})],-1),H=s("button",{class:"btn btn-success",type:"submit"},"Guardar",-1),J={key:1},K=s("div",{class:"spinner-border text-success",role:"status"},[s("span",{class:"visually-hidden"},"Loading...")],-1),Y={__name:"RegisterView",setup(Q){const c=a(""),i=a(""),r=a(""),p=a(""),m=a(""),v=a(""),f=a(!1),g=y(),h=async()=>{const _={username:c.value,password:i.value,password2:r.value,email:p.value};f.value=!0,await V(_).then(e=>{b.fire({title:"Usuario creado",text:"El usuario ha sido creado con éxito",icon:"success",confirmButtonText:"Aceptar"}),g.push({name:"login"})}).catch(e=>{const t=I(e.response.data);b.fire({icon:"error",title:"Oops...",text:t,timer:3e3,timerProgressBar:!0,showConfirmButton:!1})}).finally(()=>{f.value=!1})};return(_,e)=>(d(),u("div",U,[s("div",k,[s("div",B,[C,R,f.value?(d(),u("div",J,[o(" Espere ... "),K])):(d(),u("form",{key:0,onSubmit:w(h,["prevent"])},[s("div",N,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[0]||(e[0]=t=>c.value=t),class:"form-control",requierd:"",type:"text"},null,512),[[n,c.value]]),S]),s("div",q,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[1]||(e[1]=t=>i.value=t),class:"form-control",required:"",type:"password"},null,512),[[n,i.value]]),T]),s("div",A,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[2]||(e[2]=t=>r.value=t),class:"form-control",required:"",type:"password"},null,512),[[n,r.value]]),D]),i.value!==r.value?(d(),u("div",L,[M,o(" Las contraseñas no coinciden. ")])):x("",!0),s("div",z,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[3]||(e[3]=t=>p.value=t),class:"form-control",type:"text"},null,512),[[n,p.value]]),G]),s("div",O,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[4]||(e[4]=t=>m.value=t),class:"form-control",type:"text"},null,512),[[n,m.value]]),P]),s("div",j,[l(s("input",{id:"floatingInput","onUpdate:modelValue":e[5]||(e[5]=t=>v.value=t),class:"form-control",type:"text"},null,512),[[n,v.value]]),F]),H],40,E))])])]))}};export{Y as default};
