// // Example starter JavaScript for disabling form submissions if there are invalid fields
// (function () {
//     'use strict'
  
//     // Fetch all the forms we want to apply custom Bootstrap validation styles to
//     var forms = document.querySelectorAll('.needs-validation')
  
//     // Loop over them and prevent submission
//     Array.prototype.slice.call(forms)
//       .forEach(function (form) {
//         form.addEventListener('submit', function (event) {
//           if (!form.checkValidity()) {
//             event.preventDefault()
//             event.stopPropagation()
//           }
  
//           form.classList.add('was-validated')
//         }, false)
//       })
//   })()


  var slider3 = document.getElementById("customRange3");
  var output3 = document.getElementById("customRange3Value");
  output3.innerHTML = slider3.value;
  
  slider3.oninput = function() {
    console.log(this.value)
    output3.innerHTML = this.value;
  }


  var slider4 = document.getElementById("customRange4");
  var output4 = document.getElementById("customRange4Value");
  output4.innerHTML = slider4.value;
  
  slider4.oninput = function() {
    console.log(this.value)
    output4.innerHTML = this.value;
  }


  var slider5 = document.getElementById("customRange5");
  var output5 = document.getElementById("customRange5Value");
  output5.innerHTML = slider5.value;
  
  slider5.oninput = function() {
    console.log(this.value)
    output5.innerHTML = this.value;
  }

  document.getElementById('submit-prediction').addEventListener('click', function () {
    var formEl = document.forms.churn_form;
    var formData = new FormData(formEl);
    console.log(formData)
    // var name = formData.get('name');
  })



 


