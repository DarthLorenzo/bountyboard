class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.string :name
      t.string :link
      t.string :language
      t.string :contact

      t.timestamps
    end
  end
end
