import { niceFetch, niceSend } from './utils';
import singleton from './singleton.js';

function searchMgr() {
  let search_id;
  let click_number = 0;
  const tasks = {};

  const resetClickNumber = () => { click_number = 0; };
  const incrementClickNumber = () => { click_number++; };
  const setSearchId = id => { search_id = id; };


  const getArticles = async searchedText => {
    resetClickNumber();
    // const d = {
    //   test: {list: [{id: 1, name: "Télévision", description: "Une télé"}], search_id: 7, l: [1, 2, 3, 4, 8]},
    //   test2: {list: [{id: 2, name: "Phone", description: "Un téléphone"}], search_id: 18, l: [45, 78, 999]}
    // }
    // const data = d[searchedText] || d.test;
    // setSearchId(data.search_id);

    // for (const key in tasks) {
    //   const task = tasks[key];
    //   if (typeof task === "function") { task(data.l)}
    // }

    // return data.list;
		try {
			const data = await niceFetch(`/moteur/api/get-articles?search=${searchedText}`);
			console.log("data fetched: ", data); // data format: {list: [{id, name, description}], search_id}
      setSearchId(data.search_id);
      const articlesList = data.list;
      // const articlesList = data.list.map(a => a.id);
      for (const key in tasks) {
        const task = tasks[key];
        if (typeof task === "function") { task(articlesList); }
      }
		} catch (err) {
			console.error(err);
		}
	};

  const saveClick = async (article_name) => {
    if (!search_id) { return; }
    incrementClickNumber();
    if (click_number > 3) { return; }
    // console.log(`saveClick will use search_id ${search_id}, article_name ${article_name} and click_number ${click_number}`);
		try {
			const data = await niceSend(`/moteur/api/save-click`, "POST", {search_id, article_name, click_number});
			console.log("data: ", data);
		} catch (error) {
			console.error(error);
		}
	};

  const registerTaskOnArticlesUpadate = (key, f) => { tasks[key] = f; };

  return {
    getArticles,
    saveClick,
    registerTaskOnArticlesUpadate
  };
}

let alreadyCreated = 0;
const create = () => {
  if (!alreadyCreated) {
    singleton.register("searchMgr", searchMgr());
    alreadyCreated = 1;
  }
};

export default function getSearchMgr() {
  create();
  return singleton.get("searchMgr");
}
