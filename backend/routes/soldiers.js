const router = require("express").Router();
let Soldier = require("../models/soldier");

router.route("/").get((req, res) => {
  Soldier.find()
    .then((soldiers) => res.json(soldiers))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/soldier/:name").get((req, res) => {
  const name = req.params.name;
  Soldier.findOne({ name: name })
    .then((soldier) => res.json(soldier))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/add").post(async (req, res) => {
  const name = req.body.name;
  const water = [{ value: 70, time: Date.now() }];
  const bodyDifferential = [
    { value: req.body.bodyDifferential, time: Date.now() },
  ];
  const heartRate = [{ value: 100, time: Date.now() }];
  const moisture = [{ value: 50, time: Date.now() }];
  const bmi = [{ value: req.body.bmi, time: Date.now() }];
  const riskScore = [{ value: 0, time: Date.now() }];

  const newSoldier = new Soldier({
    name,
    water,
    bodyDifferential,
    heartRate,
    moisture,
    bmi,
    riskScore,
  });
  return newSoldier
    .save()
    .then(() => res.json("Soldier added!"))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/delete").post(async (req, res) => {
  const name = req.body.name;
  return Soldier.deleteOne({ name: name })
    .then(() => res.json("Soldier deleted!"))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/water").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { water: newSample } })
    .then(() => res.json(`Updated soldier ${name} water`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/bodyDifferential").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { bodyDifferential: newSample } })
    .then(() => res.json(`Updated soldier ${name} body differential`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/heartRate").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { heartRate: newSample } })
    .then(() => res.json(`Updated soldier ${name} heart rate`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/moisture").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { moisture: newSample } })
    .then(() => res.json(`Updated soldier ${name} moisture`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/bloodPressure").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { bloodPressure: newSample } })
    .then(() => res.json(`Updated soldier ${name} bloodPressure`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/bmi").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { bmi: newSample } })
    .then(() => res.json(`Updated soldier ${name} bmi`))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/riskScore").post(async (req, res) => {
  const name = req.body.name;
  const value = req.body.value;

  const newSample = { value: value, time: Date.now() };

  Soldier.updateOne({ name: name }, { $push: { riskScore: newSample } })
    .then(() => res.json(`Updated soldier ${name} risk score`))
    .catch((err) => res.status(400).json("Error: " + err));
});

/*
const calculateRiskScore = async (name) => {
  const soldier = (await Soldier.find({name: name}))[0]
  
  const newestBodyDifferential = soldier.bodyDifferential.slice(-1)[0].value;
  const newestHeartRate = soldier.heartRate.slice(-1)[0].value;
  const newestMoisture = soldier.moisture.slice(-1)[0].value;
  const newestBmi = soldier.bmi.slice(-1)[0].value;
  const newestWater = soldier.water.slice(-1)[0].value;
  let score =
    0.4 * newestBodyDifferential +
    0.25 * newestHeartRate +
    0.25 * newestMoisture +
    0.1 * newestBmi;
  if (newestWater > 90) {
    score = score * 0.5;
  } else if (newestWater > 80) {
    score = score * 0.8;
  } else if (newestWater > 70) {
    score = score * 0.9;
  } else if (newestWater > 60) {
    score = score * 1;
  } else {
    score = score * 1.6;
  }
  const newScoreSample = {value: score, time: Date.now()}
  console.log("Wow")
  console.log(newScoreSample)
  return newScoreSample
  
};
*/
module.exports = router;
