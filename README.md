# Qwen-code-30b Testing Repository

## Note from the author

Hi there. I'm using Jetbrains AI Chat and Junie, with cloud model.
But i want to test local model as well. I picked this model because it's a MoE.
Let's see how it goes.

- The IDE (Pycharm) is a running on a Mac.
- The Ollama server is a small Beelink server running a Ryzen7 6800U that i bought for 380e on Amazon.
- I configured the BIOS to allocate 16GB as VRAM, out of the 32GGB of UMA Ram.
- As for now the context size is set to 20k token.
- It use all the VRAM + 3GB of GTT.

~~I'll make it simple. Each test is in its own numbered (by chronological order) directory.~~
No idea what i'll code yet. But generating it will be slow :)

I'm in "offline mode" (for the AI) to make sure that it doesn't access the cloud.
Jetbrains plugin have a tendency to switch to "Auto" from time to time (Auto = latest version of cloude based Claude)

That's it. for now.

## Problems found so far

- Offline mode make the jetbrains plugin tricky to use
- The jetbrains plugin keep reverting back to "auto" (cloud based Claude) after every prompt
- Despite providing 001/main.py as a context, the model keep creating a /main.py, which is the wrong file. Worse, sometimes it try to patch it (even when it doesn't exist)
- Not sure if this is a plugin issue or a model issue.

## i'm stuck

- The fact that it can't edit the right file is a critical issue. I'm kind of stuck here :(
- okay, if i create the file myself (eg 002/main.py) i can work around the problem. I'll make do with it. I need to give it specific instruction as well to make sure it work on the right file
- i removed the directory based structure to see if it's better

## switching to vscode

- It is sad, but jetbrains ai assistant have trouble giving proper instruction to anything but claude.
- or the models fail to understand the instructions. doesn't matter
- I switched to vscode (that i dislike) and continue.dev. i have less interaction issue beetween the plugin and the model

----

## Anything below is AI generated

This repository is dedicated to testing the capabilities of the Qwen-code-30b model as a local coding assistant within JetBrains IDEs using the JetBrains AI Chat feature.

## Purpose

The main goal of this repository is to experiment with and evaluate how well the Qwen-code-30b language model performs when used locally for various programming tasks within the JetBrains ecosystem. This includes testing code generation, debugging assistance, code completion, and other AI-powered coding features.

## Model Used

- **Model**: Qwen-code-30b (a large language model specialized for code understanding and generation)
- **Usage**: Local model deployment for offline coding assistance
- **Integration**: JetBrains AI Chat for IDE integration

## Features Being Tested

- Code generation from natural language descriptions
- refactoring suggestions
- Debugging assistance and error explanation
- Code documentation generation

## Contributing

Feel free to explore, test, and provide feedback on how well the model performs with different coding tasks.
