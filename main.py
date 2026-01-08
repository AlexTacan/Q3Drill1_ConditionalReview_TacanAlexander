from pyscript import document, display

def average_compute(e): #define function average_compute to get the average
    num1 = float(document.getElementById("input").value)
    num2 = float(document.getElementById("input2").value)

    result = num1 + num2 

    result2 = result / 2

    
    if result2 >= 75:
        message = f"Your average is: {result2:.2f}"
        passing = " - You passed!"

    else:
        message = f"Your average is: {result2:.2f}"
        passing = " - You failed."

    
    display(message, target="average")
    display(passing, target="pass")


