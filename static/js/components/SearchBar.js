import React, { useState } from 'react';
import { niceFetch } from '../utils';

const SearchBar = () => {
	const [searchedText, setSearchedText] = useState("");

	const onChange = (e) => setSearchedText(e.target.value);

	const onKeyUp = (e) => {
		if (e.keyCode === 13) {
			console.log(`Will search for entered value: ${searchedText}`);
			getArticles(searchedText);
		}
	};

	const getArticles = async () => {
		try {
			const data = await niceFetch(`/moteur/api/get-articles/${searchedText}`);
			console.log("data fetched: ", data);
		} catch (err) {
			console.error(err)
		}
	};

	const saveClicks = async () => {
		try {
			const data = await niceFetch(`/moteur/api/get-articles/${searchedText}`);
			console.log("data: ", data);
		} catch (error) {
			console.error(error);
		}
	};

	return (
		<div>
			<h1 className="mt-3 display-6">Rechercher :</h1>
			<div className="input-group mb-3 w-50">
				<input className="form-control mr-sm-2 bg-outline" type="search" onKeyUp={onKeyUp} value={searchedText}
					placeholder="Qu'est-ce qui vous plairait aujourd'hui ?" aria-label="Rechercher" onChange={onChange} />
				<button className="btn btn-outline-primary" type="button">
					<i className="fa fa-search"></i>
				</button>
			</div>
			<hr className="my-4" />
		</div>
	);
};

export default SearchBar;
