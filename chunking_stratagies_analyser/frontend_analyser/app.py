import streamlit as st
import requests

st.set_page_config(page_title="Chunking Visualizer")

st.title("📄 Chunking Visualizer")

uploaded_file_list = st.file_uploader(
    "Upload File",
    type=["pdf", "csv", "xlsx", "xls", "docx", "txt"],
    accept_multiple_files=True
)


text=""
for uploaded_file in uploaded_file_list:
    if uploaded_file:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/file",
                files={"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)},
            )
            response.raise_for_status()
            text+= response.json().get("text", "")
        except Exception as e:
            st.error(f"Error extracting text: {e}")

text+= st.text_area(
            "Enter Text",
            height=200
        )

selected = st.radio(
    "Select Chunking Strategies",
    [
        "Fixed Size",
        "Fixed Size + Overlap",
        "Sentence Based",
        "Recursive",
        "Semantic"
    ]
)

if selected:

    st.divider()
    st.subheader(selected)

    payload = {
        "text": text,
        "strategy": selected
    }

    if selected == "Fixed Size":

        chunk_size = st.number_input(
            "Chunk Size",
            min_value=1,
            value=100,
            key="fixed_size"
        )

        payload["chunk_size"] = chunk_size

    elif selected == "Fixed Size + Overlap":

        chunk_size = st.number_input(
            "Chunk Size",
            min_value=1,
            value=100,
            key="overlap_chunk"
        )

        overlap_size = st.number_input(
            "Overlap Size",
            min_value=0,
            value=20,
            key="overlap_size"
        )

        payload["chunk_size"] = chunk_size
        payload["overlap_size"] = overlap_size

    elif selected == "Sentence Based":

        sentences_per_chunk = st.number_input(
            "Sentences Per Chunk",
            min_value=1,
            value=2,
            key="sentence_size"
        )

        payload["chunk_size"] = sentences_per_chunk

    if st.button(
        f"Generate {selected} Chunks",
        key=f"btn_{selected}"
    ):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/chunk",
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                chunks = data["chunks"]

                st.success(
                    f"Generated {len(chunks)} chunks"
                )

                for i, chunk in enumerate(chunks, start=1):
 
                    with st.expander(f"Chunk {i}"):
                        # response = requests.post(
                        #         "http://127.0.0.1:8000/tokenize",
                        #         json={"text": chunk},
                        #         timeout=60
                        #     )
                        # st.write(response.json().get("tokens", []))
                        st.write(chunk)

                


        except requests.exceptions.Timeout:
            st.error(
                "Request timed out. "
                "Please try again later."
            )
        except requests.exceptions.ConnectionError:

            st.error(
                "Cannot connect to backend. "
                "Make sure FastAPI is running."
            )

        except Exception as e:

            st.error(str(e))
            