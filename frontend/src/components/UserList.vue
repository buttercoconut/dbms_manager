<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }} ({{ user.email }})
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/api'

const users = ref([])

onMounted(async () => {
  try {
    const response = await api.getUsers()
    users.value = response.data
  } catch (err) {
    console.error(err)
  }
})
</script>
