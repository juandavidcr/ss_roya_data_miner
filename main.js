const regex = /^\s{11}PRECIP\s{2}EVAP\s{3}TMAX\s{3}TMIN/;
const text = "           PRECIP  EVAP   TMAX   TMIN";
if(regex.test(text)){
    console.log("Es correcto")
}else{
    console.log("Es incorrecto")
}

