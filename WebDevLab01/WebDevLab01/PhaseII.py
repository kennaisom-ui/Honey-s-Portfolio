'''Test: Which Type of Dog Are You?
Choices: Mutt, Poodle/Poodle mix, Golden Retriever, Husky
Beagle, Daschund, Bulldog, Wait a minute...YOU'RE A CAT!

1. What is your favorite drink?: Good ol Water, Hot Tea, Boba, Juice, Soda, Milk (cause I'm a freak)
2. What do you like to do in your freetime?: Excercise, Read, Sleep, Cook, Watch Nature Documentaries,
Spend time with Friends
3. On a scale from 1-10, how extroverted are you (0 is very introverted, 10 is very extroverted):
4. What is your favorite color (out of the ones dogs can see)?: Red, Yellow, Blue, Grey, Black
5. How many pets do you have? '''

import streamlit as st

def title_info():
    st.title("Which Type of Dog Are You?")
    st.write("Find out which breed of dog matches your personality best!")

def starting_scores():
    if 'score' not in st.session_state:
        st.session_state.score ={
            "Mutt":0,
            "Poodle/Doodle":0,
            "Golden Retriever":0,
            "Husky":0,
            "Beagle":0,
            "Daschund":0,
            "Bulldog":0,
            "AN IMPOSTER!...YOU'RE A CAT!":0
        }

#Multiple Choice #NEW
def question1():
    st.subheader("Question 1")
    q1= st.radio(
        "What is your favorite drink?",
        ["Good ol Water", "Hot Tea","Boba","Coffee","Juice", "Soda", "Milk (cause I'm a freak)"]
    )#NEW

    st.subheader("Question 2")
    q2 = st.multiselect(
        "What do you like to do in your freetime?",
        ["Exercise", "Read", "Sleep", "Cook/Bake", "Watch Nature Documentaries", "Spend time with Friends"]
    )#NEW

    st.subheader("Question 3")
    q3 = st.slider(
        "On a scale from 1-10, how extroverted are you? (1 is very introverted, 10 is very extroverted)",
        min_value=1, max_value=10, value=5
    ) #NEW
    st.subheader("Question 4")
    q4 = st.selectbox(
        "What is your favorite color (out of the ones dogs can see?)",
        ["Yellow", "Blue", "Grey", "Black"]
    ) #NEW

    st.subheader("Question 5")
    q5 = st.number_input(
        "How many pets do you have?",
        min_value=0, value=0, step=1
    ) #NEW

    return q1,q2,q3,q4,q5

'''Calculate Final Scores'''

def calc_scores(q1,q2,q3,q4,q5):
    #Q1
    st.session_state.scores= {breed: 0 for breed in st.session_state.score}
    if q1 == "Good ol Water":
        st.session_state.score["Mutt"] +=2
    elif q1 == "Hot Tea":
        st.session_state.score["Poodle/Doodle"] +=2
    elif q1 == "Boba":
        st.session_state.score["Daschund"] +=2
    elif q1 == "Coffee":
        st.session_state.score["Golden Retriever"] +=2
    elif q1 == "Juice":
        st.session_state.score["Husky"] +=2
    elif q1 == "Soda":
        st.session_state.score["Bulldog"] +=2
    elif q1 == "Milk (cause I'm a freak)":
        st.session_state.score["AN IMPOSTER!...YOU'RE A CAT!"] +=2
    #Q2
    if "Exercise" in q2:
        st.session_state.score["Golden Retriever"] += 2
        st.session_state.score["Husky"] += 3
    if "Read" in q2:
        st.session_state.score["Poodle/Doodle"] += 3
        st.session_state.score["Daschund"] += 2
        st.session_state.score["Bulldog"] += 1
    if "Sleep" in q2:
        st.session_state.score["Poodle/Doodle"] += 1
        st.session_state.score["AN IMPOSTER!...YOU'RE A CAT!"] += 2
        st.session_state.score["Bulldog"] += 1
    if "Cook/Bake" in q2:
        st.session_state.score["Daschund"] += 2
        st.session_state.score["Poodle/Doodle"] += 1
    if "Watch Nature Documentaries" in q2:
        st.session_state.score["Mutt"] += 2
        st.session_state.score["Golden Retriever"] += 1
    if "Spend time with Friends" in q2:
         st.session_state.score["Mutt"] += 2
         st.session_state.score["Golden Retriever"] += 1

    #Q3
    if q3==1 or q3==2:
        st.session_state.score["AN IMPOSTER!...YOU'RE A CAT!"] += 2
    elif q3 >= 7:
        st.session_state.score["Golden Retriever"] += 3
        st.session_state.score["Mutt"] += 2
        st.session_state.score["Husky"] += 3
    elif q3==3 or q3==4 or q3==5:
        st.session_state.score["Bulldog"] += 2
        st.session_state.score["Poodle/Doodle"] += 2


    #Q4
    if q4 == "Yellow":
        st.session_state.score["Poodle/Doodle"] += 1
        st.session_state.score["Golden Retriever"] += 1
    elif q4 == "Blue":
        st.session_state.score["Husky"] += 1
        st.session_state.score["Bulldog"]+=1
    elif q4 == "Grey":
        st.session_state.score["Daschund"] += 1
        st.session_state.score["Beagle"] += 1
    elif q4 == "Black":
        st.session_state.score["AN IMPOSTER!...YOU'RE A CAT!"] += 1

    #Q5
    if q5 == 0:
        st.session_state.score["AN IMPOSTER!...YOU'RE A CAT!"] += 1
    elif q5 >= 5:
        st.session_state.score["Mutt"] += 1
        st.session_state.score["Golden Retriever"] += 2
        st.session_state.score["Daschund"] += 1
        st.session_state.score["Husky"] += 3
    else:
        st.session_state.score["Poodle/Doodle"] += 1
        st.session_state.score["Beagle"] += 1



def results():
    
    your_breed = max(st.session_state.score, key=st.session_state.score.get)
    
    st.success(f"You are... {your_breed}!")
    
    image_paths = {
        "Mutt": "mutt.jpg",
        "Poodle/Doodle": "poodle.jpg",
        "Golden Retriever": "golden.jpg",
        "Husky": "husky.jpg",
        "Beagle": "beagle.jpg",
        "Daschund": "dachshund.jpg",
        "Bulldog": "bulldog.jpg",
        "AN IMPOSTER!...YOU'RE A CAT!": "cat.jpg"
    }
    
    if your_breed in image_paths:
        st.image(image_paths[your_breed], width=300)
    

def start_quiz():
    starting_scores()
    q1, q2, q3, q4, q5 = question1()
    
    if st.button("What's My Dogdentity?!"):
        
        calc_scores(q1, q2, q3, q4, q5)
        
        results()

def main(): 
    title_info()
    start_quiz()
  

if __name__ == "__main__":
    main()
