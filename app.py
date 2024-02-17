import streamlit as st

sometext = 'Hello World'

st.write(sometext) # this is shown in the webpage
print(sometext) # this is hown in the terminal

st.markdown("""
    # title

    ## many levels of subtitles

    **bold** or *italic* text with [links](http://github.com/streamlit) and:
    - bullet points
""")

col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")


our_button = st.checkbox('Show content')
# our_button = print('show')

st.write(our_button)

if our_button:
    st.write('''
        This code will only be executed when the check box is checked

        Streamlit elements injected inside of this block of code will \
        not get displayed unless it is checked
        ''')
