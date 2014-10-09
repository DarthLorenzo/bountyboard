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
	name: "Firebird",
	link: "https://github.com/bazaarvoice/firebird",
	language: "Javascript",
	contact: "Rebecca Murphy",
	imageURL: "http://media-cache-ec0.pinimg.com/736x/98/fd/00/98fd002ce5778e7f0b87b6d2255985e7.jpg")



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
