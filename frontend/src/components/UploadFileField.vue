<template>
  <div class="max-w-2xl mx-auto mb-12">
    <div class="relative group">
      <div
        class="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl blur opacity-25 group-hover:opacity-40 transition-opacity"
      ></div>
      <div class="relative bg-white rounded-2xl p-2 shadow-xl">
        <div class="flex items-center space-x-4">
          <div class="flex-1 flex items-center space-x-3 px-4">
            <div class="flex w-full items-center justify-end space-x-5 min-w-96">
              <input
                type="file"
                id="file-upload"
                accept="*/*"
                class="hidden"
                @change="handleFileChange"
              />
              <div v-if="selectedFile" class="mt-2 text-sm text-gray-600">
                Selected file: <strong>{{ selectedFile.name }}</strong> ({{
                  (selectedFile.size / 1024).toFixed(2)
                }}
                KB)
              </div>
              <label
                for="file-upload"
                class="cursor-pointer flex items-center justify-center h-12 px-4 bg-white border border-gray-300 rounded-lg shadow-sm text-gray-700 hover:bg-gray-50 transition-colors"
              >
                Upload File
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
    <QuickAction
      v-for="(action, index) in quickActions"
      :key="index"
      :title="action.title"
      :description="action.description"
      :action="action.action"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import QuickAction from './QuickAction.vue'

const selectedFile = ref<File | null>(null)

const quickActions = [
  {
    title: 'Format Dates',
    description: 'Automatically format dates in your spreadsheet',
    action: () => console.log('Action 1 clicked'),
  },
  {
    title: 'Fill Empty Cells',
    description: 'Quickly fill empty cells with default values',
    action: () => console.log('Action 2 clicked'),
  },
  {
    title: 'Custom Action',
    description: 'Use AI to modify your spreadsheet',
    action: () => console.log('Action 3 clicked'),
  },
]

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  const files = target.files
  if (files && files.length > 0) {
    selectedFile.value = files[0]
    // You can add file upload logic here if needed
    console.log('File selected:', selectedFile.value)
  } else {
    selectedFile.value = null
  }
}
</script>
