<template>
  <div>
    <div class="flex items-center justify-center">
      <button
        type="button"
        @click="openModal"
        class="
          px-4
          py-2
          text-sm
          font-medium
          text-white
          bg-black
          rounded-md
          bg-opacity-20
          hover:bg-opacity-30
          focus:outline-none
          focus-visible:ring-2
          focus-visible:ring-white
          focus-visible:ring-opacity-75
        "
      >
        Help
      </button>
    </div>
    <TransitionRoot appear :show="isOpen" as="template">
      <Dialog as="div" @close="closeModal">
        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="min-h-screen px-4 text-center">
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0"
              enter-to="opacity-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100"
              leave-to="opacity-0"
            >
              <DialogOverlay class="fixed inset-0 bg-slate-900/70" />
            </TransitionChild>

            <span class="inline-block h-screen align-middle" aria-hidden="true">
              &#8203;
            </span>

            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <div
                class="
                  inline-block
                  w-full
                  max-w-xl
                  p-6
                  my-8
                  overflow-hidden
                  text-left
                  align-middle
                  transition-all
                  transform
                  bg-white
                  shadow-xl
                  rounded-2xl
                "
              >
                <DialogTitle
                  as="h3"
                  class="text-lg font-medium leading-6 text-gray-900"
                >
                  Help
                </DialogTitle>
                <div class="mt-4">
                  <p class="text-indigo-500 font-medium">
                    Autocomplete function returns suggestions, top tags, and
                    records.
                  </p>
                  <p class="text-sm text-gray-900 font-medium mt-4">
                    Suggestions
                  </p>
                  <ul class="list-inside list-disc text-sm text-gray-700 my-2">
                    <li>
                      With each character typed into the search box, you will
                      see the suggestions change.
                    </li>
                    <li>You select anyone of the suggestions</li>
                    <li>
                      You can implement this feature before implement the Search
                      function
                    </li>
                  </ul>
                  <p class="text-sm text-gray-900 font-medium mt-4">Records</p>
                  <ul class="list-inside list-disc text-sm text-gray-700 my-2">
                    <li>Records show top full-text search results.</li>
                    <li>
                      Unlike the Search function, Autocomplete does not provide
                      semantic re-ranking and limits the results to 25.
                    </li>
                    <li>
                      Implement this for allowing users to get quick search
                      results.
                    </li>
                    <li>
                      Seqwa's Autocomplete function is incredibly less expensive
                      than Search function.
                    </li>
                  </ul>
                </div>

                <div class="mt-6">
                  <button
                    type="button"
                    class="
                      inline-flex
                      justify-center
                      px-4
                      py-2
                      text-sm
                      font-medium
                      text-blue-900
                      bg-blue-100
                      border border-transparent
                      rounded-md
                      hover:bg-blue-200
                      focus:outline-none
                      focus-visible:ring-2
                      focus-visible:ring-offset-2
                      focus-visible:ring-blue-500
                    "
                    @click="closeModal"
                  >
                    Got it, thanks!
                  </button>
                </div>
              </div>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogOverlay,
  DialogTitle,
} from "@headlessui/vue";

const isOpen = ref(true);

function closeModal() {
  isOpen.value = false;
}
function openModal() {
  isOpen.value = true;
}
</script>
