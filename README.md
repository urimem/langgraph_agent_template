# LangGraph Agent Template

A template project demonstrating how to build a sequential agent workflow using LangGraph and LangChain.

## Overview

This project implements a multi-step agent workflow using LangGraph's `StateGraph`. The agent processes input through three distinct stages:

1. Initial processing (`initial_step`)
2. LLM-based processing (`model_call`)
3. Final output generation (`final_step`)

## Project Structure

- `_agent_graph.py`: Main implementation file containing the agent workflow
- `README.md`: This documentation file

## Key Components

### State Management

The project uses TypedDict classes for strict type checking across different stages:

- `InputState`: Handles initial input parameters
  - `agent_input_a`: First input parameter
  - `agent_input_b`: Second input parameter

- `OverallState`: Manages intermediate state during processing
  - `temp_value_a`: Temporary string value
  - `temp_value_b`: List of temporary string values

- `OutputState`: Defines the final output format
  - `agent_output_value`: Final processed result

### Processing Steps

1. **Initial Step**: Performs preliminary processing on input data
2. **Model Call**: Integrates with GPT-4 for advanced processing
   - Uses a custom prompt from LangChain Hub
   - Implements structured output parsing using Pydantic
3. **Final Step**: Transforms processed data into the required output format

## Dependencies

- LangChain
- LangGraph
- OpenAI
- Pydantic

## Client & SDK usage

main.py demonstrates the use of LangGraph python SDK to call the Agent hosted in LangGraph cloud.