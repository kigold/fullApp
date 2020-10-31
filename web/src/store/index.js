import * as user from '@/store/modules/user'
import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'
import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    teams: [],
    games: [],
    user: {}
  },
  mutations: {
    ...mutations,
    SAVE_CURRENT_USER(state, user) {
      state.user = { ...state.user, user }
      state.token = user.token
    }
  },
  actions: {
    ...actions
  },
  modules: { user },
  getters: {
    teamsCount: (state, getters) => {
      console.log(getters)
      return state.teams.length
    }
  }
})
