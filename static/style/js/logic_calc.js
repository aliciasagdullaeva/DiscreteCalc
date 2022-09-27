"use strict";

const input = document.getElementById("textLine");

function addChar(character) {
  input.value += character;
}

const clearInput = () => {
  input.value = "";
};

const removeLastItem = () => {
  input.value = input.value.slice(0, -1);
};
