import React, { useState, useEffect } from 'react';
// import { range } from '../helpers/utils';
import Article from "./Article";
import getSearchMgr from '../helpers/search-mgr.js';

const Articles = () => {
  const [articlesList, setArticlesList] = useState([]);
  const searchMgr = getSearchMgr();
  searchMgr.registerTaskOnArticlesUpadate("setArticlesList", setArticlesList);

  useEffect(() => {
    const fetchArticles = async () => { await searchMgr.getArticles(''); };
    fetchArticles();
  }, []);

  return (
    <div className="container">
      <div className="d-flex p-3 justify-content-evenly flex-wrap">
        {articlesList.map(article => (
          <Article key={article.id} props={article} />
        ))}
      </div>
    </div>
  );
};

export default Articles;
