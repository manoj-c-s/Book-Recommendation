import copy
from socket import herror
import streamlit as st
from helper import Helper

# setting the page content
st.set_page_config(
    page_title="Book Recommender System",
    page_icon="assets/icon.png",
    menu_items={
        "about": "Hi there, thanks for checking out my app! feel free to checkout my [GitHub](https://www.github.com/kameshkotwani) page lets collaborate!"
    }
)

try:
    @st.cache()
    def load_popular_books():
        helper = Helper()
        return helper.get_popular_books()
    
    helper = Helper()
    

    books_name,author,image,votes,rating = load_popular_books()
    book_options = helper.get_book_list()
   
    # creating the sidebar
    with st.sidebar:
        st.title("If your NIE Student and then click on this [link](https://connect-37bba.web.app/login)" )
        st.title("Book Recommendation System")
        user_option = st.selectbox(label="Start your search here!", options=( "Top 48 Books","Recommend"))


    
    if user_option =="Top 48 Books":
        with st.spinner("loading top 48 books!"):
            st.header("You are currently looking at top 48 most read books!")
                
            k:int = 0
            # had to use 12 rows and 4 rows to create a grid of 48 itmes, otherwise getting list index out of range error 
            for i in range(1, 12):
                cols = st.columns(4)
                for j in range(0,4):
                    with cols[j]:
                        st.image(image[k])
                        st.write(f"{books_name[k]}")
                        st.caption(f"Author: {author[k]}")
                        st.caption(f"Votes: {votes[k]}")
                        st.caption(f"Rating: {rating[k]}")
                        k+=1
    elif user_option =="Recommend":
        st.subheader("Select your favorite book here and get top 5 recommendation for it 📚")
        user_option = st.selectbox(label="",options=book_options)
        if user_option:
            with st.spinner("Fetcing great books!"):
                recommended_books = helper.recommend_books(user_option)
                cols = st.columns(5)
                for i in range(0,5):
                    with cols[i]:
                        st.image(recommended_books[i][2])
                        st.write(recommended_books[i][0])
                        st.caption(f"Author: {recommended_books[i][1]}")
                        st.caption(f"Publisher: {recommended_books[i][4]}")
                        st.caption(f"Published on: {recommended_books[i][3]}")
                        
except Exception as e:
    print(e)
    st.info("perhaps, you are a unique user and we were not able to find book similar to yours.")