json.array!(@donations) do |donation|
  json.extract! donation, :id, :user_id, :ticket_id, :amount
  json.url donation_url(donation, format: :json)
end
