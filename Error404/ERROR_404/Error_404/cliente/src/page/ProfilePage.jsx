// ProfilePage.jsx
import React from 'react';

const ProfilePage = () => {
  const user = {
    name: "HOMER J. SIMPSON",
    direccion: "Calle Lola Mento",
    email: "homerjsimpson@gmail.com",
    cargo: "Planta Nuclear",
    profilePicture: "https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2017/01/coche-homer-simpson_1.jpg?tf=1200x"
  };

  return (
    <div className="flex flex-col items-center mt-10">
      <h1 className="text-3xl font-bold text-gray-800 mb-5">Perfil de Usuario</h1>
      <div className="text-center">
        <img
          src={user.profilePicture}
          alt="Perfil"
          className="rounded-full border-4 border-gray-300 mb-5"
          width="150"
        />
        <h2 className="text-2xl font-semibold text-gray-800">{user.name}</h2>
        <p className="text-lg text-gray-600">{user.cargo}</p>
        <p className="text-lg text-gray-600">{user.direccion}</p>
        <p className="text-lg text-gray-600">{user.email}</p>
      </div>
    </div>
  );
};

export default ProfilePage;
