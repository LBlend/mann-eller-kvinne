const apiBaseUrl = process.env.REACT_APP_API_URL

export const predict = async (text, toggle) => {
  if (text.length > 50000) {
    document.body.style.backgroundColor = '#171520'
    return (
      {
        probability: {
          M: 0,
          F: 0
        }
      }
    )
  }

  const data = {
    text: text,
    clf: (toggle) ? 'rnn' : 'bayes'
  }
  const rawResponse = await fetch(`${apiBaseUrl}/mann-eller-kvinne`, { // eslint-disable-line no-undef
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  const response = await rawResponse.json()
  return response
}
