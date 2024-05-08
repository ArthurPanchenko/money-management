<template>
    <div class="auth-bgc">
        <div class="auth-container">
            <div class="auth">
                <p class="response">
                    {{ errors }}
                </p>
                <input type="checkbox" id="chk" aria-hidden="true">
                
                <div class="auth__signup">
                    <form @submit.prevent="signup">
                        <label class="signup__label" for="chk" area-hidden="true">Sign Up</label>
                        <input type="text" name="username" placeholder="Username" required="true">
                        <input type="email" name="email" placeholder="Email" required="">
                        <input type="password" name="password" placeholder="Password" required="true">
                        <button>Sign Up</button>
                    </form>
                </div>
                <div class="auth__login">
                    <form @submit.prevent="login">
                        <label for="chk" aria-hidden="true">Login</label>
                        <input type="text" name="username" placeholder="Username" required="">
                        <input type="password" name="password" placeholder="Password" required="">
                        <button>Login</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
    
</template>

<script>
    import { axiosUrl } from '@/main';
    import router from '@/router';
    import axios from 'axios';
    
 
    export default {
        name: 'Auth',
        data() {
            return {
                errors: '',
                response: ''
            }
        },
        methods: {
            async signup(e) {
                let username = e.target.elements.username.value
                let email = e.target.elements.email.value
                let password = e.target.elements.password.value
                
                axios
                    .post(
                        axiosUrl + '/auth/users/',
                        {
                            email: email,
                            username: username,
                            password: password
                        }
                    )
                    .catch((er) => {
                        this.errors = er
                    })
                    .then((response) => {
                        response = 'Account created'
                    });
                    
            },
            async login(e) {
                let username = e.target.elements.username.value
                let password = e.target.elements.password.value

                axios
                    .post(
                        axiosUrl + '/auth/token/',
                        {
                            username: username,
                            password: password
                        }
                    )
                    .catch((er) => {
                        this.errors = er
                    })
                    .then((response) => {
                        this.$cookies.set(
                            'access_token',
                            response.data.access,
                            3 * 24 * 60 * 60 * 1000
                        )
                        router.push({name: 'home'})
                    });
            }
        }
    }

</script>

<style scoped>

    .auth-bgc {
        position: fixed;
        background-color: #f5a623;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .response {
        text-align: center;
        color: red
    }
    .auth {
        width: 350px;
        height: 500px;
        margin: 13rem auto;
        overflow: hidden;
        border-radius: 10px;
        background-color: white;
        box-shadow: 5px 20px 50px #000;
    }

    #chk{
	    display: none;
    }

    .auth__signup {
        position: relative;
        width: 100%;
        height: 100%;
    }

    label {
        color: #f5a623;
        font-size: 2.3rem;
        justify-content: center;
        display: flex;
        margin: 60px;
        font-weight: bold;
        cursor: pointer;
        transition: .5s ease-in-out
    }

    input {
        width: 60%;
        height: 35px;
        background: #e0dede;
        display: flex;
        justify-content: center;
        margin: 20px auto;
        padding: 10px;
        border: none;
        outline: none;
        border-radius: 5px;
    }
    button{
        width: 60%;
        height: 40px;
        margin: 10px auto;
        justify-content: center;
        display: block;
        color: #fff;
        background: #fa9c05;
        font-size: 1em;
        font-weight: bold;
        margin-top: 20px;
        outline: none;
        border: none;
        border-radius: 5px;
        transition: .2s ease-in;
        cursor: pointer;
    }
    button:hover{
        background: #f5b44d;
    }
    
    .auth__login {
        height: 460px;
        background: #eee;
        border-radius: 60% / 10%;
        transform: translateY(-195px);
        transition: .8s ease-in-out;
    }
    .auth__login label{
        color: black;
        transform: scale(.6);
    }

    #chk:checked ~ .auth__login{
        transform: translateY(-500px);
    }
    #chk:checked ~ .auth__login label{
        transform: scale(1);	
    }
    #chk:checked ~ .auth__signup label{
        transform: scale(.6);
    }
</style>