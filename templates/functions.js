function getCurrentYear() {
  var NowMoment = moment();
  year = NowMoment.format("YYYY");
  document.getElementById("currentYear").innerHTML = year;
}

function getMyAge() {
  var MyAge = moment().diff('1994-08-20', 'years');
  document.getElementById("myAge").innerHTML = MyAge;
}

window.onload = function() {
  getCurrentYear();
  getMyAge();
}
