<template>
  <div class="container">
    <h1>Busca de Procedimentos ANS</h1>
    
    <div class="search-box">
      <input
        v-model="termoBusca"
        @keyup.enter="buscar"
        placeholder="Digite um procedimento..."
      />
      <button @click="buscar" :disabled="carregando">
        {{ carregando ? 'Buscando...' : 'Buscar' }}
      </button>
    </div>

    <div v-if="erro" class="error-message">
      {{ erro }}
    </div>

    <div v-if="resultados.length" class="results-table">
      <table>
        <thead>
          <tr>
            <th v-for="coluna in colunas" :key="coluna">
              {{ formatarColuna(coluna) }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in resultados" :key="index">
            <td v-for="coluna in colunas" :key="coluna">
              {{ item[coluna] || '-' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else-if="!carregando && termoBusca" class="no-results">
      Nenhum resultado encontrado para "{{ termoBusca }}"
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

interface Procedimento {
  [key: string]: string | number
}

const termoBusca = ref('')
const resultados = ref<Procedimento[]>([])
const carregando = ref(false)
const erro = ref<string | null>(null)

const colunas = computed(() => {
  return resultados.value.length 
    ? Object.keys(resultados.value[0])
    : []
})

const formatarColuna = (coluna: string) => {
  const formatacoes: Record<string, string> = {
    'Seg. Odontológica': 'Odontológico',
    'Seg. Ambulatorial': 'Ambulatorial',
    'PROCEDIMENTO': 'Procedimento'
  }
  return formatacoes[coluna] || coluna
}

const buscar = async () => {
  if (!termoBusca.value.trim()) {
    erro.value = 'Por favor, digite um termo para buscar'
    return
  }

  carregando.value = true
  erro.value = null

  try {
    const response = await fetch(
      `http://localhost:8000/api/buscar?termo=${encodeURIComponent(termoBusca.value)}&limite=20`
    )

    if (!response.ok) {
      throw new Error('Erro ao buscar dados')
    }

    resultados.value = await response.json()
  } catch (err) {
    erro.value = err instanceof Error ? err.message : 'Erro desconhecido'
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 1rem;
}

.search-box {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
}

input {
  flex: 1;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #3aa876;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff4444;
  background-color: #ffeeee;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.results-table {
  overflow-x: auto;
  margin-top: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #eee;
}

th {
  background-color: #f5f5f5;
  font-weight: 600;
}

tr:hover {
  background-color: #f9f9f9;
}

.no-results {
  text-align: center;
  padding: 2rem;
  color: #666;
}
</style>