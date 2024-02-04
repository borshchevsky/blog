import { createRouter, createWebHistory } from "vue-router";
import HomePage from '@/views/HomePage.vue';
import SignupForm from '@/views/SignUpForm.vue';
import SigninForm from '@/views/SignInForm.vue';
import BlogPage from "@/views/BlogPage.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
    },
    {
        path: '/signup',
        name: 'Signup',
        component: SignupForm
    },
    {
        path: '/signin',
        name: 'Signin',
        component: SigninForm
    },
    {
        path: '/:id',
        name: 'Blog',
        component: BlogPage
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})


export default router