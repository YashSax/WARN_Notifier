import './App.css';
import { collection, addDoc } from "firebase/firestore"
import { db } from "./firebase"
import { useState } from "react"

const addUser = async (e, company, email, name, state) => {
  e.preventDefault()
  try {
    await addDoc(collection(db, "users"), {
      "Company" : company,
      "Email" : email,
      "Name" : name,
      "State" : state,
    });
  } catch (e) {
    console.error("Error adding document: ", e);
  }
}

function WARNForm() {
  const [name, setName] = useState("");
  const [company, setCompany] = useState("");
  const [state, setState] = useState("");
  const [email, setEmail] = useState("");

  return (
    <form>
      <label>Name: </label>
      <input name="Name" onChange={(event) => setName(event.target.value)}></input><br/>
      <label>Company: </label>
      <input name="Company" onChange={(event) => setCompany(event.target.value)}></input><br/>
      <label>State: </label>
      <input name="State" onChange={(event) => setState(event.target.value)}></input><br/>
      <label>Email: </label>
      <input name="Email" onChange={(event) => setEmail(event.target.value)}></input><br/>
      <input type="submit" value="Submit" onClick={(e) => addUser(e, company, email, name, state)}></input>
    </form>
  )
}

function App() {
  return (
    <div>
      <WARNForm></WARNForm>
    </div>
  );
}

export default App;
