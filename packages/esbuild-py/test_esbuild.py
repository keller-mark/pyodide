from pytest_pyodide import run_in_pyodide

@run_in_pyodide(packages=["esbuild_py"])
def test_jsx(selenium):
    from esbuild_py import transform

    jsx = """
import * as React from 'react'
import * as ReactDOM from 'react-dom'

ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
    """
    expected = """
import * as React from "react";
import * as ReactDOM from "react-dom";
ReactDOM.render(
  /* @__PURE__ */ React.createElement("h1", null, "Hello, world!"),
  document.getElementById("root")
);
    """
    assert transform(jsx).strip() == expected.strip()

