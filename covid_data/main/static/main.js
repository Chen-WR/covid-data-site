const globalBox = document.getElementById('global-box')
const countryBox = document.getElementById('country-box')
const stateBox = document.getElementById('state-box')
const areaBox = document.getElementById('area-box')

const globalInput = document.getElementById('global')
const countryInput = document.getElementById('country')
const stateInput = document.getElementById('state')

const globalText = document.getElementById('global-text')
const countryText = document.getElementById('country-text')
const stateText = document.getElementById('state-text')
const areaText = document.getElementById('area-text')

const globalID = document.getElementById('Global')
const countryID = document.getElementById('Country')
const stateID = document.getElementById('State')
const areaID = document.getElementById('Area')

const buttonBox = document.getElementById('button-box')

const locationForm = document.getElementById('location-form')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

$.ajax({
	type:'Get',
	url: '/world_json/',
	success: function(response){
		const globalData = response.data
		globalData.map(item=>{
			const option = document.createElement('div')
			// displaying the name of the place
			option.textContent = item.name
			option.setAttribute('class', 'item')
			option.setAttribute('id', 'globalID')
			// keeping data value as name id to filter country option
			option.setAttribute('data-value', item.name_id)
			globalBox.appendChild(option)
		})
	},
	error: function(error){
		console.log(error)
	},
})

globalInput.addEventListener('change', e=>{
	// selectWorld will be giving back parent id of the select global to filter out country
	const selectWorld = e.target.value
		countryBox.innerHTML = ""
		countryID.value = 0
		stateID.value = 0
		areaID.value = 0
		countryText.textContent = "Choose Country"
		countryText.classList.add("default")
		stateBox.innerHTML = ""
		stateText.textContent = "Choose State"
		stateText.classList.add("default")
		areaBox.innerHTML = ""
		areaText.textContent = "Choose Area"
		areaText.classList.add("default")
	$.ajax({
		type: 'Get',
		url: `/country_json/${selectWorld}/`,
		success: function(response){
			const countryData = response.data
			countryData.map(item=>{
			const option = document.createElement('div')
			// displaying the name of the place
			option.textContent = item.name
			option.setAttribute('class', 'item')
			// keeping data value as name id to filter country option
			option.setAttribute('data-value', item.name_id)
			countryBox.appendChild(option)
		})
		},
		error: function(error){
			console.log(error)
		},
	})
})

countryInput.addEventListener('change', e=>{
	const selectCountry = e.target.value
	stateID.value = 0
	areaID.value = 0
	stateBox.innerHTML = ""
	stateText.textContent = "Choose State"
	stateText.classList.add("default")
	areaBox.innerHTML = ""
	areaText.textContent = "Choose Area"
	areaText.classList.add("default")
	$.ajax({
		type: 'Get',
		url: `/state_json/${selectCountry}/`,
		success: function(response){
			const stateData = response.data
			stateData.map(item=>{
			const option = document.createElement('div')
			// displaying the name of the place
			option.textContent = item.name
			option.setAttribute('class', 'item')
			// keeping data value as name id to filter country option
			option.setAttribute('data-value', item.name_id)
			stateBox.appendChild(option)
		})
		},
		error: function(error){
			console.log(error)
		},
	})
})

stateInput.addEventListener('change', e=>{
	const selectState = e.target.value
	areaID.value = 0
	areaBox.innerHTML = ""
	areaText.textContent = "Choose Area"
	areaText.classList.add("default")
	$.ajax({
		type: 'Get',
		url: `/area_json/${selectState}/`,
		success: function(response){
			const areaData = response.data
			areaData.map(item=>{
			const option = document.createElement('div')
			// displaying the name of the place
			option.textContent = item.name
			option.setAttribute('class', 'item')
			// keeping data value as name id to filter country option
			option.setAttribute('data-value', item.name_id)
			areaBox.appendChild(option)
		})
		},
		error: function(error){
			console.log(error)
		},
	})
})

locationForm.addEventListener('submit', e=>{
	e.preventDefault()
	$.ajax({
		type:'POST',
		url:'/graph/',
		data:{
			'csrfmiddlewaretoken': csrf[0].value,
			'globalID':globalID.value,
			'countryID':countryID.value,
			'stateID':stateID.value,
			'areaID':areaID.value,
		},
		success: function(response){
			if (response['data']=='None'){
			}
			else if (response['data'] != 'None'){
				makeGraph('total-case-chart', 'Total Case', response.data.date, response.data.totalcase)
				makeGraph('new-case-chart', 'New Case', response.data.date, response.data.newcase)
				makeGraph('total-death-chart', 'Total Death', response.data.date, response.data.totaldeath)
				makeGraph('new-death-chart', 'New Death', response.data.date, response.data.newdeath)
			}
		},
		error: function(error){
			console.log(error)
		},
	})
})

function makeGraph(element, graphname, labelArray, dataArray){
	var myChart = new Chart(
		document.getElementById(element),
		{
			type: 'line',
			data: {
				labels: labelArray,
				datasets: [{
					label: graphname,
					backgroundColor: 'rgb(255, 99, 132)',
					borderColor: 'rgb(255, 99, 132)',
					data: dataArray,
				}]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
			}
		}
	);
	console.log()
}