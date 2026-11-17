import axios from 'axios'

// Una sola configuración para las peticiones al backend de Django.
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 10000,
})

export default api
