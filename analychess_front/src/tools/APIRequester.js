import axios from 'axios';
import router from '../router/router'

/**
 * Class for AJAX request to the API
 * 
 * @author Edouard Goffinet
 */
export default class ApiRequester {
    

    static #instance = null;
    #BASE_URL = 'https://analychess.srvz-webapp.he-arc.ch/api/';

    #REFRESH_URL = 'login/refresh'
    #route = null;
    #params = null;


    /**
     * Default constructor for singleton
     * 
     * @author Edouard Goffinet
     */
    constructor()
    {
        // Do nothing
    }

    /**
     * Getter for the singleton instance
     * 
     * @author Edouard Goffinet
     * @returns APIRequester's instance
     */
    static getInstance()
    {
        if (ApiRequester.instance == null)
            ApiRequester.instance = new ApiRequester();
        return ApiRequester.instance;
    }

    /**
     * Setter for the route of the request
     * 
     * @author Edouard Goffinet
     * @param {string} route 
     * @returns the APIRequester's instance
     */
    setRoute(route)
    {
        this.#route = route;
        return this;
    }

    /**
     * Setter for the params(JSON) of the request
     * 
     * @author Edouard Goffinet
     * @param {json} params 
     * @returns the APIRequester's instance
     */
    setParam(params)
    {
        this.#params = params;
        return this;
    }

    /**
     * Send a GET request
     * 
     * @author Edouard Goffinet
     * @returns Data of the request's response
     */
    async get(){
        try{
            const response = await axios.get(this.#BASE_URL + this.#route, {headers: {Authorization: `Bearer ${localStorage.getItem('access')}`}});
            return response.data;
        }
        catch(error){
            return await this.handleError(error, 'GET')
        }
    }

    /**
     * Send a POST request
     * 
     * @author Edouard Goffinet
     * @returns Data of the request's response
     */
    async post(){
        try{
            const response = await axios.post(this.#BASE_URL + this.#route, this.#params, {headers: {Authorization: `Bearer ${localStorage.getItem('access')}`}});
            return response.data;
        }
        catch(error){
            return await this.handleError(error, 'POST')
        }
    }

    async put(){
        try{
            const response = await axios.patch(this.#BASE_URL + this.#route, this.#params, {headers: {Authorization: `Bearer ${localStorage.getItem('access')}`}});
            return response.data;
        }
        catch(error){
            return await this.handleError(error, 'PUT')
        }
    }

    async delete(){
        try{
            const response = await axios.delete(this.#BASE_URL + this.#route, {headers: {Authorization: `Bearer ${localStorage.getItem('access')}`}});
            return response.data;
        }
        catch(error){
            return await this.handleError(error, 'DELETE')
        }
    }

    /**
     * Specified POST request for login
     * 
     * @author Edouard Goffinet
     * @param {string} username 
     * @param {string} password 
     */
    async login(username, password)
    {
        this.setRoute('login')
        this.setParam({'username': username, 'password': password})
        let data = await this.post();
        localStorage.setItem('access', data.access);
        localStorage.setItem('refresh', data.refresh);
    }

    /**
     * Logout
     * 
     * @author Edouard Goffinet
     */
    async logout()
    {
        this.setRoute('logout');
        try{
            this.setParam({'refresh': localStorage.getItem('refresh')});
            this.post();
        }
        catch(error)
        {
            void(0)
        }
        localStorage.removeItem('access');
    }

    /**
     * Private function to handle errors
     * 
     * @author Edouard Goffinet
     * @param {*} error 
     * @param {string} verb
     * @returns 
     */
    async handleError(error, verb)
    {
        // Authentification error with token not valid
        if (error.response.status == 401 && error.response.data.code == 'token_not_valid')
        {
            // Try to refresh the token
            if (await this.refresh())
            {
                switch (verb){
                    case 'GET':
                        return await this.get();
                    case 'POST':
                        return await this.post();
                    case 'PUT':
                        return await this.put();
                    case 'DELETE':
                        return await this.delete();
                }
            }
            else
            {
                localStorage.removeItem('access');
                router.push({name: 'Login'});
            }
        }
        // Others errors
        // TODO : implement others errors gestion (400, 404, 500)...
        else
        {
            console.log(error.response);
            console.error(error);
        }
    }

    /**
     * Private func to refresh access token
     * 
     * @author Edouard Goffinet
     * @returns true if token successfully refresh, false otherwise
     */
    async refresh()
    {
        console.log('Refreshing');
        try
        {
            const reponse = await axios.post(this.#BASE_URL + this.#REFRESH_URL, {'refresh': localStorage.getItem('refresh')}, {headers: {Authorization: `Bearer ${localStorage.getItem('access')}`}})
            localStorage.setItem('access', reponse.data.access);
            // access token successfully updated
            return true
        }
        catch(error)
        {   
             // Authentification error with refresh token invalid or other errors
            return false   
        }
    }
    
}
