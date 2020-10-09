import { Route } from './../constants/Interfaces'
import Home from '../screens/home/home'
import NotFound from '../screens/notfound/notFound'

const pages: Route[] = [
    
]

const homePage = {
    name: "Home",
    path: "/",
    component: Home
}

const notFoundPage = {
    name: "NotFound",
    component: NotFound
}

export { pages, homePage, notFoundPage }