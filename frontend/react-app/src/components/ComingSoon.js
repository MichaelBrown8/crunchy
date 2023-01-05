import { NavLink } from 'react-router-dom';
import './css/Cart.css'

const ComingSoon = () => {

    return (
        <div className='empty-cart-container'>
            <div className='dog-in-box-image-container'>
                <img
                    className='dog-in-box-image'
                    src={'https://res.cloudinary.com/dfrj03hsi/image/upload/v1672905198/Crunchy%20images/dog-in-box_akinfp.jpg'}
                    alt='doggo' />
            </div>
            <div>
                <div className='oops'>
                    Feature coming soon!
                </div>
                <div className='continue-shopping-div'>
                    <NavLink
                        className='continue-shopping-link'
                        to='/'>
                        Continue Shopping
                    </NavLink>
                </div>
            </div>
        </div>
    );
};

export default ComingSoon;
