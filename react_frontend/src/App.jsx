import React from 'react';
import { Hero, Features, AboutUs, Footer } from './sections';
import Nav from './components/Nav';
import SignUp from './components/SignUp';


const App = () => {
  return (
    <main className="relative">
      <SignUp />
      {/* <Nav />
      <section className="xl:pl-16 pl-8 wide:sm:pr-16 pr-8 sm:pb-24 pb-12">
        <Hero />
      </section>
      <section className="sm:px-16 px-8 sm:py-24 py-12">
        <Features />
      </section>
      <section className="sm:px-16 px-8 sm:py-24 py-12">
        <AboutUs />
      </section>
      <section className="bg-pumpkin sm:px-16 px-8 sm:pt-24 pt-12 pb-8">
        <Footer />
      </section> */}
    </main>


  )
}

export default App;
