<template>
  <Header></Header>
  <main>
    <div class="container">
      <div class="wallet-wrapper">
        <Wallet></Wallet>
      </div>
    </div>
  </main>
</template>

<script>
// @ is an alias to /src

import Header from '@/components/Header.vue';
import Wallet from '@/components/Wallet.vue';

export default {
  name: 'HomeView',
  components: {
    Header,
    Wallet
  }
}
</script>

<style>
  .wallet-wrapper {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
  }
</style>