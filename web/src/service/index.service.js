import axios from 'axios'
import config from './../config'

const { apiBaseUrl } = config

const instance = axios.create({
  baseURL: apiBaseUrl,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json;charset=utf-8'
  }
})

export default instance
