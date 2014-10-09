class RemoveBountyFromTableTickets < ActiveRecord::Migration
  def change
    remove_column :tickets, :bounty, :integer
  end
end
