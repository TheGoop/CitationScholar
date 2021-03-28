import React, {useState, useEffect} from 'react'
import Logo from './CitationScholar.png'
import Button from 'react-bootstrap/Button';
import axios from 'axios'
import './Search.css'
import './loading.css'

import miserables from './miserables.json'
import { ForceGraph } from './Graph'

const Search = () => {
    const [input, setInput] = useState('')

    const [arxiv, setArxiv] = useState(false)
    const [google, setGoogle] = useState(false)
    const[acm, setAcm] = useState(false)
    const[ieee, setIeee] = useState(false)

    const[loading, setLoading] = useState("start")

    const[sources, setSources] = useState(null)

    const Submit = (e) => {
        console.log(e.key === "Enter")
        if (e.key === "Enter" && input !== ''){
            setLoading("wait")
        }
    }

    const updateInput = (e) => {
        setInput(e.target.value);
    }

    useEffect(() => {
        let items = []
        if (arxiv){
            items.push("arxiv")
        }
        if (google){
            items.push("google_scholar")
        }
        if (acm){
            items.push("acm")
        }
        if (ieee){
            items.push("ieee")
        }

        let NEWGET = {
            input: input,
            valid: items,
        }

        async function makePost() {
            axios
                .get(`f`, NEWGET)
                .then(function(response) {
                    setSources(response.data)
                    setLoading("finished")
                })
        }

        if (loading === "wait"){
            // FETCH LINK HERE
            console.log(NEWGET)
            makePost()
            setTimeout(function(){ setLoading("finished"); }, 2000);

        }
    }, [loading])

    if (loading === "start"){
        return(
            <div>
                <img src={Logo} id="logo"/>
                <input id="input" placeholder="Input link to a starting topic" onKeyPress={Submit} onChange={updateInput}/>
                <div id="selection">
                    <button class={arxiv ? "button2" : "button"} onClick={() => setArxiv(!arxiv)} >arxiv</button>
                    <button class={google ? "button2" : "button"} onClick={() => setGoogle(!google)}>google scholar</button>
                    <button class={acm ? "button2" : "button"} onClick={() => setAcm(!acm)}>acm</button>
                    <button class={ieee ? "button2" : "button"} onClick={() => setIeee(!ieee)}>ieee</button>
                </div>
            </div>
        )
    }
    else if (loading === "wait"){
        return(
        <div>
            <img src={Logo} id="logo"/>
            <div id="loading">
            <div class="lds-default"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
            </div>
        </div>
        )
    }
    else if (loading === "finished"){
        return(
            // USE SOURCES HERE
            <div>
                <ForceGraph data={miserables}/>
            </div>
        )
    }
}

export default Search