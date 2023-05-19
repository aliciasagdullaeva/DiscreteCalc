'use strict'

const firstCondition = document.getElementById('first-condition')
const firstConditionInput = document.getElementById('first-condition-input')

const secondCondition = document.getElementById('second-condition')
const secondConditionInput = document.getElementById('second-condition-input')

const result = document.getElementById('result')

const parsedResult = document.getElementById('condition-result-array')

const variableIndexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
const logicOperators = ["∧", "∨", "¬", "→", "↔", "↓", "|", "⊕"];

let isFirstConditionVariablePressed = false
let isSecondConditionVariablePressed = false
let isVariablePressedResult = false

function addChar(character, conditionNumber = 1) {
  const conditionInput = conditionNumber === 1 ? firstConditionInput : secondConditionInput;
  const condition = conditionNumber === 1 ? firstCondition : secondCondition;

  const lastCharacter = getLastCharacter(conditionInput.value);

  if (lastCharacter === 'X' && character === 'X') return;
  if (lastCharacter === '¬' && character === '¬') return;

  if(logicOperators.includes(lastCharacter)) {
    const characters = ["∧", "∨", "→", "↔", "↓", "|", "⊕"];
    if(characters.includes(character)) return;
  }


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

function parseResult(character) {
  const logicOperators = ['∧', '∨', '¬', '→', '↔', '↓', '|', '⊕']
  const variableIndexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  const characterNode = document.createElement('span')
  const newSub = document.createElement('sub')

  const parsedResult = document.getElementById(`condition-result-array`)

  if (logicOperators.includes(character)) {
    isVariablePressedResult = false
  }

  if (character === 'X') {
    isVariablePressedResult = true
  }

  if (variableIndexes.includes(character) && isVariablePressedResult) {
    newSub.innerText += character
    characterNode.appendChild(newSub)
    parsedResult.appendChild(characterNode)
    return
  }

  characterNode.innerText += character
  parsedResult.appendChild(characterNode)
  return
}

if (result.innerText === '') result.innerText = ''

if (result.innerText === 'True') {
  parsedResult.innerHTML = '<div>Данные функции эквивалентны</div>'
}

if (result.innerText === 'False') {
  parsedResult.innerHTML = '<div>Данные функции не эквивалентны</div>'
}

if (result.innerText !== '') {
  let conditionResult = document.getElementById('first-condition-result')
  let str = conditionResult.innerText
  for (const strElement of str) {
    parseResult(strElement)
  }


  const newDiv = document.createElement('div')
  conditionResult = document.getElementById('condition-result-array')
  conditionResult.appendChild(newDiv)

  conditionResult = document.getElementById('second-condition-result')
  str = conditionResult.innerText
  for (const strElement of str) {
    parseResult(strElement)
  }

  parsedResult.classList.remove('d-none')
}