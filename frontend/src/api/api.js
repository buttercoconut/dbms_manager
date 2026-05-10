import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8080/api', // Adjust to your backend URL
  timeout: 10000
})

export default {
  getUsers() {
    return apiClient.get('/users')
  },
  getTables() {
    return apiClient.get('/tables')
  }
}
