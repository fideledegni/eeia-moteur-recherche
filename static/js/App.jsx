import React from "react";
import Navbar from "./components/Navbar";
import SearchBar from "./components/SearchBar";
import Articles from "./components/Articles";
import DownloadBtn from "./components/DownloadBtn";

const App = () => {
	return (
		<div className="app">
			<Navbar />

			<div className="container">
				<DownloadBtn />
				
				<div className="jumbotron">
					<SearchBar />
					<Articles />
				</div>

			</div>
		</div>
	);
};

export default App;
