import{s as a,j as t}from"./index-7e2ab289.js";const e=a(),n=s=>t.post("/jwt/create/",s),r=async s=>await t.post("/users/",s,{headers:{"Content-Type":"application/json"}}),i=async()=>{t.defaults.headers.common.Authorization="JWT "+e.pat;const s=await t.get("/me/");e.setUserData(s.data)};export{r as C,n as G,i as g};
