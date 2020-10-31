import { SAVE_GAMES } from '@/helper/mutationsConstants'
import GameService from '@/service/GameService'

export default {
  get_games({ commit }) {
    GameService.getGames()
      .then(response => {
        if (response.data.has_error) {
          console.log('There was an error:' + response.data.error)
        } else {
          console.log('Logging')
          console.log(response.data.data.results)
          commit(SAVE_GAMES, response.data.data.results)
        }
      })
      .catch(error => {
        console.log('There was an error:' + error)
      })
  }
}
