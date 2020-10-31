import axios from './index.service'

//const { pageSize } = config

export default class TeamService {
  static getTeams() {
    return axios.get('/teams/')
  }
}
