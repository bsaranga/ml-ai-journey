<script setup lang="ts">
import { RemoteRunnable } from 'langchain/runnables/remote'

const chat = new RemoteRunnable({
  url: "http://localhost:8000/openai"
});

const result = await chat.stream({text: "hello world"});

for await (const chunk of result) {
  console.log(chunk);
}

</script>

<template>
  <div class="font-bold text-xl">Hello world...</div>
</template>

<style scoped>

</style>
