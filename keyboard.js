const ks = require('node-key-sender')

function testKeyboard(){
    const keyboardKeys = "abcdefghijklmnopqrstuvwxyz1234567890.,/;]";

    console.log('Checking Keyboard Keys')

    try {
        ks.sendText(keyboardKeys)
        console.log('All keyboards are working')
    } catch(error) {
        console.log(`Error Testing Keyboard`, error.message)
        console.log('Not all keyboards are working, faulty product')
    }

}

testKeyboard();