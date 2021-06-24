import React, { useState } from 'react';
import getSearchMgr from '../helpers/search-mgr.js';

const Article = ({ props }) => {
  const [show, setShow] = useState(false);
  const searchMgr = getSearchMgr();

  const openModal  = () => { searchMgr.saveClick(props.name); setShow(true); };
  const closeModal = () => setShow(false);

  return (
    <React.Fragment>
      <div className="card m-2 article-card" onClick={openModal}>
        <svg className="card-img-top">
          <rect width="100%" height="100%" style={{ fill: "#ccc", strokeWidth: 3, stroke: "#ccc" }} />
        </svg>
        <div className="card-body">
          <p className="card-text text-center text-uppercase">{props.name}</p>
        </div>
      </div>

      <div className={"modal fade" + (show ? " show" : "")} style={{display: show ? "block" : "none"}}>
        <div className="modal-dialog modal-dialog-centered">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">{props.name}</h5>
              <button type="button" className="btn-close" onClick={closeModal} />
            </div>
            <div className="modal-body">
              <p>{props.description || "Description of article goes here."}</p>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" onClick={closeModal}>Close</button>
              <button type="button" className="btn btn-primary">Buy</button>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Article;
