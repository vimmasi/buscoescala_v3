import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { supabase } from "@/lib/supabaseClient";

let localUser;

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/SignUpView.vue"),
    },
    {
      path: "/bloqueado",
      name: "bloqueado",
      component: () => import("../views/BloqueadoView.vue"),
    },
  ],
});

//  Lógica para proteger a rota sem autenticação
router.beforeEach(async (to, from, next) => {
  const {
    data: { session },
  } = await supabase.auth.getSession();
  localUser = session?.user;

  if (to.matched.some((record) => record.meta.requiresAuth) && !localUser) {
    next({ name: "bloqueado" });
  } else if (to.name === "login" && localUser) {
    next({ name: "home" });
  } else {
    next();
  }
});

export default router;
