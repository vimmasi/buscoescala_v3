<script setup>
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import { ref, onMounted } from "vue";
import { supabase } from "./lib/supabaseClient";
</script>

<template>
  <!-- <header>
    <Navbar />
  </header> -->

  <div>
    <RouterView />
  </div>
</template>
