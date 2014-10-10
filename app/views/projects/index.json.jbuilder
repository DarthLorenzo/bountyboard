json.array!(@projects) do |project|
  json.extract! project, :id, :name, :link, :language, :contact, :imageURL, :description
  json.url project_url(project, format: :json)
end
