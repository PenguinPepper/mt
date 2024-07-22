import React from 'react';
import header_logo from '../assets/images/header_logo.svg';
import { navLinks } from '../constants';
import hamburger from '../assets/icons/hamburger.svg';
import Button from './Button';

const Nav = () => {
    return (
        <header className="sm:px-16 px-8 py-8 absolute z-10 w-full ">
            <nav className="flex justify-between items-center max-container">
                <a href="/">
                    <img src={header_logo}
                        alt="Mission Togother Logo: has a m with a t inside of it."
                        width={130}
                        height={29} />
                </a>
                <ul className="flex-1 flex justify-center items-center gap-16 max-lg:hidden">
                    {navLinks.map((item) => (
                        <li key={item.label}>
                            <a href={item.href} className="leading-normal text-lg text-slate-gray">
                                {item.label}
                            </a>
                        </li>
                    ))}
                </ul>
                <menu className="hidden max-lg:block">
                    <img src={hamburger} alt="hamburger" width={25} height={25} />
                    {/* <ul>
                        {navLinks.map((item) => (
                            <li key={item.label}>
                                <a href={item.href} className="leading-normal text-lg text-slate-gray">
                                    {item.label}
                                </a>
                            </li>
                        ))}
                    </ul> */}
                </menu>
                <div className="space-x-1.5 max-lg:hidden">
                    <Button label="Sign Up" intent="welcoming" />
                    <Button label="Log In" intent="logging_in" />
                </div>
            </nav>

        </header>
    )
}

export default Nav;