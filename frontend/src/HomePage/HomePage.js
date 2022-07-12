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
const INITIAL_TITLE = '¿CUÁL ES SU PROBLEMA ACTUAL?';

export const HomePage = () => {
  const [errors, setErrors] = useState(initialErrors);
  const [selectedOption, setSelectedOption] = useState('');
  const [response, setResponse] = useState('')
  const [title, setTitle] = useState(INITIAL_TITLE)

  const handleNext = async () => {
    const {response, newErrors} = await getNewErrors(selectedOption);
    setErrors(newErrors);
    setTitle('OBSERVA O REALIZÓ ALGUNA DE LAS SIGUIENTES OPCIONES')
    setResponse(response)
  }

  const handleReset = () => {
    setErrors(initialErrors);
    setResponse('');
    setTitle(INITIAL_TITLE);
  }

  return (
    <div className="page">
      <span className="t-stroke t-shadow pageTitle">3D ERRORS</span>
      <div className="card">
        {response 
        ? (
          <>
            <span className="title">SOLUCIÓN / PROBLEMA DE SU ERROR</span>
            <span>{response}</span>
            <Button 
              onClick={handleReset}
              className="button"
              variant="contained"
            >
              Reiniciar
            </Button>
          </>
        ) : (
          <>
            <span className="title">{title}</span>
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
          </>
        )}
      </div>
    </div>
  )
};
