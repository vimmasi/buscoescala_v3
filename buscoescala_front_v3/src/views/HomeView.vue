<template>
  <div class="flex justify-between items-center bg-gray-800 text-white p-4">
    <h1 class="text-2xl font-bold">Busco Escala - FRONT</h1>
    <button @click="signOut" type="submit"
      class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-500/80 cursor-pointer">
      Sair
    </button>
  </div>
  <div class="container mx-auto p-4">
    <div class="mb-8">
      <h2 class="text-xl font-semibold mb-2">Escalas</h2>
      <div v-if="loading">Carregando escalas...</div>
      <div v-else-if="escalas.length === 0">Nenhuma escala encontrada.</div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="escala in escalas" :key="escala.id"
          class="border p-4 rounded shadow hover:shadow-lg transition-shadow duration-200 ease-in-out cursor-pointer"
          :class="{ 'border-blue-500': selectedEscala?.id === escala.id }">
          <div class="flex justify-between">
            <h3 class="text-lg font-medium">{{ escala.mes }}</h3>
            <!-- <p>ID: {{ escala.id }}</p> -->
            <p>
              Militares: {{ escala.militares ? escala.militares.length : 0 }}
            </p>
          </div>
          <button @click="selectEscala(escala)"
            class="mt-2 px-3 py-1 bg-blue-500 hover:bg-blue-500/80 cursor-pointer text-white rounded">
            Selecionar
          </button>
        </div>
      </div>
    </div>

    <div v-if="selectedEscala" class="mb-8">
      <h2 class="text-xl font-semibold mb-2">
        Militares da Escala: {{ selectedEscala.mes }}
      </h2>

      <div class="mb-4">
        <h3 class="text-lg font-medium mb-2">Adicionar Novo Militar</h3>
        <form @submit.prevent="adicionarMilitar" class="flex flex-col gap-2">
          <div>
            <label class="block">Patente:</label>
            <input v-model="novoMilitar.patente" required class="border p-2 w-full rounded" />
          </div>
          <div>
            <label class="block">Nome:</label>
            <input v-model="novoMilitar.nome" required class="border p-2 w-full rounded" />
          </div>
          <button type="submit" class="px-4 py-2 bg-green-500 text-white rounded">
            Adicionar Militar
          </button>
        </form>
      </div>

      <div v-if="selectedEscala.militares.length === 0">
        Nenhum militar nesta escala.
      </div>
      <div v-else>
        <div v-for="militar in selectedEscala.militares" :key="militar.id"
          class="border p-4 rounded mb-2 flex justify-between items-center">
          <div>
            <p>
              <strong>{{ militar.patente }}</strong> {{ militar.nome }}
            </p>
            <p>ID: {{ militar.id }}</p>
          </div>
          <div v-if="editandoMilitar && editandoMilitar.id === militar.id">
            <form @submit.prevent="atualizarMilitar" class="flex gap-2">
              <input v-model="editandoMilitar.patente" placeholder="Patente" required class="border p-1 rounded" />
              <input v-model="editandoMilitar.nome" placeholder="Nome" required class="border p-1 rounded" />
              <button type="submit" class="px-2 py-1 bg-blue-500 text-white rounded">
                Salvar
              </button>
              <button type="button" @click="cancelarEdicao" class="px-2 py-1 bg-gray-500 text-white rounded">
                Cancelar
              </button>
            </form>
          </div>
          <div v-else class="flex gap-2">
            <button @click="iniciarEdicao(militar)" class="px-2 py-1 bg-yellow-500 text-white rounded">
              Editar
            </button>
            <button @click="removerMilitar(militar.id)" class="px-2 py-1 bg-red-500 text-white rounded">
              Remover
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!selectedEscala" class="text-center text-gray-500">
      Selecione uma escala para gerenciar militares
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from "vue";
import { supabase } from "@/lib/supabaseClient";
import router from "@/router";
import axios from "axios";

// Desconectar o usuário
async function signOut() {
  const { error } = await supabase.auth.signOut();
  if (error) {
    console.error("Erro ao fazer logout:", error);
  } else {
    router.push("/login");
  }
}

const API_URL = "http://localhost:5001";

// Gerenciamento de estado
const escalas = ref([]);
const loading = ref(true);
const selectedEscala = ref(null);
const novoMilitar = reactive({
  patente: "",
  nome: "",
  escala_id: null,
});
const editandoMilitar = ref(null);

// Carregar os dados da escala
const carregarEscalas = async () => {
  try {
    loading.value = true;
    const response = await axios.get(`${API_URL}/escala/escalas`);
    escalas.value = response.data;
  } catch (error) {
    console.error("Erro ao carregar escalas:", error);
    alert("Erro ao carregar escalas. Verifique o console para mais detalhes.");
  } finally {
    loading.value = false;
  }
};

const selectEscala = async (escala) => {
  try {
    loading.value = true;
    const response = await axios.get(`${API_URL}/escala/escalas/${escala.id}`);
    selectedEscala.value = response.data;
    novoMilitar.escala_id = escala.id;
  } catch (error) {
    console.error("Erro ao selecionar escala:", error);
    alert("Erro ao selecionar escala. Verifique o console para mais detalhes.");
  } finally {
    loading.value = false;
  }
};

// Gerenciamento de militares (adicionar, modificar e remover)
const adicionarMilitar = async () => {
  try {
    const response = await axios.post(`${API_URL}/militar/militares`, {
      patente: novoMilitar.patente,
      nome: novoMilitar.nome,
      escala_id: selectedEscala.value.id,
    });

    selectedEscala.value.militares.push(response.data);

    // Limpeza simples de formulário
    novoMilitar.patente = "";
    novoMilitar.nome = "";

    alert("Militar adicionado com sucesso!");
  } catch (error) {
    console.error("Erro ao adicionar militar:", error);
    alert("Erro ao adicionar militar. Verifique o console para mais detalhes.");
  }
};

const iniciarEdicao = (militar) => {
  editandoMilitar.value = { ...militar };
};

const cancelarEdicao = () => {
  editandoMilitar.value = null;
};

const atualizarMilitar = async () => {
  try {
    const response = await axios.put(
      `${API_URL}/militar/militares/${editandoMilitar.value.id}`,
      {
        patente: editandoMilitar.value.patente,
        nome: editandoMilitar.value.nome,
        escala_id: selectedEscala.value.id,
      },
    );

    const index = selectedEscala.value.militares.findIndex(
      (m) => m.id === editandoMilitar.value.id,
    );
    if (index !== -1) {
      selectedEscala.value.militares[index] = response.data;
    }

    editandoMilitar.value = null;

    alert("Militar atualizado com sucesso!");
  } catch (error) {
    console.error("Erro ao atualizar militar:", error);
    alert("Erro ao atualizar militar. Verifique o console para mais detalhes.");
  }
};

const removerMilitar = async (id) => {
  if (!confirm("Tem certeza que deseja remover este militar?")) {
    return;
  }

  try {
    await axios.delete(`${API_URL}/militar/militares/${id}`);

    selectedEscala.value.militares = selectedEscala.value.militares.filter(
      (m) => m.id !== id,
    );

    alert("Militar removido com sucesso!");
  } catch (error) {
    console.error("Erro ao remover militar:", error);
    alert("Erro ao remover militar. Verifique o console para mais detalhes.");
  }
};

// Bloco de inicialização
onMounted(() => {
  carregarEscalas();
});
</script>
