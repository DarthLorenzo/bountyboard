# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
User.create([{name: 'Perry Shuman', email: "perry.shuman@bazaarvoice.com", budget: 2500}, {name: 'Jesse Vera', email: "Jesse.Vera@bazaarvoice.com", budget: 3000}, {name: 'Clayton Stout', email: "clayton.stout@bazaarvoice.com", budget: 0}])
Ticket.create(title: 'Building the bounty board!', description: 'We would like to have a bounty board where we can post up new ideas for 20% projects and give rewards for their completion.', addDate: '2014-10-09T00:59:00.000Z', bounty: 300, user_id: 2)
