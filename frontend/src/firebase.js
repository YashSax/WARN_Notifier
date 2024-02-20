// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBuU9hLsLwkxlUgZGywPtv8PT7Zq5y8UGk",
  authDomain: "warn-notices-ff163.firebaseapp.com",
  projectId: "warn-notices-ff163",
  storageBucket: "warn-notices-ff163.appspot.com",
  messagingSenderId: "739340273902",
  appId: "1:739340273902:web:95c50146773054dcd54bff",
  measurementId: "G-FYVFHQRWB0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);