import * as React from "react";
import { Routes, Route, NavLink } from "react-router-dom";
import ItemsApp from "./Items";
import CoursesApp from "./Courses";
import { AddressBook, People, Person, PersonAddForm, Groups } from "./AddressBook";
import { useEffect, useState } from "react";

function App() {
  return (
    <div>
      <ul className="Menu">
        <li><NavLink to="/">Home</NavLink></li>
        <li><NavLink to="/clock">Clock</NavLink></li>
        <li><NavLink to="/items">Items</NavLink></li>
        <li><NavLink to="/grocery">Grocery</NavLink></li>
        <li><NavLink to="/fetch">Fetch</NavLink></li>
        <li><NavLink to="/addressBook">Address book</NavLink></li>
        <li><NavLink to="/about">About</NavLink></li>
      </ul>
      <header>
        <h1>Welcome to React Router!</h1>
      </header>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="clock" element={<Clock />} />
        <Route path="items" element={<Items />} />
        <Route path="grocery" element={<Grocery />} />
        <Route path="fetch" element={<Fetch />} />
        <Route path="addressBook" element={<AddressBook />}>
          <Route path="people/*" element={<People />}>
            <Route index element={<p>Sélectionnez une personne</p>} />
          </Route>
          <Route path="groups" element={<Groups />}>
            <Route index element={<p>Sélectionnez un groupe</p>} />
          </Route>
        </Route>
        <Route path="about" element={<About />} />
      </Routes>
    </div>
  );
}

function Home() {
  return (
    <>
      <main>
        <h2>Welcome to the homepage!</h2>
        <p>You can do this, I believe in you.</p>
      </main>
    </>
  );
}

function Clock() {
  const [value, setValue] = useState(new Date());
  useEffect(() => {
    const interval = setInterval(() => setValue(new Date()), 1000/60);
    return () => { clearInterval(interval);};
  }, []);
  return (
    <>
      <main>
        <h2>Clock</h2>
        <p>You have the time men. Coool.</p>
  <p>Time : {value.toLocaleTimeString()}:{value.getMilliseconds().toLocaleString('fr-FR', {minimumIntegerDigits: 3})}</p>
      </main>
    </>
  );
}

function Items() {
  return (
    <>
      <main>
        <h2>Where are you items?</h2>
        <p>I want to find some valuable items for make me rich.</p>
      </main>
      <ItemsApp></ItemsApp>
    </>
  );
}

function Grocery() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [message, setMessage] = useState("");
  useEffect(() => {
    fetch("https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/pokedex.json")
    .then(res => res.json())
    .then(
      (result) => {
        setIsLoaded(true);
        setMessage(result);
      },
      (error) => {
        setIsLoaded(true);
        setError(error);
      }
    )
  }, []);
  return <p>message</p>;
}

function Fetch() {
  return (
    <>
      <main>
        <h2>It's Hot.</h2>
        <p>I want to sell some hot spice.</p>
      </main>
      <CoursesApp></CoursesApp>
    </>
  );
}



function About() {
  return (
    <>
      <main>
        <h2>Who are we?</h2>
        <p>
          That feels like an existential question, don't you
          think?
        </p>
      </main>
      <iframe width="560" height="315"
      src="https://www.youtube.com/embed/OJYWVCGe0Jk"
      title="YouTube video player" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen></iframe>
    </>
  );
}

export default App;
