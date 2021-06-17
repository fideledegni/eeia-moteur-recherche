import React, { useState } from 'react';
import getSearchMgr from '../helpers/search-mgr.js';

const SearchBar = () => {
	const [searchedText, setSearchedText] = useState("");
	const searchMgr = getSearchMgr();

	const onChange = (e) => setSearchedText(e.target.value);

	const search = async () => {
		console.log(`Will search for entered value: ${searchedText}`);
		const articles_list = await searchMgr.getArticles(searchedText);
		console.log("Got articles_list: ", articles_list);
	};

	const onKeyUp = (e) => {
		if (e.keyCode === 13) { search(); }
	};

	return (
		<div>
			<h1 className="mt-3 display-6">Rechercher :</h1>
			<div className="input-group mb-3 w-50">
				<input className="form-control mr-sm-2 bg-outline" type="search" onKeyUp={onKeyUp} value={searchedText}
					placeholder="Qu'est-ce qui vous plairait aujourd'hui ?" aria-label="Rechercher" onChange={onChange} />
				<button className="btn btn-outline-primary" type="button" onClick={search}>
					<i className="fa fa-search"></i>
				</button>
			</div>
			<hr className="my-4" />
		</div>
	);
};

export default SearchBar;
