import React from 'react';
import MainCarosel from '../../components/HomeCarosel/MainCarosel';
import HomeSectionCarosel from '../../components/HomeSectionCarosel/HomeSectionCarosel';
import KeyboardArrowLeftIcon from '@mui/icons-material/KeyboardArrowLeft';

const HomePage = () => {
  return (
    <div>
      <MainCarosel />

      <div className='space-y-10 py-20'>
        <HomeSectionCarosel />
        <HomeSectionCarosel />
        
       
        
      </div>

      <button variant="contained" className="z-50" sx={{ position: 'absolute', top: '8rem', left: '0rem ', transform: 'translateY(-50%)' }} color="white" aria-label="next">
        
       <KeyboardArrowLeftIcon />
      </button>

    </div>
  );
};

export default HomePage;