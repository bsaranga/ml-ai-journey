<script setup lang="ts">
import { ref } from '@vue/reactivity';
import { RemoteRunnable } from 'langchain/runnables/remote'
import type Topic from './models/topic';

const topic = ref<string>('electron');
const field = ref<string>('physics');

const list = ref<Topic>({ topics: ['abc', 'def', 'ghi'] });

const chat = new RemoteRunnable({
  url: "http://localhost:8000/topics"
});

async function prompt2() {
  const response = await fetch('http://localhost:8000/topics/stream', {
    method: "POST",
    body: JSON.stringify({
    "input": {
      "topic": topic.value,
      "field": field.value
    }})
  })

  const reader = response.body!.pipeThrough(new TextDecoderStream()).getReader()

  while (true) {
    const {value, done} = await reader.read()
    if (done) break;
    const rawData = value.split('\n')[1]
    if (rawData != '' && rawData != '\n') {
      const jsonStr = rawData.split('data: ')[1]
      if (jsonStr != undefined) {
        const jsonData = JSON.parse(jsonStr);
        console.log(jsonData)
        list.value = jsonData;
      }
    }
  }
  
  reader.releaseLock();
}

async function prompt() {
  console.log('Prompting...')
  const result = await chat.stream({"topic": topic.value, "field": field.value});
  const reader = result.getReader();

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done)
        break;
      else {
        list.value = value as Topic
        console.log(value)
      }
    }
  } catch (error) {
    console.error(error)
    list.value.topics.pop()
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
  <button class="bg-slate-400 px-3 py-1 rounded-sm hover:bg-slate-500 active:bg-slate-300" @click="prompt2">Prompt</button>

  <ul class="ml-4 mt-2">
    <li v-for="topic in list.topics">{{ topic }}</li>
  </ul>
</template>

<style scoped>

</style>
