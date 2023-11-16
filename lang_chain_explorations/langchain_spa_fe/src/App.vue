<script setup lang="ts">
import { ref } from '@vue/reactivity';
import { RemoteRunnable } from 'langchain/runnables/remote'

const topic = ref<string>('electron');
const field = ref<string>('physics');

const chat = new RemoteRunnable({
  url: "http://localhost:8000/topics"
});

async function prompt() {
  console.log('Prompting...')
  const result = await chat.stream({"topic": topic.value, "field": field.value});
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
  <div class="flex flex-col">
    <label class="text-sm font-medium">Topic</label>
    <input class="rounded-sm border border-slate-400 w-[200px]" type="text" :value="topic" @input="event => topic = (event.target as any).value">
  </div>
  <div class="flex flex-col">
    <label class="text-sm font-medium">Field</label>
    <input class="rounded-sm border border-slate-400 w-[200px]" type="text" :value="field" @input="event => field = (event.target as any).value">
  </div>
  <button class="bg-slate-400 px-3 py-1 rounded-sm hover:bg-slate-500 active:bg-slate-300" @click="prompt">Prompt</button>
</template>

<style scoped>

</style>
