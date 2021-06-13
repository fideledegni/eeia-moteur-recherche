import React from "react";
import axios from "axios"; // Use axios for requests. Doc: https://www.npmjs.com/package/axios


// const inProd=  process.env.inProd;
export default class App extends React.Component {
  render() {

    let searchedText = "";

    async function getArticles(text) { // TODO: in progress...
      try {
        const response = await axios.get(`/moteur/api/get-articles/${text}`);
        // console.log(response);
        if (response.status === 200) {
          const data = response.data;
          console.log("data: ", data);
        }
      } catch (error) {
        console.error(error);
      }
    }

    async function saveClicks(text) { // TODO: in progress...
      try {
        const clicks = ["télévision", "téléphone"].join(",");
        const response = await axios.get(`/moteur/api/save-clicks/${text}/${clicks}`);
        // console.log(response);
        if (response.status === 200) {
          const data = response.data;
          console.log("data: ", data);
        }
      } catch (error) {
        console.error(error);
      }
    }

    const onKeyUp = e => {
      const keyCode = e.keyCode;
      if (keyCode === 13) {
        const text = e.target.value;
        console.log(`Will search for entered value: ${text}`);
        searchedText = text;
        getArticles(text);
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
            <input className="form-control mr-sm-2" type="search" onKeyUp={e => onKeyUp(e)} autoFocus placeholder="Qu'est-ce qui vous plairait aujourd'hui ?" aria-label="Rechercher"/>
          <hr className="my-4"/>

          <div>
            Artices here if any...
          </div>
          <img src="static/img/favicon.png"/>
        </div>
      </div>
    </div>;
  }
}
