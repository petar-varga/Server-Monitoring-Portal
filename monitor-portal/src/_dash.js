/* eslint-disable no-useless-escape */
export const isEmpty = (obj) =>
  [Object, Array].includes((obj || {}).constructor) &&
  !Object.entries(obj || {}).length;

export const isEmptyObj = (obj) => {
  for (const key in obj) {
    if (
      obj[key] !== null &&
      obj[key] !== "" &&
      obj[key] !== false &&
      obj[key] !== undefined
    )
      return false;
  }
  return true;
};

export const allowOnlyIntegers = (evt) => {
  const charCode = evt.which ? evt.which : evt.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
    evt.preventDefault();
  }
};

export const roundOff = (value) => {
  return Math.round(value * 100) / 100;
};

export const random = (array) => {
  return array[Math.floor(Math.random() * array.length)];
};

export const range = (start, end) =>
  Array.from({ length: end + 1 - start }, (v, k) => k + start);

export const sort = (data, sortKey) => {
  return data.sort((a, b) => {
    return (
      (a[sortKey] === null) - (b[sortKey] === null) ||
      +(a[sortKey] > b[sortKey]) ||
      -(a[sortKey] < b[sortKey])
    );
  });
};
