# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
User.create([
	{
		name: 'Perry Shuman',
		email: "perry.shuman@bazaarvoice.com",
		budget: 2500
	},
	{
		name: 'Jesse Vera',
		email: "Jesse.Vera@bazaarvoice.com",
		budget: 3000
	},
	{
		name: 'Clayton Stout',
		email: "clayton.stout@bazaarvoice.com",
		budget: 0
	}])

Project.create(
	name: "Miscellaneous",
	link: "none",
	language: "unknown",
	contact: "Claire Cahill",
	imageURL: "resources/Miscellaneous.png" )
Project.create(
	name: "Firebird",
	link: "https://github.com/bazaarvoice/firebird",
	language: "Javascript",
	contact: "Rebecca Murphy",
	imageURL: "resources/Firebird.png")
Project.create(
	name: "Flynn",
	link: "https://github.com/bazaarvoice/flynn",
	language: "Scala",
	contact: "Jona Fenocchi",
	imageURL: "resources/Flynn.png" )
Project.create(
	name: "Rudy",
	link: "https://github.com/bazaarvoice/rudy",
	language: "Java",
	contact: "Juicy J",
	imageURL: "resources/Rudy.png" )
Project.create(
	name: "Gumshoe",
	link: "https://github.com/bazaarvoice/gumshoe",
	language: "Java",
	contact: "Sherlock Holmes",
	imageURL: "resources/Gumshoe.png" )
Project.create(
	name: "Badger",
	link: "https://github.com/bazaarvoice/badger",
	language: "Java",
	contact: "Honey Badger",
	imageURL: "resources/Badger.png" )
Project.create(
	name: "Rosetta",
	link: "https://github.com/bazaarvoice/rosetta",
	language: "Java",
	contact: "Rosetta Stone",
	imageURL: "resources/Rosetta.png" )


Ticket.create(
	title: 'Building the bounty board!',
	description: 'We would like to have a bounty board where we can post up new ideas for 20% projects and give rewards for their completion.',
	user_id: 2,
	project_id: 1)
Ticket.create(
	title: 'Adding the BV theme back into our bounty board project',
	description: "I'm really bad at javascript, html, and css! Are you a front end developer? Do you know what you're doing? Are you like me and just want a little break from writing elasticsearch queries?? Please help me by fully encorporating the bybootstrap css to make our project look more b:adass! Let me know if you have any questions, and I'd be happy to help!",
	user_id: 1,
	project_id: 1)


Donation.create(
	user_id: 2,
	ticket_id: 1,
	amount: 300)
Donation.create(
	user_id: 1,
	ticket_id: 2,
	amount: 250)
Donation.create(
	user_id: 1,
	ticket_id: 1,
	amount: 900)
