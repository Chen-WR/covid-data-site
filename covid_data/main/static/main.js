const globalBox = document.getElementById('global-box')
const countryBox = document.getElementById('country-box')
const stateBox = document.getElementById('state-box')
const areaBox = document.getElementById('area-box')
const globalInput = document.getElementById('global')
const countryInput = document.getElementById('country')
const stateInput = document.getElementById('state')

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