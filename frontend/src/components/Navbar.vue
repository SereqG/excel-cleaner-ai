<template>
  <nav class="flex items-center justify-between px-10 mt-2 w-full">
    <div class="text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-fuchsia-600">
      <p class="font-bold text-xl">Excel Cleaner</p>
    </div>
    <div class="flex space-x-5 justify-center items-center">
      <ul class="flex space-x-5 text-gray-600 font-bold">
        <li>
          <router-link to="/">Home</router-link>
        </li>
        <li>
          <router-link to="/">Features</router-link>
        </li>
        <li>
          <router-link to="/">About</router-link>
        </li>
      </ul>
      <button
        class="p-2 px-4 bg-white text-violet-600 border rounded-xl font-bold hover:bg-violet-100 hover:text-violet-700 transition duration-300"
      >
        Sign In
      </button>
      <button
        class="p-2 px-4 bg-gradient-to-r from-violet-600 to-fuchsia-600 text-white font-bold rounded-xl hover:from-violet-700 hover:to-fuchsia-700 transition duration-300"
      >
        Get Started
      </button>
    </div>
  </nav>
</template>
