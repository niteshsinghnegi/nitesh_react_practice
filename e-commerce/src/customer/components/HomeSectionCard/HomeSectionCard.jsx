import React from 'react'

const HomeSectionCard = () => {
  return (
    <div className="cursor-pointer flex flex-col items-center bg-white rounded-lg shadow-lg overflow-hidden w-[15rem] mx-3 border - black">

      <div className="h-[13rem] w-[10rem]">
        <img
          src="https://images.unsplash.com/photo-1593032465175-481ac7f401a0?q=80&w=1920"
          alt="No Filter"
          className="object-cover object-top w-full h-full"
        />
      </div>

      <div className="p-4">
        <h3 className="text-lg font-bold text-gray-800">
          Nofilter
        </h3>

        <p className="mt-2 text-sm text-gray-600">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, doloremque.
        </p>
      </div>

    </div>
  )
}

export default HomeSectionCard
