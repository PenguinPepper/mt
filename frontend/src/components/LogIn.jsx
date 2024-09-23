import React from 'react';
import { useForm } from 'react-hook-form';
import { DevTool } from '@hookform/devtools';
import Button from './Button';
import header_logo from '../assets/images/header_logo.svg';


const LogIn = () => {
    //Signup form
    const form = useForm();
    const { register, control, handleSubmit, formState } = form;
    const { errors } = formState;

    const onSubmit = (data) => {
        //Capture the new inputs
        //acess the values onebyone
        // send them in a proper post request to log in to website
        console.log('Form submitted', data)
    }

    return (
        <section className='max-sm:w-fit w-5/12 max-sm:px-10 flex flex-row justify-center  max-sm:min-h-screen min-h-fit gap-10 max-container border border-4 border-amber-100  mt-4'>
            <section>
                <img
                    src={header_logo}
                    alt="Mission Togother Logo: has a m with a t inside of it."
                    width={130}
                    height={29}
                    className='my-10 mx-10' />
                <form onSubmit={handleSubmit(onSubmit)} noValidate className='flex flex-col pb-9'>
                    <label htmlFor="email" className='text-lg ml'>
                        Email Address:
                        <p className="text-sm ml-3 text-red-600">{errors.email?.message}</p>
                    </label>
                    <input type="email" name="email" {...register("email", {
                        required: {
                            value: true,
                            message: "Email address is required",
                        },
                        pattern: {
                            value:
                                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                            message: "Invalid email format"
                        },
                    })} className="form-input px-3 py-2 rounded-3xl mb-5" />


                    <label htmlFor="password" className='text-lg'>
                        Password:
                    </label>
                    <input type="password" name="password" {...register("password", {
                        required: "Password is required",
                    })} className="form-input px-3 py-2 rounded-3xl mb-7" />

                    <Button label="Log In" intent="loggingIn" />
                </form>
                <DevTool control={control} />
            </section>
        </section>
    )
}

export default LogIn;