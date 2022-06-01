import { useEffect, useState } from 'react';
import { Routes, Route, Outlet, NavLink, useNavigate, useParams } from 'react-router-dom';
import { getMailAddresses, getPeople, getPerson, addPerson, addMail } from './api';

export const AddressBook = () => {
    return <div>
        <ul className="Menu">
            <li><NavLink to="people">People</NavLink></li>
            <li><NavLink to="groups">Groups</NavLink></li>
        </ul>
        <Outlet/>
    </div>;
};

export const People = () => {
    const [people, setPeople] = useState([]);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();
    useEffect(() => {
        getPeople()
            .then(data => {
                setPeople(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    const add_person = (p) => {
        return addPerson(p)
        .then(newP => {
            setPeople(cur => [newP, ...cur]);
        });
    };

    return <>
        <h3>Address book</h3>
        {loading ? <p>Loading...</p> :
            error ? <p style={{ color: 'red' }}>{error}</p> :
                <div style={{ display: 'flex' }}>
                    <div>
                        <NavLink to="new">Nouvelle personne</NavLink>
                        <ul style={{ paddingRight: "1rem", borderRight: "black solid 1px" }}>
                            {people.map(p => <li style={{display: 'block'}} key={p.id} onClick={() => navigate(`${p.id}`)}>
                                {p.firstname} {p.lastname}
                            </li>)}
                        </ul>
                    </div>
                    <div style={{ padding: "1rem" }}>
                        <Routes>
                            <Route path=":id" element={<Person />} />
                            <Route path="new" element={<PersonAddForm onAdd={add_person} />} />
                        </Routes>
                        <Outlet />
                    </div>
                </div>
        }
    </>;
};

export const Groups = () => {
    return <div style={{ display: 'flex' }}>
        <div>
            <NavLink to="new">Nouveau groupe</NavLink>
        </div>
        <div style={{ padding: "1rem" }}>
            <Outlet />
        </div>
    </div>;
};

export const Person = () => {
    const { id } = useParams();

    const [person, setPerson] = useState(null);
    const [mailAddresses, setMailAddresses] = useState([]);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        Promise.all([getPerson(id), getMailAddresses(id)])
            .then(([p, ma]) => {
                setPerson(p);
                setMailAddresses(ma);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, [id]);

    const add_mail_address = (m) => {
        return addMail(m, id)
        .then(newMail => {
            setMailAddresses(cur => [newMail, ...cur]);
        });
    };

    return loading ? <p>Loading...</p> :
        error ? <p style={{ color: 'red' }}>{error}</p> :
            <>
                <h4>Détails de {person.firstname} {person.lastname} n°{id}</h4>
                <MailAddForm onAdd={add_mail_address} />
                <ul>
                    {mailAddresses.map(m => <li key={m.id}>{m.address}</li>)}
                </ul>
            </>;
};

export const PersonAddForm = ({onAdd}) => {
    const [lastname, setCurrentLastname] = useState("");
    const [firstname, setCurrentFirstname] = useState("");
    const [enabled, setEnabled] = useState(true);
    const handleAdd = () => {
        setEnabled(false);
        onAdd({firstname, lastname})
        .then(() => {
            setCurrentFirstname('');
            setCurrentLastname('');
        })
        .finally(() => {
            setEnabled(true);
        });
    };
    const handleChange = e => {setCurrentFirstname(e.target.value)};
    const handleChange2 = e => {setCurrentLastname(e.target.value)};
    return <>
    <input type="text" onChange={handleChange} placeholder="FirstName" value={firstname}></input>
    <input type="text" onChange={handleChange2} placeholder="LastName" value={lastname}></input>
    <button disabled={!enabled} onClick={handleAdd} type="submit">Ajouter une personne</button></>;
};

export const MailAddForm = ({onAdd}) => {
    const [address, setCurrentAddress] = useState("");
    const [enabled, setEnabled] = useState(true);
    const [error, setError] = useState(null);
    const handleAdd = () => {
        setEnabled(false);
        setError(null);
        onAdd({address})
        .then(() => {
            setCurrentAddress('');
        })
        .catch(err => setError(err))
        .finally(() => {
            setEnabled(true);
        });
    };
    const handleChange = e => {setCurrentAddress(e.target.value)};
    return <>
        <input type="text" onChange={handleChange} placeholder="Address@e.mail" value={address}/>
        <button disabled={!enabled} onClick={handleAdd} type="submit">Ajouter une AddressMail</button>
        {error ? <p style={{color: 'red'}}>{error.message}</p> : null}
    </>;
};
