import gradio as gr
from summarizer import Summarizer
import torch


def summarize_text(text):
    model = Summarizer()
    return model(text)
    # return('Test working')

inputs = gr.inputs.Textbox(lines=10, placeholder="Paste Text Here...")
output_text = gr.outputs.Textbox()

iface = gr.Interface(
  fn=summarize_text,
  inputs= inputs,
  outputs= output_text)

iface.launch()
