import streamlit as st
from code_editor import code_editor

with st.sidebar:
    run_on_change = st.toggle("Run code on change", value=True)
    response_dict = code_editor(
        "st.write('Hello, world!')",
        height=[10, 2000],
        key="code",
        lang="python",
        options={
            "wrap": True,
            "showLineNumbers": True,
            # "displayIndentGuides": True,
            # "foldStyle": "markbegin",
            # "foldStyle": "markbeginend",
        },
        props={
            "tabSize": 2,
            # "focus": True,
            # "showPrintMargin": True,
            # "showGutter": False,
            # "readOnly": True,
            # "enableBasicAutocompletion": True,
        },
        response_mode="debounce",
        # response_mode=["debounce", "blur"],
    )

if (
    response_dict["type"] == "change"
    and run_on_change
    or response_dict["type"] == "submit"
):
    exec(response_dict["text"])
