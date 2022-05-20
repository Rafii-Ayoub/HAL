import '../styles/globals.css'
import 'tailwindcss/tailwind.css'
import { MoralisProvider } from "react-moralis";

function MyApp({ Component, pageProps }) {
  return( 
  
<MoralisProvider
  appId="uCUwtfvdY6Jf9Iv9MzciWSTGD1SPqHzVLMcxd79b"
  serverUrl='https://3ml0xqvekni2.usemoralis.com:2053/server'>
  <Component {...pageProps}/>
  </MoralisProvider>
  )
}

export default MyApp
