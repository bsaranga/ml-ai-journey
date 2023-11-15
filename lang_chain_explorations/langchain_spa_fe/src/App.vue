<script setup lang="ts">
import { RemoteRunnable } from 'langchain/runnables/remote'

const chat = new RemoteRunnable({
  url: "http://localhost:8000/openai"
});

async function prompt() {
  console.log('Prompting...')
  const result = await chat.stream({text: "hello world"});
  const reader = result.getReader();

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done)
        break;
      else console.log(value)
    }
  } catch (error) {
    console.error(error)
  } finally {
    reader.releaseLock();
    console.log('lock released')
  }
}

</script>

<template>
  <div class="font-bold text-xl">Langchain tests</div>
  <button class="bg-slate-400 px-3 py-1 rounded-sm hover:bg-slate-500 active:bg-slate-300" @click="prompt">Prompt</button>
</template>

<style scoped>

</style>
