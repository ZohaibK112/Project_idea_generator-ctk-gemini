import os
from urllib import response
import customtkinter as ctk
import google.generativeai as genai

genai.configure(api_key="Your API")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 200,  # Limiting to 200 tokens for ideas
}


def generate():
    prompt="Please generate 1 ideas for coding projects "
    language=language_dropdown.get()
    prompt+= "The programming Language is " + language + "."

    difficulty=difficulty_value.get()
    prompt+= "The difficulty is " + difficulty + "."

    if checkbox1.get():
        prompt+= "The project should include an Database" 
    if checkbox2.get():
        prompt+= "The project should include a API" 

    print(prompt)

    try:
            # Instantiate the GenerativeModel
            model = genai.GenerativeModel("gemini-1.5-PRO")  # Adjust the model name if necessary

            # Generate content based on the prompt
            response = model.generate_content(prompt)

            if response and hasattr(response, 'text'):
                result.delete("1.0", "end")  # Clear previous results
                result.insert("1.0", response.text)  # Display the generated ideas
            else:
                result.delete("1.0", "end")
                result.insert("1.0", "No ideas were generated. Please try again.")

    except Exception as e:
            result.delete("1.0", "end")
            result.insert("1.0", f"Error occurred: {e}")

def maximize_output():
    result.pack_forget()  # Hide the current textbox
    result.pack(pady=10, fill="both", expand=True) 

root = ctk.CTk()
root.geometry("750x550")
root.title("Gemini Pro")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="Gemini Pro",
                           font=ctk.CTkFont(size=30, weight="bold"))
                            
title_label.pack(padx=10, pady=(40,20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100,pady=(20,5), fill="both")
language_label = ctk.CTkLabel(
    language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold")
)
language_label.pack()

language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Python", "Java", "C++", "JavaScript" , "Golang"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100,pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Poject Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy" , variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20,10) , pady=10)

radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium" , variable=difficulty_value, value="Medium")
radiobutton1.pack(side="left", padx=10 , pady=10)

radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard" , variable=difficulty_value, value="Hard")
radiobutton1.pack(side="left", padx=10 , pady=10)


features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100,pady=5, fill="both")
features_label = ctk.CTkLabel(
  features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left",padx=50, pady=10) 
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left",padx=50, pady=10) 

button= ctk.CTkButton(frame, text="Generate Ideas", command=generate)
button.pack(padx=100, fill="x" , pady=(5,20))

maximize_button = ctk.CTkButton(frame, text="Maximize Output", command=maximize_output)
maximize_button.pack(padx=100, fill="x", pady=(5,20))

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10 , fill="x", padx=100)

root.mainloop()