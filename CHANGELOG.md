# Changelog

## [4.1.0](https://github.com/LBlend/mann-eller-kvinne/compare/4.0.0...4.1.0) (2026-11-05)


### Features

* add dropout to reduce overfitting ([009f356](https://github.com/LBlend/mann-eller-kvinne/commit/009f356f23a8ce1f3c1151abba99323d9c976154))
* average LSTM outputs over the whole text ([e544efe](https://github.com/LBlend/mann-eller-kvinne/commit/e544efe19f293c570c8fb9859deecbca7a6ebf14))
* enlarge the vocab and cap the sequence length ([430fe55](https://github.com/LBlend/mann-eller-kvinne/commit/430fe553428c94c312a627ea6657cdccb9c27e21))
* use a smaller LSTM to reduce overfitting ([e4ec51f](https://github.com/LBlend/mann-eller-kvinne/commit/e4ec51f56d04bb4363068620eaa999910deddfb4))


### Bug Fixes

* always load RNN model with safe_mode on ([ba5d892](https://github.com/LBlend/mann-eller-kvinne/commit/ba5d89234e8de6c41bf2371f6e2593f25d0d344d))
* always read corpus as UTF-8 ([082d91b](https://github.com/LBlend/mann-eller-kvinne/commit/082d91bc1e8c88d2f68c792f447d66746bb29e44))
* check for the correct bayes model filenames ([9955697](https://github.com/LBlend/mann-eller-kvinne/commit/99556970eef3ac8bf2091a138dd08dad880d7578))
* create dir before saving bayes model ([8633bbc](https://github.com/LBlend/mann-eller-kvinne/commit/8633bbc28fd3a3ed2efdcfb0ba1eed7a1e24f614))
* don't run container as root ([054c700](https://github.com/LBlend/mann-eller-kvinne/commit/054c7004e355dfeab52ea4d96080322e61f2b429))
* don't wrap callback in tuple ([752c8de](https://github.com/LBlend/mann-eller-kvinne/commit/752c8de166a83078487669d6da2d64b726a13cea))
* ignore whitepsace around allowed origins entries ([099e518](https://github.com/LBlend/mann-eller-kvinne/commit/099e51892cb8d48a3ce6dd51529d50b27b9500e1))
* keep .env and .git out of the docker build ([ac09e39](https://github.com/LBlend/mann-eller-kvinne/commit/ac09e3915517aa36f0d2a4e089f5121a32696d6c))
* keep each corpus class in own direcotry ([41f07a2](https://github.com/LBlend/mann-eller-kvinne/commit/41f07a216025fc89cf50c029e79a1f0764d51c92))
* keep the best weights when stopping early ([f36ea7c](https://github.com/LBlend/mann-eller-kvinne/commit/f36ea7c9fc92bafe995ff676f37941a591de69da))
* load models with relative paths instead of working dir ([b936537](https://github.com/LBlend/mann-eller-kvinne/commit/b936537ce3e50de50455ee6f10189a49097095c6))
* load settings from .env correctly ([3023ea9](https://github.com/LBlend/mann-eller-kvinne/commit/3023ea9f1ffc9db57afd3c3a378bd106ae253abb))
* only allow content-type header in CORS requests ([57fab7f](https://github.com/LBlend/mann-eller-kvinne/commit/57fab7f159ebe5ac88ec3e90685f871e2702b395))
* pass text to RNN as non-np array ([cae3f77](https://github.com/LBlend/mann-eller-kvinne/commit/cae3f77daa160ff6d8c4dfb498ec9e2a6e71f6c4))
* raise learning rate to 1e-3 ([aff3572](https://github.com/LBlend/mann-eller-kvinne/commit/aff35722886dc8e42184b383d2303641a0b7dba2))
* register corpus classes only once ([9af02ed](https://github.com/LBlend/mann-eller-kvinne/commit/9af02edd53fb99c07b6690866a569d253bc45cc9))
* stop build on error ([e0dc552](https://github.com/LBlend/mann-eller-kvinne/commit/e0dc5525f74a552a08c8c26c4abf23004302954a))
* stop falling back to bayes ([6aa7dd1](https://github.com/LBlend/mann-eller-kvinne/commit/6aa7dd19aeec0aff934b9ffbac3f1b9ea7a4b885))
* stop surpressing all python warnings ([d493d32](https://github.com/LBlend/mann-eller-kvinne/commit/d493d32a9e1843550021d2c1b64d8d2d4934cedf))
* update validation script for keras 3 ([2b76390](https://github.com/LBlend/mann-eller-kvinne/commit/2b763900b61537aca6c8778d17c3d5eed759b1a2))
* upgrade all dependencies to their latest versions ([a2db4f0](https://github.com/LBlend/mann-eller-kvinne/commit/a2db4f0dacce4498cd29c6747428378c4fcb8dc5))
* use yaml.safe_load ([f328624](https://github.com/LBlend/mann-eller-kvinne/commit/f328624fd19b26dbe889320b34974431d30c3b06))
