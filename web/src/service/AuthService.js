import axios from './index.service'

export default class AuthService {
  static getInstance() {
    return axios
  }
  static signUp(payload) {
    return axios.post(`/profile/`, payload)
  }

  static login(payload) {
    return axios.post(`/api/token/`, payload)
  }
}
