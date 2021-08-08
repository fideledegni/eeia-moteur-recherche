import React from 'react';

const DownloadBtn = () => {
  const searchesLink = "/moteur/api/get_csv_searches_list";
  const articlesLink = "/moteur/api/get_csv_articles_list";
  const bgStyle = {backgroundColor: "#dbe2ef"}
  const itemStyle = {color: "#125d98"};

  return <div className="dropdown">
    <button className="btn dropdown-toggle pull-right" style={bgStyle} type="button" id="downButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      Téléchargements
    </button>
    <div className="dropdown-menu" aria-labelledby="downButton">
      <a className="dropdown-item" style={itemStyle} href={searchesLink} target="_blank" rel="noopener noreferrer">
        Télécharger les recherches
      </a>
      <a className="dropdown-item" style={itemStyle} href={articlesLink} target="_blank" rel="noopener noreferrer">
        Télécharger les articles
      </a>
    </div>
  </div>;
};

export default DownloadBtn;
