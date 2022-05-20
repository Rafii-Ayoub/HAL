import Middle from './Middle'
import RightBar from './RightBar'
import React, { useState, useEffect } from 'react'
import { TagCloud } from 'react-tagcloud'


const ListicStat = () => {

const [words, setWords] = useState([]);

useEffect(() => {
    fetch('http://localhost:5000/listic')
      .then((res) => res.json())
      .then((data) => {
        setWords(data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  
  const removeduplicates = (words) => [...new Set(
    words.map(el => JSON.stringify(el))
  )].map(e => JSON.parse(e));
  

  

    return (
        <div className=" bg-white h-full " > 

            <div className="flex  ml-3 mt-6 space-x-2  mr-4 ">
                <div className=" bg-white  ml-2   shadow-sm w-full h-screen   ">
                  <br></br>
                 <span></span> <h2 className='text-xl  font-semibold text-blue-600 ' >Nombre de Publications : 6,5K</h2>
                 <br></br>
                 <span></span> <h2 className='text-xl  font-semibold text-blue-600 ' >Nombre d'auteurs : 188</h2>
                 <br></br>
                 <h2 className='text-xl  font-semibold text-blue-600 ' >Nuage des sujets:</h2>
                 <br></br>
                <TagCloud
                  minSize={1}
                  maxSize={80}  
                  tags={removeduplicates(words)}
                  />
        
        </div>
    
            </div>
        </div>
    )
}


export default ListicStat
