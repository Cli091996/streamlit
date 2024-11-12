import streamlit as st
from PIL import Image
def main():

    # Load the image
    image = Image.open('media/Chromium_Logo.svg.png')
    
    # Set the layout
    st.set_page_config(layout="wide")
    
    # Create three columns that span 2/3 of the screen
    cols = st.columns([1, 1,1,1, 1])  # Left column (1), Center column (2), Right column (1)
    
    # Place the image in the center column
    with cols[2]:
        st.image(image, use_container_width=False, width=300)
    
    # Add the title centered below the image
    st.markdown(
        """
        <h1 style="text-align: center;">Pace Holdings Explorer</h1>
        """,
        unsafe_allow_html=True,
    )

    # Create a container for the buttons
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; margin: 20px;">
            <button style="flex: 1; margin-right: 10px; padding: 10px;">Button 1</button>
            <button style="flex: 1; margin: 0 10px; padding: 10px;">Button 2</button>
            <button style="flex: 1; margin-left: 10px; padding: 10px;">Button 3</button>
        </div>
        """,
        unsafe_allow_html=True,
    )



if __name__ == "__main__":
    main()
