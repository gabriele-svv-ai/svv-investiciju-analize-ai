import gradio as gr
from service.analysis_svv import analyze_svv_project

def run_analysis(initial_investment, cash_flows_text, discount_rate):
    # Convert text input "12000,15000,18000" → [12000, 15000, 18000]
    cash_flows = [float(x.strip()) for x in cash_flows_text.split(",")]

    result = analyze_svv_project(
        initial_investment=float(initial_investment),
        yearly_cash_flows=cash_flows,
        discount_rate=float(discount_rate)
    )

    return result

ui = gr.Interface(
    fn=run_analysis,
    inputs=[
        gr.Number(label="Pradinė investicija (pvz. -50000)"),
        gr.Textbox(label="Metiniai pinigų srautai (pvz. 12000,15000,18000)"),
        gr.Number(label="Diskonto norma (pvz. 0.1)")
    ],
    outputs="json",
    title="SVV Investicijų Analizė",
    description="NPV, IRR, Payback ir Monte Carlo rizikos analizė"
)

if __name__ == "__main__":
    ui.launch(share=True)
