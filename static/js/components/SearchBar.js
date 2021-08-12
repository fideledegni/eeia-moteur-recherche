import React, { useState } from 'react';
import getSearchMgr from '../helpers/search-mgr.js';

const SearchBar = () => {
	const [searchedText, setSearchedText] = useState("");
	const [modelNum, setModelNum] = useState("1");
	const searchMgr = getSearchMgr();

	const onChange = (e) => setSearchedText(e.target.value);
	const onModelChange = (e) => setModelNum(e.target.value);

	const search = () => {
		console.log(`Will search for entered value: ${searchedText}. Using modelNum: ${modelNum}`);
		searchMgr.getArticles(searchedText, modelNum);
	};

	const onKeyUp = (e) => {
		if (e.keyCode === 13) { search(); }
	};

	const t1 = "\u2022 Le modèle 1 fait une recherche basique en cherchant le mot recherché dans les noms des articles.\n\n";
	const t2 = "\u2022 Le modèle 2 est un peu plus malin et utilise la distance de Levenshtein pour trouver les articles même si on se trompe un peu dans l'orthographe.\n\n";
	const t3 = "\u2022 Le modèle 3 'apprend' du comportement des utilisateurs pour proposer des résultats encore plus pertinents.";
	const modelTitle = t1 + t2 + t3

	return (
		<div>
			<h1 className="mt-3 display-6">Rechercher :</h1>
			<div className="row">
				<div className="col-md-10">
					<div className="input-group mb-3 w-50">
						<input className="form-control mr-sm-2 bg-outline" type="search" onKeyUp={onKeyUp} value={searchedText}
							placeholder="Qu'est-ce qui vous plairait aujourd'hui ?" aria-label="Rechercher" onChange={onChange} autoFocus />
						<button className="btn btn-outline-primary" type="button" onClick={search}>
							<i className="fa fa-search"></i>
						</button>
					</div>
				</div>
				<div className="col-md-2">
					<select id="modelSelect" defaultValue="1" className="form-select form-select-sm" aria-label="Default select example" onChange={onModelChange} title={modelTitle}>
						<option value="1">Modèle 1</option>
						<option value="2">Modèle 2</option>
						<option value="3">Modèle 3</option>
					</select>
				</div>
			</div>				
			<hr className="my-4" />
		</div>
	);
};

export default SearchBar;
