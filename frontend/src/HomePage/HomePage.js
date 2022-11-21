import React, { useState } from 'react';
import { Button } from '@mui/material';
import { Form } from '../Form/Form';
import { getFirstQuestion, getNewErrors, getNextQuestion } from '../api';
import './styles.css';

const INITIAL_OPTIONS = [
  {
    label: 'Problemas con la primer capa',
    value: 'Problemas con la primer capa',
  },
  {
    label: 'La pieza está desfasada',
    value: 'La pieza está desfasada',
  },
  {
    label: 'La pieza esta rodeada de hilos',
    value: 'La pieza esta rodeada de hilos',
  },
  {
    label: 'La pieza quedó a medio hacer',
    value: 'La pieza quedó a medio hacer',
  },
];

const OPTIONS = [
  { label: 'Si', value: true },
  { label: 'No', value: false },
];

const INITIAL_TITLE = '¿Cuál es su problema actual?';

export const HomePage = () => {
  const [title, setTitle] = useState(INITIAL_TITLE);
  const [isFirstQuestion, setIsFirstQuestion] = useState(true);
  const [selectedCondition, setSelectedCondition] = useState();
  const [currentCondition, setCurrentCondition] = useState();
  const [currentQuestion, setCurrentQuestion] = useState();
  const [finishResponse, setFinishResponse] = useState('');

  const handleNext = async () => {
    const { nextCondition, nextQuestion, result } = isFirstQuestion
      ? await getFirstQuestion(selectedCondition)
      : await getNextQuestion(currentCondition, selectedCondition);

    if (result) {
      setTitle(result);
      setFinishResponse(result);
    } else {
      setTitle(nextQuestion);
      setIsFirstQuestion(!!result);
      setCurrentCondition(nextCondition);
      setCurrentQuestion(nextQuestion);
    }
  };

  const handleReset = () => {
    setIsFirstQuestion(true);
    setTitle(INITIAL_TITLE);
    setFinishResponse();
  };

  return (
    <div className="page">
      <span className="t-stroke t-shadow pageTitle">3D ERRORS</span>
      <div className="card">
        <span className="title">
          {isFirstQuestion || finishResponse ? title : currentQuestion}
        </span>
        <div className="form">
          {!finishResponse && (
            <Form
              options={isFirstQuestion ? INITIAL_OPTIONS : OPTIONS}
              onSelect={setSelectedCondition}
            />
          )}
          <div className="buttonsContainer">
            <Button fullWidth onClick={handleReset} variant="text">
              Resetear
            </Button>
            {!finishResponse && (
              <Button fullWidth onClick={handleNext} variant="contained">
                Siguiente
              </Button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
