var firebaseURL = 'https://multisensor9.firebaseio.com/'
var userInfo = {}
var thisUser



const admin = require('firebase-admin');
const tootls = require('firebase-tools');
const functions = require('firebase-functions');
const database = admin.database()



// Initialize Firebase
var config = {
    apiKey: "AIzaSyD40MAcvt9Vx4Sud-AcoGY-POq-rQ-lZP0",
    authDomain: "multisensor9.firebaseapp.com",
    databaseURL: "https://multisensor9.firebaseio.com",
    projectId: "multisensor9",
    storageBucket: "multisensor9.appspot.com",
    messagingSenderId: "829800944158"
};
firebase.initializeApp(config);





function signIn(email, pword){
    firebase.auth().signInWithEmailAndPassword(email, pword).catch(function(error){
        var errorCode = error.code;
        var errorMsg = error.message;

        firebase.auth().currentUser.sendEmailVerification()
        username = user.email
        username = username.substr(0, (username.search('@')))
    }).then
    {
        firebase.auth().onAuthStateChanged(function (user) {
            user = firebase.auth().currentUser
            if (user) {
                thisUser = user.uid
                console.log(user.uid)
                firebase.auth().currentUser.sendEmailVerification()
                username = user.email
                username = username.substr(0, (username.search('@')))
                userInfo = {

                    displayName: user.displayName,
                    email: user.email,
                    emailVerified: user.emailVerified,
                    photoURL: user.photoURL,
                    isAnonymous: user.isAnonymous,
                    uID: user.uid,
                    providerData: user.providerData,
                }
            } else {
                window.location.assign = '404.html'
                alert('There was an error!!!')

            }
            var initialised = false
            firebasePush(thisUser, initialised)
            window.location.assign = 'signedIn.html'
        })
    }

}







function firebasePush(UID, booleanCheck) {
    booleanCheck = true
    db = firebase.database()
    ref = db.ref('/Readings/' + UID)
    ref.update({
        placeholder: booleanCheck

    })

    return;
}







function getNodeValues (nodeName) {

}







function makeCreds(email, pword){
    firebase.auth().createUserWithEmailAndPassword(email, pword)
    signIn(email, pword);
}






function checkCreds(email, pword, pwordConf) {
    if (email.includes('@') == true) {
        if (pword.length >= 6) {
            if (pword == pwordConf) {
                makeCreds(email, pword)
            }
            else {
                alert('Your passwords do not match, please try again.')
                window.location = 'index.html';
            }
        } else {
            alert('Sorry, your password has to be at least 6 chars.')
            window.location = 'index.html';
        }
    } else {
        alert('Please enter a valid email address')
    }
}
