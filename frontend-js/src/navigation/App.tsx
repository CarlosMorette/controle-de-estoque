import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { pages, homePage, notFoundPage } from './Routes'
import './reset.css'

export default function App() {
  return (
    <Router>
        <Switch>
          <Route exact component={homePage.component} path="/"/>
          {pages.map((p, i) => <Route key={i} exact path={p.path} component={p.component} />)}
          <Route component={notFoundPage.component}/>
        </Switch>
    </Router>
  );
}