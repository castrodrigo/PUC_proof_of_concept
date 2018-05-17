import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import ReduxPromise from 'redux-promise';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import HomePage from './pages/home-page/';
import CoursePage from './pages/course-page';
import reducers from './reducers';

const createStoreWithMiddleware = applyMiddleware(ReduxPromise)(createStore);

const AppRouter = () => (
  <main>
    <Switch>
      <Route exact path='/' component={HomePage}/>
      <Route path='/cursos' component={CoursePage}/>
    </Switch>
  </main>
)

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
    <BrowserRouter>
      <AppRouter />
    </BrowserRouter>
  </Provider>
  , document.querySelector('.container'));
