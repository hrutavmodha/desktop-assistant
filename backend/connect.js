const mongoose = require("mongoose")
module.exports.connect = (dbname) => {
  mongoose.connect(`${process.env.MONGO_URI}/${dbname}`, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    }).then(() => {
      console.log("MongoDB connected successfully")
    }).catch((err) => {
      console.error(err.message)
      process.exit(1)
    })
}
