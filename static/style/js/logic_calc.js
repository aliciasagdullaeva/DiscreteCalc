"use strict";

const input = document.getElementById("textLine");
const divRef = document.getElementById("textDiv");

let isVariablePressed = false;
let lastCharacter = null;

function addChar(character) {
  const logicOperators = ["∧", "∨", "¬", "→", "↔", "↓", "|", "⊕"];
  const variableIndexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];

  const characterNode = document.createElement("span");
  const newSub = document.createElement("sub");

  if (logicOperators.includes(character)) {
    isVariablePressed = false;
  }

  if (character === "X") {
    isVariablePressed = true;
  }

  if (variableIndexes.includes(character) && isVariablePressed) {
    newSub.innerText += character;
    characterNode.appendChild(newSub);
    divRef.appendChild(characterNode);
    input.value += character;
    return;
  }

  characterNode.innerText += character;
  divRef.appendChild(characterNode);
  input.value += character;
}

const clearInput = () => {
  input.value = "";
  divRef.innerHTML = "";
};

const removeLastItem = () => {
  input.value = input.value.slice(0, -1);
  divRef.removeChild(divRef.lastChild);
};
