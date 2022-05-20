import React from 'react'
import { useEffect,useState } from 'react';
import axios from 'axios';
import Grid from '@mui/material/Grid'




const Middle = () => {
    

    return (
    <div className=" bg-white  ml-2   shadow-sm w-full h-screen   ">
        <Grid container >
            {data.map( article =>(
                <Grid item key = {article.id} >
                    <Card sx={{ maxWidth: 250 }}>
        <CardMedia
            component="img"
            height="140"
            image='/listic.png'
            alt="green iguana"
        />
        <CardContent>
            <Typography gutterBottom variant="h5" component="div">
            Lizard
            </Typography>
            <Typography variant="body2" color="text.secondary">
            Lizards are a widespread group of squamate reptiles, with over 6,000
            species, ranging across all continents except Antarctica
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
    )
}

export default Middle
