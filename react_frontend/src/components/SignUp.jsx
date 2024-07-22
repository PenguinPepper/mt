import React from 'react';
import { useForm } from 'react-hook-form';
import { DevTool } from '@hookform/devtools';
import signupImage from '../assets/images/signupImage.svg';
import header_logo from '../assets/images/header_logo.svg';
import Button from './Button';

const SignUp = () => {
    // Button component will deal with all the buttons
    // props: label - label to be displayed
    // intent - determines colour of the button.
    const form = useForm();
    const { register, control, handleSubmit, formState } = form;
    const { errors } = formState;

    const onSignUp = (data) => {
        //capture enter input
        //if they are alx students then send a post request to api
        //have the api save the new user in the database and save their credentials
        console.log('Form submitted:', data);
    }

    return (
        <section className="max-xl:sm:px-16 px-8">
            <nav className=" flex flex-row pt-6">
                <a href="/">
                    <img src={header_logo}
                        alt="Mission Togother Logo: has a m with a t inside of it."
                        width={130}
                        height={29}
                        className='relative z-10'
                    />
                </a>
                <h3 className='text-3xl py-3'>Mission Together</h3>
            </nav>
            <section className='max-container flex pt-5 '>
                <section className="relative max-w-xl xl:w-2/5 flex flex-col justify-center items-stretch">
                    <form onSubmit={handleSubmit(onSignUp)} className='flex flex-col'>
                        <fieldset>
                            <legend>Are you an enrolled student at ALX?</legend>
                            <input type="radio" name="inAlx" value="yes" id="alx-yes" {...register("alxStatus")} className="form-radio " />
                            <label htmlFor="inAlx" className='mr-3 ml-1'>Yes</label>

                            <input type="radio" name="notAlx" value="no" id="alx-no" {...register("alxStatus")} className="form-radio" />
                            <label htmlFor="notAlx" className='mr-3 ml-1'>No</label>
                        </fieldset>
                        <label htmlFor='name' className="mt-3">Name: </label>
                        <input type="text" name="name" id="name" {...register("name")} className="form-input rounded-3xl mb-3" />

                        <label htmlFor='surname'>Surname: </label>
                        <input type="text" name="surname" id="surname" {...register("surname")} className="form-input rounded-3xl mb-3" />

                        <label htmlFor="email">Email address: </label>
                        <p className="text-sm ml-3 text-red-600">{errors.email?.message}</p>
                        <input type="email" name="email" id="emil" {...register("email",
                            {
                                required: {
                                    value: true,
                                    message: "Email address is required",
                                },
                                pattern: {
                                    value:
                                        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                                    message: "Invalid email format"
                                },
                            })} className="form-input rounded-3xl mb-3" />

                        <label htmlFor="password">Password: </label>
                        <p className="text-sm ml-3 text-red-600">{errors.password?.message}</p>
                        <input type="password" name="password" id="password" {...register("password",
                            {
                                required: {
                                    value: true,
                                    message: "Password is required",
                                },
                            })} className="form-input rounded-3xl mb-3" />

                        <label htmlFor="githubUsername">Github Username</label>
                        <input type="text" name="githubUsername" id="githubUsername" {...register("githubUsername")} className="form-input rounded-3xl mb-3" />

                        <Button label="Sign Up" intent="welcoming" />
                    </form>
                    <DevTool control={control} />
                </section>
                <section className="max-sm:hidden relative flex flex-1 justify-center items-center">
                    <img src={signupImage}
                        width={650}
                        height={502}
                        className="object-contain relative z-10" />
                </section>
            </section>
        </section>
    )
}

export default SignUp;