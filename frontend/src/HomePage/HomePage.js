import React, {useState} from "react";
import { Button } from "@mui/material";
import { Form } from "../Form/Form";
import { getNewErrors } from "../api";
import './styles.css';


const initialErrors = [
  'Problemas con la primer capa',
  'Hilos rodeando la pieza',
  'Mala definición de la pieza',
  'La pieza está desfasada',
  'Pieza a medio hacer',
  'Ausencia de filamento al inicio de la impresión',
];

export const HomePage = () => {
  const [errors, setErrors] = useState(initialErrors);
  const [selectedOption, setSelectedOption] = useState('');

  const handleNext = async () => {
    const newErrors = await getNewErrors(selectedOption);
    setErrors(newErrors);
  }

  return (
    <div className="page">
      <span className="t-stroke t-shadow pageTitle">3D ERRORS</span>
      {/* <span className="pageTitle">3D-ERRORS</span> */}
      <div className="card">
        <span className="title">Indique cual es el error que presenta.</span>
        <div className="form">
          <span className="subtitle">Seleccione alguna de las siguientes opciones.</span>
          <Form errors={errors} onSelect={setSelectedOption} />
        </div>
        <Button 
          onClick={handleNext}
          className="button"
          variant="contained"
        >
          Siguiente
        </Button>
      </div>
    </div>
  )
};
