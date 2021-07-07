import React from 'react';
import getSearchMgr from '../helpers/search-mgr.js';

const Article = ({ props }) => {
  const searchMgr = getSearchMgr();

  const openModal  = () => { searchMgr.saveClick(props.name); };

  const image_name = props.image_name || "favicon.png"
  const modalId = `articleModal-${props.id}`

  return <React.Fragment>
    <div className="card m-2 article-card" data-toggle="modal" data-target={`#${modalId}`} onClick={openModal}>
      <img src={`static/img/${image_name}`}/>
      <div className="card-body">
        <p className="card-text text-center text-uppercase">{props.name}</p>
      </div>
    </div>

    <div className="modal fade" id={modalId} tabIndex="-1" role="dialog">
      <div className="modal-dialog modal-dialog-centered modal-lg">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">{props.name}</h5>
            <button type="button" className="btn-close" data-dismiss="modal" />
          </div>
          <div className="modal-body text-center">
            <img src={`static/img/${image_name}`}/>
            <br/><br/>
            <p>{props.description || "Pas d'informations supplémentaires pour cet article"}</p>
          </div>
          <div className="modal-footer">
            <button type="button" className="btn btn-secondary" data-dismiss="modal">Fermer</button>
            <button type="button" className="btn btn-primary">Acheter</button>
          </div>
        </div>
      </div>
    </div>
  </React.Fragment>;
};

export default Article;
