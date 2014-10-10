# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141010160013) do

  create_table "donations", force: true do |t|
    t.integer  "user_id"
    t.integer  "ticket_id"
    t.integer  "amount"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  add_index "donations", ["ticket_id"], name: "index_donations_on_ticket_id"
  add_index "donations", ["user_id"], name: "index_donations_on_user_id"

  create_table "projects", force: true do |t|
    t.string   "name"
    t.string   "link"
    t.string   "language"
    t.string   "contact"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "imageURL"
    t.text     "description"
  end

  create_table "tickets", force: true do |t|
    t.string   "title"
    t.text     "description"
    t.integer  "user_id"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.integer  "project_id"
  end

  add_index "tickets", ["user_id"], name: "index_tickets_on_user_id"

  create_table "users", force: true do |t|
    t.string   "name"
    t.string   "email"
    t.integer  "budget"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end
