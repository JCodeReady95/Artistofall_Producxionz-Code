# Artistofall Producxionz - Continuous Learning & Onboarding Trivia Game
import time

def run_quiz():
    print("="*60)
    print("  ARTISTOFALL PRODUCXIONZ: CONTINUOUS LEARNING TERMINAL")
    print("  Staff, Assistant & Intern Training Module v1.3")
    print("="*60)
    
    # Modular Question Database grouped by department / skill level
    training_modules = {
        "Level 1: Studio Operations & Business Standards": [
            {
                "question": "What is the primary operational priority when handling studio equipment?",
                "options": ["A) Leave gear scattered", "B) Ensure items are secure, logged, and verified", "C) Pack everything away without checking", "D) Disassemble camera lenses"],
                "answer": "B"
            },
            {
                "question": "In studio business models, what do TFP (Time-for-Print) and B2B (Business-to-Business) represent?",
                "options": [
                    "A) Time-for-Print (portfolio trade) and Business-to-Business (commercial clients)",
                    "B) Technical File Processing and Brand-to-Buyer marketing",
                    "C) Terminal Function Protocol and Backup-to-Base routing",
                    "D) Total Frame Production and Billing-to-Budget tracking"
                ],
                "answer": "A"
            }
        ],
        "Level 2: Lighting & Depth of Field Standards": [
            {
                "question": "Which standard lighting setup uses a key light, fill light, and back light to create dimension and separate a subject from the background?",
                "options": ["A) Flat ring lighting", "B) Three-point lighting", "C) Natural ambient bouncing", "D) Direct flash isolation"],
                "answer": "B"
            },
            {
                "question": "Which camera setting and lens choice primarily controls a shallow depth of field to produce a blurred, artistic background (bokeh)?",
                "options": ["A) Fast shutter speed", "B) High ISO sensitivity", "C) Wide aperture (low f-stop number)", "D) High resolution recording"],
                "answer": "C"
            }
        ],
        "Level 3: Camera Mechanics & Media Standards": [
            {
                "question": "Which camera setting controls motion blur and how long the camera's sensor is exposed to light?",
                "options": ["A) Aperture", "B) Shutter Speed", "C) ISO", "D) White Balance"],
                "answer": "B"
            },
            {
                "question": "What does a standard frame rate of 24fps represent in professional cinematic media?",
                "options": ["A) Cinematic motion standard", "B) Audio frequency", "C) Storage capacity", "D) Resolution size"],
                "answer": "A"
            }
        ]
    }

    score = 0
    total_questions = 0

    # Loop through each module level using nested loops and dictionary iteration
    for module_name, questions in training_modules.items():
        print(f"\n--- Entering {module_name} ---")
        time.sleep(0.3)
        
        for q in questions:
            total_questions += 1
            print(f"\nQ{total_questions}: {q['question']}")
            for opt in q['options']:
                print(f"  {opt}")
            
            # Capture user input and normalize it to uppercase
            user_answer = input("Your Answer (A/B/C/D): ").strip().upper()
            
            if user_answer == q['answer']:
                print("✓ Correct! Asset verified and secured.")
                score += 1
            else:
                print(f"✗ Incorrect. The correct answer was {q['answer']}. Review module logs.")
        
        print("-" * 40)

    # Final Diagnostic Report & Performance Evaluation
    print("\n" + "="*60)
    print("  STUDIO TRAINING DIAGNOSTIC REPORT")
    print("="*60)
    print(f"  Candidate Final Score: {score} / {total_questions}")
    
    percentage = (score / total_questions) * 100
    print(f"  Proficiency Rating: {percentage:.1f}%")
    
    if percentage == 100:
        print("  Status: MASTERED. Ready for full studio deployment!")
    elif percentage >= 70:
        print("  Status: APPROVED. Solid understanding with minor review needed.")
    else:
        print("  Status: REQUIRES RE-TRAINING. Please review company documentation.")
    print("="*60)

if __name__ == "__main__":
    run_quiz()