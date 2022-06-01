const delay = res => {
    return new Promise((resolve) => {
        setTimeout(() => resolve(res), 1000);
    });
};

const checkStatus = response => {
    if (response.ok) {
        return response;
    } else {
        return response.text()
            .then(text => {
                throw new Error(text);
            });
    }
};

const URL = 'http://localhost:3000';

export const getPeople = () => {
    return fetch(URL + '/person')
        .then(delay)
        .then(checkStatus)
        .then(res => res.json());
};

export const getPerson = (id) => {
    return fetch(URL + '/person/' + id)
        .then(delay)
        .then(checkStatus)
        .then(res => res.json());
};

export const getMailAddresses = (id) => {
    return fetch(URL + '/person/' + id + '/mailAddress')
        .then(delay)
        .then(checkStatus)
        .then(res => res.json());
};

export const addPerson = (data) => {
    return fetch(URL + '/person', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(delay)
        .then(checkStatus)
        .then(res => res.json());
};


export const addMail = (data,id) => {
    return fetch(URL + '/person/'+ id +"/mailAddress", {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(delay)
        .then(checkStatus)
        .then(res => res.json());
};
