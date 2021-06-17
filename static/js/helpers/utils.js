import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// boolean to check the environnement mode: DEV or PROD ?
export const DEV = !process.env.NODE_ENV || process.env.NODE_ENV === 'development';

// Override the default console.log function
export const log = (...data) => {
	if(DEV) {
		console.log('[EEIA]', ...data);
	}
};


// DELETE this after !!! NOT NEEDED IN THE PROJECT
// USED ONY FOR STYLING PURPOSES WHEN NO DATA IS AVAILABLE
// DUPLICATE THE BEHAVIOR OF range IN PYTHON
export const range = (start, stop) => {
	if(!Number.isInteger(stop) || !Number.isInteger(start)) { throw new Error("Expected integer"); }
	return [...Array(stop - start).keys()].map(i => i + start);
};

// Helper function for GET requests
// This is useful and get rid of the try-catch blocks !!!
export const niceFetch = async (url, options) => {
	const timeout = (options && options.timeout) || 5000;

	try {
		const res = await axios.get(url, { timeout, ...options });
		if(res.statusText !== "OK") {
			throw new Error(res.status + ' Error: ' + res.statusText);
		}
		return res.data;
	} catch(err) {
		console.error(err);
		throw new Error('Could not GET from: ' + url);
	}
};

// Helper function for POST, PATCH, DELETE.... requests
export const niceSend = async (url, method, data) => {
	const withData = data !== undefined;
	const timeout = 5000;
	const headers = withData ? { 'Content-Type': 'application/json' } : {};
	
	try {
		const res = await axios({ url, method, headers, data, timeout });
		if(res.statusText !== "OK") {
			throw new Error(res.status + ' Error: ' + res.statusText);
		}
		return res.data;
	} catch (err) {
		console.error(err);
		throw new Error('Could not ' + method + ' to ' + url);
	}
};
