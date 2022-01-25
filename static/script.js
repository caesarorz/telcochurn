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
    output3.innerHTML = this.value;
  }

  var slider4 = document.getElementById("customRange4");
  var output4 = document.getElementById("customRange4Value");
  output4.innerHTML = slider4.value;
  
  slider4.oninput = function() {
    output4.innerHTML = this.value;
  }

  var slider5 = document.getElementById("customRange5");
  var output5 = document.getElementById("customRange5Value");
  output5.innerHTML = slider5.value;
  
  slider5.oninput = function() {
    output5.innerHTML = this.value;
  }

document.querySelector('.btn-close').addEventListener('click', (e) => {
  document.getElementById('alert-result').classList.toggle('hide-element')
})


const formatValuesTable = (value) => {
  if (value === 'SeniorCitizen') {
    return "Yes"
  }
  start = value.indexOf("_");
  new_value = value.slice(start+1, value.length);
  return new_value
}

const rendertablePrediction = (data) => {
  table_body = document.querySelector(".fill-data")
  data = JSON.parse(data)
  for (const [key, value] of Object.entries(data)) {
      var tr = document.createElement('tr');   
      var td1 = document.createElement('td');
      var td2 = document.createElement('td');
      var text1 = document.createTextNode(`${key}`);
      var text2 = document.createTextNode(`${formatValuesTable(value)}`);
      td1.appendChild(text1);
      td2.appendChild(text2);
      tr.appendChild(td1);
      tr.appendChild(td2);
      table_body.appendChild(tr);
  }
}

const renderResult = (data) => {
  if (data.prediction === 'No' || data.prediction === 'Yes'){
    document.getElementById("prediction-result").innerHTML = `Model Result: <bold>${data.prediction}</bold>`
    document.getElementById('alert-result').classList.toggle("hide-element")
    // document.getElementById('alert-result').classList.toggle("show-element")
  }
  else {
    document.getElementById("prediction-result").innerHTML = `Error in prediction, we are working to fix the issue.`
  }
}


const Form = document.getElementById("churn_form");

Form.addEventListener("submit", handleFormSubmit);
 async function handleFormSubmit(event) {
	event.preventDefault();
	const form = event.currentTarget;
	const url = form.action;
	try {
		const formData = new FormData(form);
		const responseData = await postFormDataAsJson({ url, formData });
    renderResult(responseData)
	} catch (error) {
		console.error(error);
	}
}


 async function postFormDataAsJson({ url, formData }) {
	const plainFormData = Object.fromEntries(formData.entries());
	const formDataJsonString = JSON.stringify(plainFormData);

	const fetchOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		body: formDataJsonString,
	};

	const response = await fetch(url, fetchOptions);


	if (!response.ok) {
		const errorMessage = await response.text();
		throw new Error(errorMessage);
	}

  rendertablePrediction(formDataJsonString)
	return response.json();
}



 


