import auth_actions from './auth'
import game_actions from './games'
import team_actions from './teams'

export default {
  ...auth_actions,
  ...game_actions,
  ...team_actions
}
