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

globalID.value = 0
countryID.value = 0
stateID.value = 0
areaID.value = 0

$.ajax({
	type:'Get',
	url: '/world_json/',
	success: function(response){
		// console.log(response)
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
	// console.log(e.target.value)
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
			// 'world':globalText.textContent,
			// 'country':countryText.textContent,
			// 'state':stateText.textContent,
			// 'area':areaText.textContent,
			'globalID':globalID.value,
			'countryID':countryID.value,
			'stateID':stateID.value,
			'areaID':areaID.value,
		},
		success: function(response){
			// console.log(response)
		},
		error: function(error){
			console.log(error)
		},
	})
})