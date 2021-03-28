import React, {useState, useEffect} from 'react'
import Logo from './CitationScholar.png'
import Button from 'react-bootstrap/Button';
import './Search.css'

const Search = () => {
    const [input, setInput] = useState('')

    const [arxiv, setArxiv] = useState(false)
    const [google, setGoogle] = useState(false)
    const[acm, setAcm] = useState(false)
    const[ieee, setIeee] = useState(false)

    const Submit = (e) => {
        console.log(e.key === "Enter")
        if (e.key === "Enter" && input !== ''){
            
        }
    }

    return(
        <div>
            <img src={Logo} id="logo"/>
            <input id="input" placeholder="Input link to a starting topic"/>
            <div id="selection">
                <button class={arxiv ? "button2" : "button"} onClick={() => setArxiv(!arxiv)} >arxiv</button>
                <button class={google ? "button2" : "button"} onClick={() => setGoogle(!google)}>google scholar</button>
                <button class={acm ? "button2" : "button"} onClick={() => setAcm(!acm)}>acm</button>
                <button class={ieee ? "button2" : "button"} onClick={() => setIeee(!ieee)}>ieee</button>
            </div>
        </div>
    )
}

export default Search