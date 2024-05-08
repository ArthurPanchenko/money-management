<template>
    <div class="wallet-content">
        <div class="wallet">
            <h1 class="wallet__left-money">
                У вас осталось {{ wallet.left_money }} до {{ wallet.left_date }}
            </h1>
            <h3 class="wallet__daily-available">Доступно на сегодня: {{ wallet.daily }}</h3>
            <button @click="toggleFormBtn" id="toggleFormBtn" class="wallet__form__button">Обновить</button>
        </div>
        <form @submit.prevent="createPurchase" class="wallet__form" id="createForm">
            <label for="title">Купить</label>
            <input type="text" name="title" class="wallet__form__input" required="true">
            <label for="spend">За цену</label>
            <input type="number" name="spend" class="wallet__form__input" required="true">
            <button class="wallet__form__button" type="submit">Потратить</button>
        </form>
        <form @submit.prevent="updateWallet" class="wallet__form" id="updateForm">
            <label for="money">Осталось</label>
            <input type="number" name="money" class="wallet__form__input" required="true">
            <label for="date">До</label>
            <input type="date" name="date" class="wallet__form__input" required="true">
            <button class="wallet__form__button" type="submit">Обновить</button>
        </form>
    </div>
    <div class="wallet__spends">
        <h3>Последние покупки</h3>
        <ul class="wallet__spends__list">
            <li v-for="purchase in wallet.purchases" :key="purchase.id" class="wallet__spends__item">
                <p class="wallet__spend__title">{{ purchase.title }}</p>
                <p class="wallet__spend__price">{{ purchase.amount }}</p>
                <p class="wallet__spend__date">{{ purchase.purchase_date }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios';
    import { axiosUrl } from '@/main';

    export default {
        data() {
            return {
                wallet: {},
                token: '',
                show_update_form: false,
            }
        },
        methods: {
            async getData() {
                axios
                    .get(
                        axiosUrl + '/api',
                        {
                            headers: {
                                'Authorization': 'Bearer ' + this.token
                            }
                        }
                    )
                    .catch ((er) => {
                        if (er.response.status == 401) {
                            this.$router.push({name: 'auth'})
                        }
                    })
                    .then((response) => {
                        if (response) {
                            this.wallet = response.data
                        }
                    });
                
            },
            async createPurchase(e) {
                let title = e.target.elements.title.value
                let spend = e.target.elements.spend.value
                axios
                    .post(
                        axiosUrl + '/api' + '/purchase/',
                        {
                            title: title,
                            amount: spend
                        },
                        {
                            headers: {
                                'Authorization': 'Bearer ' + this.token
                            }
                        }
                    )
                    .then((response) => {
                        this.getData()
                    }) 

            },
            async updateWallet(e) {
                let money = e.target.elements.money.value
                let date = e.target.elements.date.value
                axios
                    .put(
                        axiosUrl + '/api/',
                        {
                            left_money: money,
                            left_date: date
                        },
                        {
                            headers: {
                                'Authorization': 'Bearer ' + this.token
                            }
                        }
                    )
                    .then((response) => {
                        this.getData()
                    }) 
            },
            toggleFormBtn() {
                let updateForm = document.getElementById('updateForm')
                let createForm = document.getElementById('createForm')
                

                if (this.show_update_form) {
                    updateForm.style.display = 'none';
                    createForm.style.display = 'flex';
                    this.show_update_form = false
                } else {
                    updateForm.style.display = 'flex';
                    createForm.style.display = 'none';
                    this.show_update_form = true
                }
            
                
            }
        },
        created() {
            this.token = this.$cookies.get('access_token')
            this.getData()
        }
    }


    

</script>

<style scoped>

    .wallet__daily-available {
        margin-top: 10px;
    }
    .wallet-content { 
        margin-top: 15px;
    }

    .wallet__spends {
        width: 350px;
        border: 10px inset #f5a623;
        padding: 10px;
    }

    .wallet__form {
        margin-top: 10px;
        display: flex;
        flex-direction: column;
    }

    .wallet__form > label {
        margin-top: 10px;
        font-size: 20px;
    }

    .wallet__form__input {
        border: 3px solid #f5a623;
        padding: 5px;
    }

    .wallet__form__button {
        background-color: #f5a623;
        outline: none;
        margin-top: 15px;
        font-size: 18px;
        padding: 5px;
    }

    .wallet__spends__list {
        overflow-y: scroll;
        max-height: 480px;
    }

    .wallet__spends__item:not(:last-of-type) {
        margin-top: 5px;
        border-bottom: 1px solid #f5a623;
    }

    #updateForm {
        display: none;
    }
</style>