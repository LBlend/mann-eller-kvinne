const api_base_url = "https://api.mann-eller-kvinne.no"

export const predict = async (text) => {
  if (text.length > 5000) {
    document.body.style.backgroundColor = '#171520';
    return (
      {
        prediction: {
          norwegian: 'som skriver for lange tekster'
        },
        likelyhood: {
          simple: {
            man: '0%',
            woman: '0%'
          }
        }
      }
    )
  }
  let data = {text: text}
  console.log(data)
  const rawResponse = await fetch(`${api_base_url}/mann-eller-kvinne`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  });
  let response = await rawResponse.json();
  return response;
}
