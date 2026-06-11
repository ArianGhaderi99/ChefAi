document.querySelector('.mobile-menu')?.addEventListener('click', () => {
    document.querySelector('.nav-menu').style.display = 'block';
});


function getCookie(name){

let cookieValue = null;

if(document.cookie){

const cookies =
document.cookie.split(';');

for(let i=0;i<cookies.length;i++){

const cookie =
cookies[i].trim();

if(cookie.startsWith(name + '=')){

cookieValue =
decodeURIComponent(
cookie.substring(
name.length + 1
)
);

break;
}

}
}

return cookieValue;
}


const generateBtn =
document.getElementById(
"generateBtn"
);


if(generateBtn){

generateBtn.addEventListener(
"click",

async ()=>{

const ingredients =
document.getElementById(
"ingredients"
).value;


document.getElementById(
"loading"
).innerHTML =
"در حال تولید پیشنهادات...";


const response =
await fetch(

"/chef-ai/api/",

{

method:"POST",

headers:{

"Content-Type":
"application/json",

"X-CSRFToken":
getCookie("csrftoken")

},

body:JSON.stringify({

ingredients

})

}

);


const data =
await response.json();


document.getElementById(
"loading"
).innerHTML = "";


document.getElementById(
"result"
).innerHTML =

`
<div class="ai-result">
${data.answer}
</div>
`;

}

);

}