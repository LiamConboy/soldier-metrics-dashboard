const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const soldierSchema = new Schema({
  name: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    minlength: 3,
  },
  water: { type: Array, required: true },
  bodyDifferential: { type: Array, required: true },
  heartRate: { type: Array, required: true },
  moisture: { type: Array, required: true },
  bmi: { type: Array, required: true },
  riskScore: { type: Array, required: true },
});

const Soldier = mongoose.model("Soldier", soldierSchema);

module.exports = Soldier;