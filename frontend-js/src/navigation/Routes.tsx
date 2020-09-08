import { Route } from './../constants/Interfaces'
import Home from './../screens/Home'
import NotFound from './../screens/NotFound'

const routesPages: Route[] = [
    {
        name: "Home",
        path: "/",
        component: Home
    }
]

const notFound = {
    name: "NotFound",
    component: NotFound
}

export { routesPages, notFound }