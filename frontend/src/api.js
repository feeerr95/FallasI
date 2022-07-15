import axios from 'axios';

const api = axios.create();

export const getNewErrors = async (selectedOption) => {
  console.log(selectedOption)
  const resp = await api.get(`http://localhost:8000/api/trouble?name=${selectedOption}`);
  const { data, status } = resp;

  try {
    if (status !== 200) return [];
    else return data;
  } catch (error) {
    console.error(error);
  }
};
