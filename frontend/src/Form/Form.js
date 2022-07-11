import React from 'react';
import RadioGroup from '@mui/material/RadioGroup';
import FormControl from '@mui/material/FormControl';
import Radio from '@mui/material/Radio';
import FormControlLabel from '@mui/material/FormControlLabel';

export const Form = ({errors, onSelect}) => {

  return (
    <FormControl>
      <RadioGroup>
        {errors.map(error => 
          <FormControlLabel 
            key={error}
            onChange={e => onSelect(e.target['value'])}
            value={error}
            control={<Radio />}
            label={error}
          />
        )}
      </RadioGroup>
    </FormControl>
  );
};
