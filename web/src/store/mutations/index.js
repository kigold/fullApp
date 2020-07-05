import game_mutations from './games'
import team_mutations from './teams'
export default {
  ...team_mutations,
  ...game_mutations
}
