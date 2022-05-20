
import Header from "./components/Header"
import ContainerAut from "./components/ContainerAut"
import Sidebar from "./components/sidebar"
import React, {useState, useEffect} from 'react';





export default function Home() {

  return (
    <div>
      <div className="flex w-full  " >
      <Sidebar />
        <div className="w-screen " id="middle">
          <Header />
          <div id="container">
          <ContainerAut/>
          </div>
          
        </div>
      </div>

    </div>
  )
}
