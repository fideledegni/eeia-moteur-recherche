import React from 'react';

const DownloadBtn = () => {
  const apiLink = "/moteur/api/get_csv_searches_list";
  return <div>
    <a className="btn btn-link pull-right" style={{color: "#125d98"}} href={apiLink} target="_blank" rel="noopener noreferrer">
      Télécharger les recherches
    </a>
  </div>;
};

export default DownloadBtn;
