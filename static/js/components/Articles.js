import React, { useState } from 'react';
import { range } from '../helpers/utils';
import Article from "./Article";
import getSearchMgr from '../helpers/search-mgr.js';

const Articles = () => {
  const [articlesList, setArticlesList] = useState(range(1, 29));
  const searchMgr = getSearchMgr();
  searchMgr.registerTaskOnArticlesUpadate("setArticlesList", setArticlesList);

  return (
    <div className="container">
      <div className="d-flex p-3 justify-content-evenly flex-wrap">
        {articlesList.map(i => (
          <Article key={i} name={`Article n° ${i}`}/>
        ))}
      </div>
    </div>
  );
};

export default Articles;
