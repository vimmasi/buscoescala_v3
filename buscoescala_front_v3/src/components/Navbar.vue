<template>
  <nav class="navbar bg-gray-800 text-white p-4">
    <ul class="nav-links flex justify-around">
      <li>
        <router-link class="hover:text-gray-300" to="/">Home</router-link>
      </li>
      <li class="text-gray-500">|</li>
      <li>
        <router-link class="hover:text-gray-300" to="/login">Login</router-link>
      </li>
    </ul>
  </nav>
</template>
