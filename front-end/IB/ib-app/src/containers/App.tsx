import Login from "../components/login"
import { Outlet } from "react-router-dom";
import { Box } from "@mui/material";


function App() {
  return (
    <div className="App">
       <Box sx={{ mt: 10 }}>
        {/* El Outlet se remplazará por el componente asignada a la ruta actual (cf. react-front\src\index.js ) */}
        <Outlet />
      </Box>
    </div>
  );
}

export default App;
