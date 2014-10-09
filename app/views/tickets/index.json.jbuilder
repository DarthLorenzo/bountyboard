json.array!(@tickets) do |ticket|
  json.extract! ticket, :id, :title, :description, :created_at
  json.bounty Donation.where(:ticket_id => ticket.id).sum :amount
  json.owner ticket.user, :id, :name, :email
  json.url ticket_url(ticket, format: :json)
end
