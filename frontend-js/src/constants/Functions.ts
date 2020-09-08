import axios from 'axios'
import { URL_BASE } from './Constants'

async function requestApi(method: "GET" | "POST" | "PUT" | "DELETE", path: string, body?: object) {
    const url = `${URL_BASE}/${path}`

    return await axios({ 
        method: method, 
        url,
        data: body
    })
    .then(response => response.data)
    .catch(error => error)
}

export {
    requestApi
}