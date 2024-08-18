/**
 * plugins/index.ts
 *
 * Automatically included in `./src/main.ts`
 */

// Plugins
import { $vuetify } from './vuetify'
import pinia from '../stores'
import router from '../router'
import { useNotifierPlugin } from 'vue3-notifier'

// Types
import type { App } from 'vue'

export function registerPlugins (app: App) {
  app
    .use(pinia)
    .use($vuetify)
    .use(useNotifierPlugin({
      id: 'top right',
      position: 'top right',
    }))
    .use(router)
}