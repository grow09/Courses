var min = 0;

document.getElementById("min").innerHTML = min;


var carName = 'Ford'
var carYear = 2005

var personYear = 2012

/*if(calculateAge(carYear) < 10) {
   console.log('less 10 years')
} else {
   console.log('more 10 years')
}

if(calculateAge(personYear) < 10) {
   console.log('less 10 years')
} else {
   console.log('more 10 years')
}*/


function calculateAge(year) {
   var currentYear = 2020
   var result = currentYear - year
   return result
}

function checkAndLogAge(year) {
   if (calculateAge(year) < 10) {
       console.log('less 10 years')
   } else {
       console.log('more 10 years')
   }
}

checkAndLogAge(carYear)
checkAndLogAge(personYear)
