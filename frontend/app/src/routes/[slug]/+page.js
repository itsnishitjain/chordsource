export const load = async ({ fetch, params }) => {
	let res = await fetch('http://0.0.0.0:8080/status', {
		method: 'GET'
	});

	res = await res.json();

	return {
		res: res,
		slug: params.slug
	};
};
