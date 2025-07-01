<template>
  <div class="w-full h-screen flex flex-col items-center justify-center text-center">
    <Tagline />
    <WelcomeHeader />
    <UploadFileField />
  </div>
</template>

<script setup>
import Tagline from '@/components/Tagline.vue'
import UploadFileField from '@/components/UploadFileField.vue'
import WelcomeHeader from '@/components/WelcomeHeader.vue'
import { ref } from 'vue'
</script>
