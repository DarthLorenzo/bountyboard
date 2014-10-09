json.array!(@tickets) do |ticket|
  json.extract! ticket, :id, :title, :description, :addDate, :bounty
  json.owner ticket.user, :id, :name, :email
  json.url ticket_url(ticket, format: :json)
end
