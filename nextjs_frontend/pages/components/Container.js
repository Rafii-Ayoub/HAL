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

const Container = () => {
let [walletBalance, setBalance] = useState(0);
let [marketingBalance, setMarketing] = useState(0);
let [buyBackBalance, setBuyBack] = useState(0);
let [walletBnb, setWalletBnb] = useState(0);
let [walletAddress,setWalletAddress] = useState(0);
const [articles, setArticles] = useState([]);

const { authenticate, isAuthenticated, user ,logout } = useMoralis();


    

  
useEffect(() => {
    fetch('http://localhost:5000/publications')
      .then((res) => res.json())
      .then((data) => {
        setArticles(data);
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
            {removeduplicates(articles).map( article =>(
                <Grid item key = {article.id}  md={3} lg={4}>
                    <Card sx={{ maxWidth: 350 }}>
        <CardMedia
            component="img"
            height="140"
            image='/listic.png'
            alt="green iguana"
        />
        <CardContent>
            <Typography gutterBottom variant="h6" component="div">
            {article.title}
            </Typography>
            
        </CardContent>
        <CardActions>
            <Button size="medium">OPEN</Button>
            <Button size="big">BUY</Button>
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


export default Container
