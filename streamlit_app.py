import streamlit as st
from code_editor import code_editor

from editor_config import ACE_STYLE, BUTTONS, INFO_BAR

if not "code" in st.session_state:
    st.session_state.code = "st.write('Hello, world!')"


with st.sidebar:
    run_on_change = st.toggle("Run code on change", value=True)
    if not run_on_change:
        with st.container(border=True):
            st.markdown("Manual run: `Ctrl + Enter` or `⌘ + Enter`")

    response_dict = code_editor(
        st.session_state.code,
        height=[10, 2000], # type: ignore
        key="code_editor",
        lang="python",
        options={
            "wrap": True,
            "showLineNumbers": True,
        },
        props={
            "tabSize": 2,
            "style": ACE_STYLE,
            # "readOnly": True,
        },
        response_mode="debounce",
        focus=True,
        buttons=BUTTONS,
        info=INFO_BAR,
    )


if (
    response_dict["type"] == "change"
    and run_on_change
    or response_dict["type"] == "submit"
):
    st.session_state.code = response_dict["text"]

exec(st.session_state.code)
