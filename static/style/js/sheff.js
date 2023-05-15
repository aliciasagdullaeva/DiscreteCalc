'use strict'

const condition = document.getElementById('condition')
const conditionInput = document.getElementById('condition-input')


const variableIndexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
const logicOperators = ["∧", "∨", "¬", "→", "↔", "↓", "|", "⊕"];


let isVariablePressed = false

function addChar(character) {
  const conditionInput = document.getElementById('condition-input')
  const condition = document.getElementById('condition')

  const lastCharacter = getLastCharacter(conditionInput.value);

  if (lastCharacter === 'X' && character === 'X') return;

  if(logicOperators.includes(lastCharacter) && logicOperators.includes(character)) return;

  if (character === 'X') {
    isVariablePressed = true
  } else if (logicOperators.includes(character)) {
    isVariablePressed = false
  }

  const characterNode = document.createElement('span');
  const newSub = document.createElement('sub');

  if (variableIndexes.includes(character) && isVariablePressed) {
    newSub.innerText += character;
    characterNode.appendChild(newSub);
    condition.appendChild(characterNode);
    conditionInput.value += character;
  } else {
    characterNode.innerText += character;
    condition.appendChild(characterNode);
    conditionInput.value += character;
  }
}

function getLastCharacter(condition) {
  if (!condition) return '';
  return condition.charAt(condition.length - 1);
}

function clearInput (conditionNumber = 1) {
  conditionInput.value = "";
  condition.innerHTML = "";
}

function removeLastItem (conditionNumber = 1)  {
  conditionInput.value = conditionInput.value.slice(0, -1)
  condition.removeChild(condition.lastChild)
}