import streamlit as st
import math
from math import sin, cos, tan, pi
from PIL import Image

# making functions for add sub mul and div

def addition(num1, num2):
  return num1 + num2
def subtraction(num1, num2):
  return num1 - num2
def multiplication(num1, num2):
  return num1 * num2
def division(num1, num2):
  return num1 / num2


def main(): 
  
  st.title("Calculator")
  st.sidebar.write("***A short clip:***")
  video_file = open('video.mp4', 'rb')
  video_bytes = video_file.read()

  st.sidebar.video(video_bytes)

  
  

  
  st.subheader("**This is a simple calculator app**")
  
  img = Image.open("pic.png")
  st.image(img)

  num1 = st.number_input("Enter first number")
  num2= st.number_input("Enter second number")

  operation = st.selectbox("**Select the Operation you want to perform**", ["Add", "Subtract", "Multiply", "Divide"])

  tri_num = st.number_input("Enter a number for trig")
  operation1 = st.selectbox("**Select Operation against which you want to know the value**", ["Sin", "Cos", "Tan"])

  
  if operation == "Add":
    st.write("**The value of addition between** ",num1,"and",num2,"is :",addition(num1, num2))
  elif operation == "Subtract":
    st.write("**The value of subtraction between** ",num1,"and",num2,"is :",subtraction(num1, num2))
  elif operation == "Multiply":
    st.write("**The value of multiplication between** ",num1,"and",num2,"is :",multiplication(num1, num2))
  elif operation == "Divide":
    st.write("**The value of division between** ",num1,"and",num2,"is :",division(num1, num2))


  if operation1== "Sin":
    st.write("**The converted value from degree to radian is :**",math.sin(math.radians(tri_num))," ","**and The converted value from radian to degree is :**",math.sin(math.degrees(tri_num)))
  elif operation1 == "Cos":
    st.write("**The converted value from degree to radian is :**",math.sin(math.radians(tri_num))," ","**and The converted value from radian to degree is :**",math.cos(math.degrees(tri_num)))
  elif operation1 == "Tan":
    st.write("**The converted value from degree to radian is :**",math.sin(math.radians(tri_num))," ","**and The converted value from radian to degree is :**",math.tan(math.degrees(tri_num)))



if __name__ == '__main__':
  main()


