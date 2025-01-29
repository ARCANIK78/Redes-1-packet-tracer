import * as React from "react";
import { styled } from "@mui/material/styles";
import Link from "@mui/material/ListItemText";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { SidebarContext } from "./SideBar";

export const Logo = React.forwardRef(({
  children,
  img = "",
  imgStyle = {},
}, ref) => {
  const customizer = React.useContext(SidebarContext);
  const LogoStyled = styled(Link)(() => ({
    whiteSpace: "nowrap",
    overflow: customizer.isCollapse ? "hidden" : "visible",
    WebkitLineClamp: "1",
    fontSize: "2rem",
    padding: "15px 22px",
    textOverflow: "ellipsis",
  }));

  return (
    <LogoStyled href="/">
      {img === "" ? (
        <Typography variant="body">{children}</Typography>
      ) : (
        <Box
          component="img"
          sx={{
            display: "flex",
            alignItems: "center",
            ...imgStyle, // Aplicamos los estilos personalizados
          }}
          src={img}
        />
      )}
    </LogoStyled>
  );
});
