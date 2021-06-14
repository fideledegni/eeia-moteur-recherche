import React from "react";
import axios from "axios";

export default class App extends React.Component {
  render() {

    async function getArticles(text) {
      // TODO: use text value
      // Use axios for requests. Doc: https://www.npmjs.com/package/axios
      try {
        const response = await axios.get('/api/get-articles');
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    }

    const onKeyUp = e => {
      const keyCode = e.keyCode;
      if (keyCode === 13) {
        console.log("Will search...");
        const text = e.target.value;
        console.log("Entered value: ", text);
        // getArticles(text);
      }
    };

    return <div>
      <nav className="navbar sticky-top navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <a className="navbar-brand" href="/">Moteur de recherche EEIA</a>
        </div>
      </nav>

      <div className="container">
        <div className="jumbotron">
          <h1 className="display-6">Rechercher :</h1>
            <input className="form-control mr-sm-2" type="search" onKeyUp={e => onKeyUp(e)} autoFocus placeholder="Qu'est-ce qui vous plairaît aujourd'hui ?" aria-label="Rechercher"/>
          <hr className="my-4"/>

          <div>
            Artices here if any....
          </div>
          <img src="static/img/favicon.png"/>
        </div>
      </div>
    </div>;
  }
}
