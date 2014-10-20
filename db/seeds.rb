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
	name: "Bounty Board",
	link: "https://github.com/bazaarvoice/rosetta",
	language: "Javascript",
	contact: "Claire Cahill",
	imageURL: "resources/Bountyboard.png",
	description: "Attaching promises of bounty in exchange for work")
Project.create(
	name: "Flynn",
	link: "https://github.com/bazaarvoice/flynn",
	language: "Scala",
	contact: "Jona Fenocchi",
	imageURL: "resources/Flynn.png",
	description: "For exploring Polloi-based ElasticSearch clusters")
Project.create(
	name: "Rudy",
	link: "https://github.com/bazaarvoice/rudy",
	language: "Java",
	contact: "Juicy J",
	imageURL: "resources/Rudy.png",
	description: "For debugging Syndication 2.0: Switchboard, Oracle, Theo, and Agrippa")
Project.create(
	name: "Gumshoe",
	link: "https://github.com/bazaarvoice/gumshoe",
	language: "Java",
	contact: "Sherlock Holmes",
	imageURL: "resources/Gumshoe.png",
	description: "Investigating Bazaarvoice's data asset")
Project.create(
	name: "Badger",
	link: "https://github.com/bazaarvoice/badger",
	language: "Java",
	contact: "Honey Badger",
	imageURL: "resources/Badger.png",
	description: "Monitoring Bazaarvoice services")
Project.create(
	name: "Rosetta",
	link: "https://github.com/bazaarvoice/rosetta",
	language: "Java",
	contact: "Rosetta Stone",
	imageURL: "resources/Rosetta.png",
	description: "For understanding client configuration")
Project.create(
	name: "Banyan",
	link: "https://github.com/bazaarvoice/banyan",
	language: "Java",
	contact: "Rosetta Stone",
	imageURL: "resources/banyan.png",
	description: "Data store for internal client configurations")
Project.create(
	name: "Miscellaneous",
	link: "none",
	language: "unknown",
	contact: "Claire Cahill",
	imageURL: "resources/Miscellaneous.png",
	description: "Description")


Ticket.create(
	title: 'Building the bounty board!',
	description: 'We would like to have a bounty board where we can post up new ideas for 20% projects and give rewards for their completion.',
	user_id: 2,
	project_id: 1)


Donation.create(
	user_id: 2,
	ticket_id: 1,
	amount: 100)
