'use strict'

var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
)
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

const input = document.getElementById('textLine')
const divRef = document.getElementById('textDiv')
const condition = document.getElementById('condition')
const conditionFromStorage = sessionStorage.getItem('condition')
const resultArray = document.getElementById('resultArray')
const parsedResult = document.getElementById('parsedResult')

let isVariablePressed = false

let isVariablePressedResult = false

function addChar(character) {
  const logicOperators = ['∧', '∨', '¬', '→', '↔', '↓', '|', '⊕']
  const variableIndexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

  const characterNode = document.createElement('span')
  const newSub = document.createElement('sub')

  if (logicOperators.includes(character)) {
    isVariablePressed = false
  }

  if (character === 'X') {
    isVariablePressed = true
  }

  if (variableIndexes.includes(character) && isVariablePressed) {
    newSub.innerText += character
    characterNode.appendChild(newSub)
    divRef.appendChild(characterNode)
    input.value += character
    return
  }

  characterNode.innerText += character
  divRef.appendChild(characterNode)
  input.value += character
}

const clearInput = () => {
  input.value = ''
  divRef.innerHTML = ''
  sessionStorage.setItem('condition', '')
  parsedResult.classList.add('d-none')
}

const removeLastItem = () => {
  input.value = input.value.slice(0, -1)
  divRef.removeChild(divRef.lastChild)
}

function parseResult(character) {
  const logicOperators = ['∧', '∨', '¬', '→', '↔', '↓', '|', '⊕']
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

const form = document.getElementById('form')
form.addEventListener('submit', (event) => {
  sessionStorage.setItem('condition', input.value)
})

if (conditionFromStorage !== null || conditionFromStorage !== '') {
  const splittedCondition = conditionFromStorage.split('')
  splittedCondition.forEach((character) => {
    addChar(character)
  })
}

if (resultArray.innerText !== '') {
  const slicedResultArray = resultArray.innerText.slice(1, -1)
  const splittedResultArray = slicedResultArray.split(',')
  splittedResultArray.forEach((split) => {
    split = split.replaceAll(`'`, '')
    const splittedString = split.split('')
    splittedString.forEach((character) => {
      parseResult(character)
    })
    const newLine = document.createElement('br')
    parsedResult.appendChild(newLine)
  })
  parsedResult.classList.remove('d-none')
}
