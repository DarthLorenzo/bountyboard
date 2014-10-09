# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
User.create([{name: 'Perry Shuman', email: "perry.shuman@bazaarvoice.com", budget: 2500}, {name: 'Jesse Vera', email: "Jesse.Vera@bazaarvoice.com", budget: 3000}, {name: 'Clayton Stout', email: "clayton.stout@bazaarvoice.com", budget: 0}])
Ticket.create(title: 'Building the bounty board!', description: 'We would like to have a bounty board where we can post up new ideas for 20% projects and give rewards for their completion.', bounty: 300, user_id: 2)
Ticket.create(title: 'Adding the BV theme back into our bounty board project', description: "I'm really bad at javascript, html, and css! Are you a front end developer? Do you know what you're doing? Are you like me and just want a little break from writing elasticsearch queries?? Please help me by fully encorporating the bybootstrap css to make our project look more b:adass! Let me know if you have any questions, and I'd be happy to help!", bounty: 250, user_id: 1)
