import Middle from './Middle'
import RightBar from './RightBar'
import React, { useState, useEffect } from 'react'
import { useMoralis } from "react-moralis";

import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Image from 'next/image';
import Link from "next/link";
import next from 'next';
import Router from 'next/router';

const ContainerAut = () => {

const [auteurs, setAuteurs] = useState([]);
function sendAuteur(name){
    Router.push({
        pathname:"/auteur",
        query:{
            name,
        }
    })
}
useEffect(() => {
    fetch('http://localhost:5000/publications_info')
      .then((res) => res.json())
      .then((data) => {
        setAuteurs(data);
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
        <Grid container spacing={2}>
            {removeduplicates(auteurs).map( auteur =>(
                <Grid item key = {auteur.id}  md={4} lg={4}>
                    <Card sx={{ maxWidth: 250 }}>
            <CardMedia
                    component="img"
                    height="140"
                    image='/auteur.jpg'
                    alt="green iguana"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                    {auteur.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                    {auteur.institution}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="medium" onClick={() => sendAuteur(auteur.name,auteur.id)} >
                OPEN</Button>
                
                </CardActions>
                </Card>

                </Grid>
                
            ))}
    </Grid>

        
        </div>
    
            </div>
        </div>
    )
}


export default ContainerAut
