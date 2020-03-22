function print(){
    checkAndLogAge(document.getElementById("human").value)
    checkAndLogAge(document.getElementById("car").value)
    human = document.getElementById("human").value
    car = document.getElementById("car").value
}

function calculateAge(year) {
   var currentYear = 2020
   var result = currentYear - year
   return result
}

function checkAndLogAge(year) {
    if (year !== ''){
        if (calculateAge(year) < 0) {
            console.log('WTF?')
        } else if (calculateAge(year) < 10) {
                if (year == human){
                    console.log('You younger than 10 years')
                } else if (year == car) {
                    console.log('Car younger than 10 years')
                } 
        } else if (calculateAge(year) >= 10) {
                if (year == human){
                    console.log('You older than 10 years')
                } else if (year == car) {
                    console.log('Car older than 10 years')
                }
        } else {
            console.log("Incorrect data!")
        }
    } 
}
