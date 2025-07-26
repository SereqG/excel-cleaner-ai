<template>
  <div class="relative group">
    <div
      class="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl blur opacity-25 group-hover:opacity-40 transition-opacity"
    ></div>
    <div class="relative bg-white rounded-2xl p-2 shadow-xl">
      <div
        className=" backdrop-blur-sm rounded-2xl p-6 border border-white/20 hover:bg-white/20 transition-all duration-300 group"
      >
        <h3 className="text-xl font-semibold text-gray-800 mb-2">{{ title }}</h3>
        <p className="text-gray-600">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { title, description, action } = defineProps<{
  title?: string
  description?: string
  action?: () => void
}>()
console.log('QuickAction props:', title, description, action)
</script>
