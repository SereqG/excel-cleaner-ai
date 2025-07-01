<script setup lang="ts">
import Navbar from './components/Navbar.vue'
</script>

<template>
  <div
    class="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-pink-50 relative overflow-hidden"
  >
    <div class="absolute inset-0 overflow-hidden">
      <div
        class="absolute -top-40 -right-40 w-80 h-80 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
      ></div>
      <div
        class="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
      ></div>
      <div
        class="absolute top-40 left-40 w-60 h-60 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
      ></div>
    </div>
    <Navbar />
    <router-view> </router-view>
  </div>
</template>
