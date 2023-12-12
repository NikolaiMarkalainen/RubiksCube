import axios from 'axios'

export const getRequest = async () => {
    axios.get('http://localhost:5001')
    .then(response => {
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    })
}

export const postImage = async (file) => {
    try{
        const response = await axios.post('http://localhost:5001/',file)
        console.log('Server response:', response.data);
    }
    catch(error) {
        console.log('ERROR:', error)
    } 
}

