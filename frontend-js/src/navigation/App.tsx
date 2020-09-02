import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { routesPages, notFound } from './Routes'
import './../css/reset.css'


export default function App() {
  return (
    <Router>
        <Switch>
          {routesPages.map((p, i) => <Route key={i} exact path={p.path} component={p.component} />)}
          <Route component={notFound.component}/>
        </Switch>
    </Router>
  );
}