import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';

import { Sidebar } from "./components/SideBar";
import { Logo } from "./components/Logo";
import { Menu } from "./components/Menu";
import { MenuItem } from "./components/MenuItem";
import { Submenu } from './components/Submenu';
import HomePage from './page/HomePage';
import SettingsPage from './page/SettingsPage';
import ProfilePage from './page/ProfilePage';

import React, { useState } from 'react';
import { Menu as MUI_Menu, MenuItem as MUI_MenuItem, Button } from '@mui/material';

function App() {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Router>
      <div style={{ display: 'flex' }}>
        {/* Sidebar */}
        <Sidebar width={"270px"}>
          <Logo 
            img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj-wUZvLtE8x2ARpVHXiUh6wqQR-y6tE-9NfJn96siD9LolxdtA8TP_Sc8oXPycYyjwi8&usqp=CAU"
            imgStyle={{ width: "100px", height: "auto" }}
          >
            AdminMart 
          </Logo>

          <Menu subHeading="HOME">
            {/* Menú con redirección para Home */}
            <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
              <MenuIx tem link="/" badge="true">
                Home
              </MenuIx>
            </Link>
            {/* Menú con redirección para Settings */}
            <Link to="/settings" style={{ textDecoration: 'none', color: 'inherit' }}>
              <MenuItem>Settings</MenuItem>
            </Link>
            {/* Menú con redirección para Profile */}
            <Link to="/profile" style={{ textDecoration: 'none', color: 'inherit' }}>
              <MenuItem>Profile</MenuItem>
            </Link>
          </Menu>

          <Menu subHeading="APPS">
            <MenuItem>Chat</MenuItem>
            <MenuItem>Calendar</MenuItem>
          </Menu>

          <Menu subHeading="OTHERS">
            <Submenu title="Menu Level">
              <MenuItem>Post</MenuItem>
              <MenuItem>Details</MenuItem>
              <Submenu title="Level 2">
                <MenuItem>new</MenuItem>
                <MenuItem>Hello</MenuItem>
              </Submenu>
            </Submenu>

            <MenuItem>Chip</MenuItem>
            <MenuItem target="_blank" link="google.com">
              External Link
            </MenuItem>
          </Menu>
        </Sidebar>

        {/* Contenedor de las páginas */}
        <div style={{ flex: 1, padding: '20px' }}>
          <Routes>
            {/* Define las rutas aquí */}
            <Route path="/" element={<HomePage />} />
            <Route path="/settings" element={<SettingsPage />} />
            <Route path="/profile" element={<ProfilePage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
