class AddImageToProduct < ActiveRecord::Migration
  def change
    add_column :projects, :imageURL, :string
  end
end
