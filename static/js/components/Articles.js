import React from 'react';
import { range } from '../utils';
import Article from "./Article";

const Articles = () => {

  return (
    <div className="container">
      <div className="d-flex p-3 justify-content-evenly flex-wrap">
        {range(1, 29).map(i => (
          <Article key={i} name={`Article n° ${i}`}/>
        ))}
      </div>
    </div>
  );
};

export default Articles;
