import React from "react";
import HomeSectionCard from "../HomeSectionCard/HomeSectionCard";
import { kurtaProducts } from "../../../data/menskurta";

const HomeSectionCarosel = () => {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
      {kurtaProducts.map((item) => (
        <HomeSectionCard key={item.id} product={item} />
      ))}
    </div>
  );
};

export default HomeSectionCarosel;