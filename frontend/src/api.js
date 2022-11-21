import axios from 'axios';

const api = axios.create();
const baseUrl = 'http://localhost:8000/api';

export const getNewErrors = async (selectedOption) => {
  const resp = await api.get(`${baseUrl}/trouble?name=${selectedOption}`);
  const { data, status } = resp;

  try {
    if (status !== 200) return [];
    else return data;
  } catch (error) {
    console.error(error);
  }
};

export const getFirstQuestion = async (condition) => {
  const resp = await api.get(`${baseUrl}/rete/firstQuestion/`, {
    params: { condition },
  });
  const { data, status } = resp;

  try {
    if (status !== 200) return [];
    else return data;
  } catch (error) {
    console.error(error);
  }
};

export const getNextQuestion = async (condition, response) => {
  const resp = await api.get(`${baseUrl}/rete/nextQuestion/`, {
    params: { condition, response },
  });
  const { data, status } = resp;

  try {
    if (status !== 200) return [];
    else return data;
  } catch (error) {
    console.error(error);
  }
};
