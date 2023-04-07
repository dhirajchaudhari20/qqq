import streamlit as st
import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

gr_interface = gr.Interface(fn=greet, inputs="text", outputs="text")

def main():
    st.set_page_config(page_title="Gradio in Streamlit", page_icon=":guardsman:")
    st.title("Gradio in Streamlit Demo")
    st.write("This is an example of embedding a Gradio interface within a Streamlit app.")
    st.write("Enter your name below to be greeted.")
    name = st.text_input("Name:")
    if name:
        result = gr_interface.process([name])
        st.write(result)

if __name__ == "__main__":
    main()
