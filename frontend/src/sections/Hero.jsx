import React from 'react';
import Button from '../components/Button';
import arrow_right from '../assets/icons/arrow_right.svg';
import landing1 from '../assets/images/landing1.svg'

const Hero = () => {
    return (
        <section id="home" className="w-full flex xl:flex-row flex-col justify-center min-h-screen gap-10 max-container border-naple">
            <section className='relative xl:w-2/5 flex flex-col justify-center items-start w-full pt-28 max-xl:sm:px-16 px-8'>
                <h1 class="font-thin text-3xl font-playfare italic mb-2">Dream work takes teamwork. Let's find you the perfect team mates.</h1>
                <h3 class="tracking-tight text-8xl max-sm:text-[72px] text-pumpkin font-thin mb-3 mt-6 xl-bg-white xl:whitespace-nowrap relative z-10 pr-10">Mission Together</h3>
                <p class="text-base text-lg leading-8 mt-6 mb-1 sm:max-w-sm">Explore fellow sudents and get an idea of what its like to work with them from those who have.</p>
                <Button label="Join Now" intent="welcoming" iconURL={arrow_right} />
            </section>
            <section className="relative flex-1 flex justify-center items-center xl:min-h-screen max-xl:py-40  bg-primary bg-hero bg-cover bg-center">
                <img src={landing1} alt="Two figures one sitting down holding two images and he other standing looking at those two images"
                    width={610}
                    height={502}
                    className="object-contain relative z-10" />
            </section>
        </section>
    )
}

export default Hero;