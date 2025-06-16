import os
import pptx
import comtypes.client

def slide_generation(arr):
    # Load template
    presentation = pptx.Presentation(os.path.join("powerpoints", "input.pptx"))

    def update_text_of_textbox(presentation, slide, text_box_id, new_text):
        slide = presentation.slides[(slide - 1)]
        count = 0
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text:
                count += 1
                if count == text_box_id:
                    text_frame = shape.text_frame
                    first_paragraph = text_frame.paragraphs[0]
                    first_run = first_paragraph.runs[0] if first_paragraph.runs else first_paragraph.add_run()

                    # Preserve formatting
                    font = first_run.font
                    font_name, font_size = font.name, font.size
                    font_bold, font_italic = font.bold, font.italic
                    font_underline, font_color = font.underline, font.color.rgb

                    # Clear and set new text
                    text_frame.clear()
                    new_run = text_frame.paragraphs[0].add_run()
                    new_run.text = new_text

                    # Reapply formatting
                    new_run.font.name = font_name
                    new_run.font.size = font_size
                    new_run.font.bold = font_bold
                    new_run.font.italic = font_italic
                    new_run.font.underline = font_underline
                    new_run.font.color.rgb = font_color
                    return

    # Slide 1
    update_text_of_textbox(presentation, 1, 1, arr[0][0])
    update_text_of_textbox(presentation, 1, 3, arr[0][1])

    # Slide 2–9
    for slide in range(2, 10):
        for text_box_id in range(3, 5):
            update_text_of_textbox(presentation, slide, text_box_id, arr[slide - 1][text_box_id - 3])

    # Save presentation
    pptx_path = os.path.join("powerpoints", "generated_presentation.pptx")
    presentation.save(pptx_path)
    print(f"✅ Presentation saved at: {pptx_path}")

    # Convert to PDF
    def convert_pptx_to_pdf(pptx_path, pdf_path):
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        deck = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
        deck.SaveAs(pdf_path, 32)  # 32 = PDF
        deck.Close()
        powerpoint.Quit()

    convert_pptx_to_pdf(pptx_path, "pdf_folder/output_pdf.pdf")
