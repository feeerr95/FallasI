import React from 'react';
import RadioGroup from '@mui/material/RadioGroup';
import FormControl from '@mui/material/FormControl';
import Radio from '@mui/material/Radio';
import FormControlLabel from '@mui/material/FormControlLabel';

export const Form = ({ options, onSelect, children }) => {
  return (
    <FormControl>
      <RadioGroup>
        {options.map(({ label, value }) => (
          <FormControlLabel
            key={label}
            onChange={({ target }) => onSelect(target.value)}
            value={value}
            control={<Radio />}
            label={label}
          />
        ))}
      </RadioGroup>
      {children}
    </FormControl>
  );
};
