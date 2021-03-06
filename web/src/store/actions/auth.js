import { SAVE_CURRENT_USER } from '@/helper/mutationsConstants'
import AuthService from '@/service/AuthService'
import VueJwtDecode from 'vue-jwt-decode'

export default {
  async login({ commit }, payload) {
    try {
      const response = await AuthService.login(payload)
      if (response.data.has_error) {
        console.log('There was an error:' + response.data.error)
      } else {
        console.log('Logging')
        console.log(response.data.data)
        localStorage.setItem('user-token', response.data.data.access)
        const user = VueJwtDecode.decode(response.data.data.access)
        AuthService.getInstance().defaults.headers.common['Authorization'] =
          'Bearer ' + response.data.data.access
        commit(SAVE_CURRENT_USER, {
          name: user.name,
          id: user.user_id,
          refresh_token: response.data.data.refresh,
          token: response.data.data.access
        })
        console.log('Just finished getting token')
      }
    } catch (error) {
      console.log('There was an error:' + error)
    }
  }
}
