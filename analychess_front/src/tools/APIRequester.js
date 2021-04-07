import axios from "axios";

export default class ApiRequester {
    
    static #instance = null;
    #BASE_URL = 'http://127.0.0.1:8000/api/';
    #ROUTE = null;
    #URL_PARAM = null;
    #PARAM = null;

    constructor()
    {

    }

    static getInstance()
    {
        if (ApiRequester.instance == null)
            ApiRequester.instance = new ApiRequester();
        return ApiRequester.instance;
    }

    setRoute(route)
    {
        this.#ROUTE = route;
        return this;
    }

    setURLParam(params)
    {
        this.#URL_PARAM = params;
        return this;
    }

    setParam(params)
    {
        this.#PARAM = params;
        return this;
    }

    get(){

    }

    async post(){
        try{
            const response = await axios.post(this.#BASE_URL + this.#ROUTE, this.#PARAM);
            console.log(response.data);
        }
        catch(errors){
            console.error(errors);
        }
    }
    
}
