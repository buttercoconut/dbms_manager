<template>
  <div>
    <h2>Data Table</h2>
    <table>
      <thead>
        <tr>
          <th v-for="col in columns" :key="col">{{ col }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id">
          <td v-for="col in columns" :key="col">{{ row[col] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/api'

const columns = ref([])
const rows = ref([])

onMounted(async () => {
  try {
    const response = await api.getTables()
    const data = response.data
    if (data.length) {
      columns.value = Object.keys(data[0])
      rows.value = data
    }
  } catch (err) {
    console.error(err)
  }
})
</script>
