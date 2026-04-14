import React from "react";
import AliceCarousel from "react-alice-carousel";
import "react-alice-carousel/lib/alice-carousel.css";
import { MainCarouselData } from "./MainCaroselData";

const MainCarousel = () => {

  const items = MainCarouselData.map((item, index) => (
    <div key={index}>
      <img
        src={item.image}
        alt=""
        className="w-full h-[220px] md:h-[320px] lg:h-[380px] object-cover"
      />
    </div>
  ));

  return (
    <AliceCarousel
      items={items}
      autoPlay
      autoPlayInterval={2000}
      infinite
      disableButtonsControls
      disableDotsControls={false}
      mouseTracking
    />
  );
};

export default MainCarousel;