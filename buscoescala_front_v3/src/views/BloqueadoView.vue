<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="text-center">
      <h1 class="text-6xl font-bold text-red-500">401</h1>
      <p class="mt-4 text-xl text-gray-700">Acesso não autorizado</p>
      <p class="mt-2 text-gray-600">
        Você não tem permissão para visualizar essa página.
      </p>
      <router-link
        to="/login"
        class="mt-6 inline-block px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
      >
        Logar
      </router-link>
    </div>
  </div>
</template>
