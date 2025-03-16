
import streamlit as st
import json

st.set_page_config(page_title='Library Management App 🏛️', page_icon='📚')

# Custom CSS for styling
st.markdown("""
    <style>
        /* Gradient Background */
        .stApp {
            background: linear-gradient(135deg, #FFC0CB, #800080);
            color: #000000;
        }

        /* Gradient Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            color: black;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            transition: 0.3s ease;
        }
            

        div.stButton > button:hover {
            background: linear-gradient(135deg, #ff7eb3, #ff758c);
            transform: scale(1.05);
        }

        /* Shadowed Input Fields */
        .stTextInput > div > div > input {
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
            border-radius: 8px;
            border: 1px solid #ccc;
        }
            
        /* Sidebar Styling */
        .css-1d391kg {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
        }

    </style>
""", unsafe_allow_html=True)

# Load/Send and save library data
def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the library
def save_library(library):
    with open('library.json', 'w') as file:
        json.dump(library, file, indent=4)

# Initialize the library
library = load_library()

# Title of the app
st.title('📖 Personal Library Manager 📚')

# Sidebar Menu with Emojis
menu = st.sidebar.radio("📌 Select an Option", [
    '📚 View Library', 
    '➕ Add books', 
    '❌ Remove Book', 
    '🔍 Search Books', 
    '💾 Save & Exit'
])

# View Library
if menu == '📚 View Library':
    st.header('📖 Your Library')
    if library:
        st.table(library)
    else:
        st.warning('⚠️ Your Library is Empty! Add some books. 📚')

# Add Book
elif menu == '➕ Add books':
    st.header('📝 Add a New Book')
    title = st.text_input('📖 Title')
    author = st.text_input('✍️ Author')
    publish_year = st.number_input("📅 Year", min_value=2005, max_value=2050, step=1)
    category = st.text_input('📂 Category')
    read_status = st.checkbox('✅ Mark as Read')

    if st.button('📥 Add Book'):
        library.append({
            "Title": title, 
            "Author": author, 
            "Year": publish_year, 
            "Category": category, 
            "Read_Status": read_status
        })
        save_library(library)
        st.success('✅ Book Added Successfully! 🎉')
        st.balloons()

# Remove Book
elif menu == '❌ Remove Book':
    st.header('🗑️ Remove a Book')
    book_titles = [book['Title'] for book in library]

    if book_titles:
        selected_book = st.selectbox('📌 Select Book to Remove', book_titles)
        if st.button('🗑️ Remove Book'):
            library[:] = [book for book in library if book['Title'] != selected_book]
            save_library(library)
            st.success('✅ Book Removed Successfully! 🎯')
            st.balloons()
    else:
        st.warning('⚠️ No books in your library. Add some books! 📚')

# Search Book
elif menu == '🔍 Search Books':
    st.header('🔎 Search a Book')
    search_input = st.text_input('🔍 Search by Title or Author')

    if search_input:
        search_results = [book for book in library if search_input.lower() in book['Title'].lower() or search_input.lower() in book['Author'].lower()]
        if search_results:
            st.success(f'✅ {len(search_results)} book(s) found! 📚')
            st.table(search_results)
        else:
            st.warning('⚠️ No Books Found!')

# Save & Exit
elif menu == '💾 Save & Exit':
    st.header('📁 Thank You for Using Library Manager! 😊')
    save_library(library)
    st.balloons()
