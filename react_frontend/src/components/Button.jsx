import React from 'react';

const Button = ({ label, intent, iconURL }) => {
    // Button component will deal with all the buttons
    // props: label - label to be displayed
    // intent - determines colour of the button.
    return (
        <button className={`justify-center items-center max-sm:px-4 
         px-6 max-sm:py3 py-4 border text-lg leading-none rounded-full
         text-white ${intent === "welcoming" ? 'bg-fire hover:bg-ice' :
                'bg-naple hover:bg-pumpkin'} ${iconURL ? 'flex' : 'inline'} cursor-pointer border-transparent `}>
            {label}
            {iconURL && (
                <img
                    src={iconURL}
                    alt='arrow right icon'
                    className='ml-2 rounded-full bg-white w-5 h-5'
                />
            )}
        </button>

    )
}

export default Button;