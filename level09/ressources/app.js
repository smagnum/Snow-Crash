const fs = require('fs')

fs.readFile('token', 'binary' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data)
    i = 0
    res = ''
    while (i < data.length) {
        res += (String.fromCharCode(data.charCodeAt(i) - i))
        i+=1
    }
    console.log(res)
        
})
