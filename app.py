import gradio as gr

def process(pdf):
    return "Processing..."

demo = gr.Interface(
    fn=process,
    inputs="file",
    outputs="text"
)

demo.launch()
