'use strict'

const firstCondition = document.getElementById('first-condition')
const firstConditionInput = document.getElementById('first-condition-input')

const secondCondition = document.getElementById('second-condition')
const secondConditionInput = document.getElementById('second-condition-input')

const variableIndexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
const logicOperators = ["∧", "∨", "¬", "→", "↔", "↓", "|", "⊕"];

let isFirstConditionVariablePressed = false
let isSecondConditionVariablePressed = false

function addChar(character, conditionNumber = 1) {
  const conditionInput = conditionNumber === 1 ? firstConditionInput : secondConditionInput;
  const condition = conditionNumber === 1 ? firstCondition : secondCondition;

  const lastCharacter = getLastCharacter(conditionInput.value);

  if (lastCharacter === 'X' && character === 'X') return;

  if(logicOperators.includes(lastCharacter) && logicOperators.includes(character)) return;


  if (character === 'X') {
    conditionNumber === 1 ? isFirstConditionVariablePressed = true : isSecondConditionVariablePressed = true;
  } else if (logicOperators.includes(character)) {
    conditionNumber === 1 ? isFirstConditionVariablePressed = false : isSecondConditionVariablePressed = false;
  }

  const characterNode = document.createElement('span');
  const newSub = document.createElement('sub');

  if (variableIndexes.includes(character) && (isFirstConditionVariablePressed || isSecondConditionVariablePressed)) {
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
  if(conditionNumber === 1) {
    firstConditionInput.value = "";
    firstCondition.innerHTML = "";
  } else {
    secondConditionInput.value = "";
    secondCondition.innerHTML = "";
  }
}

function removeLastItem (conditionNumber = 1)  {
  if(conditionNumber === 1) {
    firstConditionInput.value = firstConditionInput.value.slice(0, -1)
    firstCondition.removeChild(firstCondition.lastChild)
  } else {
    secondConditionInput.value = secondConditionInput.value.slice(0, -1)
    secondCondition.removeChild(secondCondition.lastChild)
  }
}