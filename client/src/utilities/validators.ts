export const emailRules = [
  (value: string) => {
    if (value) return true
    return 'You must enter an email.'
  },
  (value: string) => {
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) return true
    return 'Email must be a valid email address.'
  },
]
export const nameRules = [
  (value: string) => {
    if (value) return true
    return 'You must enter a name.'
  },
  (value: string) => {
    if (value?.length > 4) return true
    return 'Name must be at least 5 character.'
  },
  (value: string) => {
    if (value?.length < 49) return true
    return 'Name must be at most 50 characters.'
  },
  (value: string) => {
    if (/[^0-9]/.test(value)) return true
    return 'Name can not contain digits.'
  },
]

export const passwordRules = [
  (value: string) => {
    if (value) return true
    return 'You must enter a password.'
  },
  (value: string) => {
    if (value?.length > 3) return true
    return 'Password must be at least 4 character.'
  },
  (value: string) => {
    if (value?.length < 127) return true
    return 'Password must be at most 128 characters.'
  },
]

export function confirmedPasswordRule (newPassword: string) {
  return [
    (confirmPassword: string) => {
      if (newPassword) {
        if (newPassword === confirmPassword) return true
        return 'Passwords does not match'
      }
      return 'You must enter new password first.'
    },
  ]
}
