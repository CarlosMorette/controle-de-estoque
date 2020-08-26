import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { routesPages } from './Routes'

export default function App() {
  return (
    <Router>
      <Switch>
        {routesPages.map((p, i) => <Route key={i} path={p.path} component={p.component} />)}
      </Switch>
    </Router>
  );
}
