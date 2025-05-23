# Runnables in LangChain

This repository provides illustrative examples of using LangChain Runnables, a powerful abstraction for building modular and composable AI workflows. Each script demonstrates a specific Runnable component, showcasing how to construct flexible and maintainable pipelines for language model applications.

## 📁 Repository Structure

### 1-Runnable_Sequence.py
Demonstrates RunnableSequence, enabling the chaining of multiple Runnables to form a sequential pipeline.

### 2-RunnableParallel.py
Showcases RunnableParallel, allowing concurrent execution of multiple Runnables for parallel processing.

### 3-RunnablePassthrough.py
Illustrates RunnablePassthrough, which passes inputs directly to outputs without modification—useful for debugging or pipeline placeholders.

### 4-RunnableLambda.py
Utilizes RunnableLambda to wrap simple functions as Runnables, facilitating quick integration of custom logic.

### 5-RunnableBranch.py
Explores RunnableBranch, enabling conditional branching within pipelines based on input criteria.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher

### Install dependencies:

```bash
pip install langchain
```

### Running Examples
Execute any of the example scripts directly:

```bash
python 1-Runnable_Sequence.py
```

Replace the filename with the desired script to explore different Runnable components.

## 📚 Learn More

- [LangChain Runnables Documentation](https://python.langchain.com/docs/expression_language/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for enhancements or additional examples.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

For any questions or discussions, please open an issue in the repository.
