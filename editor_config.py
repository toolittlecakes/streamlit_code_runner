INFO_BAR_CSS = """
# background-color: #bee1e5;
background-color: lightgrey;

body > #root .ace-streamlit-dark~& {
   background-color: #262830;
}

.ace-streamlit-dark~& span {
   color: #fff;
   opacity: 0.6;
}

span {
   color: #000;
   opacity: 0.5;
}

.code_editor-info.message {
   width: inherit;
   margin-right: 75px;
   order: 2;
   text-align: center;
   opacity: 0;
   transition: opacity 0.7s ease-out;
}

.code_editor-info.message.show {
   opacity: 0.6;
}

.ace-streamlit-dark~& .code_editor-info.message.show {
   opacity: 0.5;
}
"""

INFO_BAR = {
    "name": "language info",
    "css": INFO_BAR_CSS,
    "style": {
        "order": "1",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "width": "100%",
        "height": "2.5rem",
        "padding": "0rem 0.75rem",
        "borderRadius": "8px 8px 0px 0px",
        "zIndex": "9993",
    },
    "info": [{"name": "python", "style": {"width": "100px"}}],
}

BUTTONS = [
    {
        "name": "copy",
        "feather": "Copy",
        "hasText": True,
        "alwaysOn": True,
        "commands": [
            "copyAll",
            [
                "infoMessage",
                {
                    "text": "Copied to clipboard!",
                    "timeout": 2500,
                    "classToggle": "show",
                },
            ],
        ],
        "style": {"top": "0rem", "right": "0.4rem"},
    },
    {
        "name": "Run",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "showWithText": False,
        "alwaysOn": True,
        "commands": ["submit"],
        "style": {"bottom": "0rem", "right": "0.4rem"},
    },
]

# Needed to remove the border radius from the top of the editor where it connects to the info bar 🤡
ACE_STYLE = {"borderRadius": "0px 0px 8px 8px"}
