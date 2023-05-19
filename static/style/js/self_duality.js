'use strict'

const condition = document.getElementById('conditionTextArea')
const conditionInput = document.getElementById('condition-input')

const result = document.getElementById('result')
const conditionResult = document.getElementById('condition-result')

const parsedResult = document.getElementById('condition-result-array')

const variableIndexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
const logicOperators = ["∧", "∨", "¬", "→", "↔", "↓", "|", "⊕"];

let isVariablePressed = false
let isVariablePressedResult = false

function addChar(character) {
  const conditionInput = document.getElementById('condition-input')
  const condition = document.getElementById('condition')

  const lastCharacter = getLastCharacter(conditionInput.value);

  if (lastCharacter === 'X' && character === 'X') return;
  if (lastCharacter === '¬' && character === '¬') return;

  if(logicOperators.includes(lastCharacter)) {
    const characters = ["∧", "∨", "→", "↔", "↓", "|", "⊕"];
    if(characters.includes(character)) return;
  }

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
  result.innerText = ''
  conditionResult.innerText = ''
  parsedResult.innerText = ''
}

function removeLastItem (conditionNumber = 1)  {
  conditionInput.value = conditionInput.value.slice(0, -1)
  condition.removeChild(condition.lastChild)
}

function parseResult(character) {
  const logicOperators = ['∧', '∨', '¬', '→', '↔️', '↓', '|', '⊕']
  const variableIndexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  const characterNode = document.createElement('span')
  const newSub = document.createElement('sub')

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
  parsedResult.innerHTML = '<div>Данная функция является самодвойственной</div>' // TODO Change text
}

if (result.innerText === 'False') {
  parsedResult.innerHTML = '<div>Данная функция не является самодвойственной</div>' // TODO Change text
}

if (result.innerText !== '') {
  const conditionResult = document.getElementById('condition-result')
  const str = conditionResult.innerText
  for (const strElement of str) {
    parseResult(strElement)
  }
  parsedResult.classList.remove('d-none')
}
