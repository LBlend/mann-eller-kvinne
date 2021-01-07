const api_base_url = "https://genderapi.lblend.moe"
// const api_base_url = "http://127.0.0.1:5000"

export const predict = async (text) => {
  if (text.length > 5000) {
    document.body.style.backgroundColor = '#171520';
    return (
      {
        probability: {
          'M': 0,
          'F': 0
        },
      }
    )
  }

  let data = {
    text: text,
    clf: 'bayes'
    // clf: 'rnn'
  }
  console.log(data)
  const rawResponse = await fetch(`${api_base_url}/mann-eller-kvinne`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  });
  const response = await rawResponse.json();
  return response;
}
