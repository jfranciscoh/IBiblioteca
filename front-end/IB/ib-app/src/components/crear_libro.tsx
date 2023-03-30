import React, { useState } from 'react';
import { TextField, Button, Grid } from '@mui/material';

const AddBookForm = () => {
  const [book, setBook] = useState({
    title: '',
    author: '',
    publisher: '',
    year: '',
    location: ''
  });

  const handleInputChange = (event: { target: { name: any; value: any; }; }) => {
    const { name, value } = event.target;
    setBook({ ...book, [name]: value });
  }

  const handleSubmit = (event: { preventDefault: () => void; }) => {
    event.preventDefault();
    console.log(book);
    // Aquí se puede agregar el código para enviar los datos del formulario a la base de datos o almacenarlos en el estado de la aplicación
  }

  return (
    <form onSubmit={handleSubmit}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <TextField name="title" label="Título" value={book.title} onChange={handleInputChange} fullWidth />
        </Grid>
        <Grid item xs={12}>
          <TextField name="author" label="Autor" value={book.author} onChange={handleInputChange} fullWidth />
        </Grid>
        <Grid item xs={12}>
          <TextField name="publisher" label="Editorial" value={book.publisher} onChange={handleInputChange} fullWidth />
        </Grid>
        <Grid item xs={12}>
          <TextField name="year" label="Año" value={book.year} onChange={handleInputChange} fullWidth />
        </Grid>
        <Grid item xs={12}>
          <TextField name="location" label="Ubicación" value={book.location} onChange={handleInputChange} fullWidth />
        </Grid>
        <Grid item xs={12}>
          <Button type="submit" variant="contained" color="primary">
            Agregar libro
          </Button>
        </Grid>
      </Grid>
    </form>
  );
};

export default AddBookForm;
