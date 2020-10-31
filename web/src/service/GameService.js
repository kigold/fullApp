import axios from './index.service'

export default class GameService {
  static getInstance() {
    return axios
  }
  static getGames() {
    return axios.get(`/games/fixtures/`)
  }
}
