<template>
    <header>
        <div class="container">
            <nav>
                <ul class="nav__list">
                    <li class="nav__item">Тяжеловенько)</li>
                    <li class="nav__item">
                        <router-link :to="{name: 'graphs'}">Статистика</router-link>
                    </li>
                </ul>
                <p class="nav__login">
                    
                    <a class="custom-link" v-if="auth" v-on:click="logout">Logout</a>
                    <router-link v-else :to="{name: 'auth'}">Выход</router-link>


                </p>
            </nav>
        </div>
    </header>
</template>

<script>

    export default {
        data() {
            return {
                auth: false
            }
        },
        methods: {
            is_auth() {
                if (this.$cookies.get('access_token')) {
                    this.auth = true;
                } else {
                    this.$router.push({name: 'auth'})
                }
            },
            logout() {
                this.$cookies.remove('access_token')
                this.$router.push({name: 'auth'})
            }
        },
        created() {
            this.is_auth()
        }
    }

</script>

<style scoped>
    header {
        background-color: #f5a623;
    }

    nav {
        display: flex;
        justify-content: space-between;
        height: 50px;
        align-items: center;
    }
    .nav__list {
        display: flex;
        justify-content: space-between;
        width: 250px;
    }

</style>