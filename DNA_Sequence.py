import tkinter as tk
from tkinter import messagebox

def calculate_gc_content(dna_sequence):
    """
    Calculate the GC content percentage in the DNA sequence.
    """
    if len(dna_sequence) == 0:
        return 0
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    return (gc_count / len(dna_sequence)) * 100

def reverse_complement(dna_sequence):
    """
    Generate the reverse complement of the DNA sequence.
    """
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    reversed_sequence = "".join(complement[base] for base in reversed(dna_sequence))
    return reversed_sequence

# Main Tkinter window setup
root = tk.Tk()
root.title("DNA Analyzer")
root.geometry("400x300")
root.resizable(False, False)

# Input label and entry for DNA sequence
tk.Label(root, text="Enter DNA Sequence:").pack(pady=10)
dna_entry = tk.Entry(root, width=50)
dna_entry.pack()

# Labels for displaying the results
gc_content_label = tk.Label(root, text="GC Content: ")
gc_content_label.pack(pady=10)

reverse_complement_label = tk.Label(root, text="Reverse Complement: ")
reverse_complement_label.pack(pady=10)

def analyze_dna():
    """
    Analyze the DNA sequence entered by the user.
    """
    dna_sequence = dna_entry.get().upper()
    
    # Input validation
    if not set(dna_sequence).issubset({"A", "T", "G", "C"}):
        messagebox.showerror("Invalid Input", "Please enter a valid DNA sequence (A, T, G, C only).")
        return

    # Calculate GC content and reverse complement
    gc_content = calculate_gc_content(dna_sequence)
    rev_complement = reverse_complement(dna_sequence)
    
    # Update labels with results
    gc_content_label.config(text=f"GC Content: {gc_content:.2f}%")
    reverse_complement_label.config(text=f"Reverse Complement: {rev_complement}")

# Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_dna)
analyze_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
