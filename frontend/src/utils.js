import { ref } from "vue";

export const state = ref({ currentUser: null });

export const getCurrentUser = async () => {
  const response = await fetch('http://localhost:8000/api/v1/user/get_current_user', {
    method: 'get',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.cookie.split('csrftoken=').slice(-1)[0].split(';')[0]
    }
  });

  if (response.ok) {
    return await response.json();
  }
}