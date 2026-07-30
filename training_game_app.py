# Artistofall Producxionz - Visual Training & Onboarding App (Flet UI)
import flet as ft

def main(page: ft.Page):
    page.title = "Artistofall Producxionz: Training Terminal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.window_width = 500
    page.window_height = 700

    # Question Database
    questions = [
        {
            "q": "What is the primary operational priority when handling studio equipment?",
            "options": ["A) Leave gear scattered", "B) Ensure items are secure, logged, and verified", "C) Pack everything away without checking", "D) Disassemble camera lenses"],
            "answer": "B"
        },
        {
            "q": "In studio business models, what do TFP (Time-for-Print) and B2B (Business-to-Business) represent?",
            "options": [
                "A) Time-for-Print (portfolio trade) and Business-to-Business (commercial clients)",
                "B) Technical File Processing and Brand-to-Buyer marketing",
                "C) Terminal Function Protocol and Backup-to-Base routing",
                "D) Total Frame Production and Billing-to-Budget tracking"
            ],
            "answer": "A"
        },
        {
            "q": "Which standard lighting setup uses a key light, fill light, and back light to create dimension?",
            "options": ["A) Flat ring lighting", "B) Three-point lighting", "C) Natural ambient bouncing", "D) Direct flash isolation"],
            "answer": "B"
        },
        {
            "q": "Which camera setting and lens choice primarily controls a shallow depth of field (bokeh)?",
            "options": ["A) Fast shutter speed", "B) High ISO sensitivity", "C) Wide aperture (low f-stop number)", "D) High resolution recording"],
            "answer": "C"
        }
    ]

    current_index = [0]
    score = [0]

    # UI Elements
    title_text = ft.Text("ARTISTOFALL PRODUCXIONZ", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.LIGHT_BLUE_ACCENT)
    progress_text = ft.Text(f"Question 1 of {len(questions)}", size=14, color=ft.Colors.WHITE70)
    question_text = ft.Text(questions[0]["q"], size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
    feedback_text = ft.Text("", size=14, weight=ft.FontWeight.BOLD)

    options_column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)

    def check_answer(selected_option):
        correct_letter = questions[current_index[0]]["answer"]
        if selected_option.startswith(correct_letter):
            score[0] += 1
            feedback_text.value = "✓ Correct! Asset verified and secured."
            feedback_text.color = ft.Colors.GREEN_ACCENT
        else:
            feedback_text.value = f"✗ Incorrect. The correct answer was {correct_letter}."
            feedback_text.color = ft.Colors.RED_ACCENT

        current_index[0] += 1
        
        if current_index[0] < len(questions):
            load_question()
        else:
            show_results()
        page.update()

    def load_question():
        q_data = questions[current_index[0]]
        progress_text.value = f"Question {current_index[0] + 1} of {len(questions)}"
        question_text.value = q_data["q"]
        
        options_column.controls.clear()
        for opt in q_data["options"]:
            btn = ft.ElevatedButton(
                opt,
                width=420,
                on_click=lambda e, o=opt: check_answer(o)
            )
            options_column.controls.append(btn)

    def show_results():
        percentage = (score[0] / len(questions)) * 100
        progress_text.value = "Training Complete!"
        question_text.value = f"Final Score: {score[0]} / {len(questions)} ({percentage:.1f}%)"
        options_column.controls.clear()
        
        if percentage == 100:
            status = "Status: MASTERED. Ready for full deployment!"
        elif percentage >= 70:
            status = "Status: APPROVED. Solid understanding."
        else:
            status = "Status: REQUIRES RE-TRAINING."
            
        feedback_text.value = status
        feedback_text.color = ft.Colors.YELLOW_ACCENT

    load_question()

    # Main Container Layout with dark blue-grey background for high contrast
    card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                title_text,
                progress_text,
                ft.Divider(),
                question_text,
                ft.Container(height=10),
                options_column,
                feedback_text
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=25,
            width=460,
            bgcolor=ft.Colors.BLUE_GREY_800,  # Fixed: Added dark container background for contrast
            border_radius=10,
        )
    )

    page.add(card)

ft.app(target=main)