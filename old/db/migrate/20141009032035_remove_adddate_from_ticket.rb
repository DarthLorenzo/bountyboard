class RemoveAdddateFromTicket < ActiveRecord::Migration
  def change
    remove_column :tickets, :addDate, :datetime
  end
end
