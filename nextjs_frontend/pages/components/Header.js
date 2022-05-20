import CropLandscapeIcon from '@material-ui/icons/CropLandscape';
import Button from '@material-ui/core/Button'
import { useMoralis } from "react-moralis";
import React, { useState, useEffect } from 'react'



const Header = () => {
    const { authenticate, isAuthenticated, user ,logout } = useMoralis();
    if (!isAuthenticated) {
        
        return(
            <div className="flex shadow-sm  p-4 justify-between  ">
                <div className="flex space-x-3  ">
                    <p className="text-blue-500 text-lg font-semibold">Wallet Address  : </p>
                    <p></p>
                    <CropLandscapeIcon className="text-gray-300" />
                   
    
                </div>
                <div className="flex ">
                <Button id='connect' variant="contained" size="large"  onClick={() => authenticate()}
   >Connect Your Wallet</Button>                </div>
            </div>)
    }
    else{
        const [address, setAddress] = useState();

        useEffect(() => {
            if (isAuthenticated) {
              setAddress(user.attributes.ethAddress);
            }
          }, [isAuthenticated]);

        return(
            <div className="flex shadow-sm  p-4 justify-between  ">
                <div className="flex space-x-3  ">
                    <p className="text-blue-500 text-lg font-semibold"> Wallet Address : {address} </p>
                    
                    <CropLandscapeIcon className="text-gray-300" />
                    
    
                </div>
                <div className="flex ">
                <Button id='disconnect'  size="large" onClick={() => logout()}
   >Disconnect Your Wallet</Button>                </div>
            </div>)
    }
    
       

    
        
    
}

export default Header
