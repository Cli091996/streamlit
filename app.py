# import streamlit as st
# from PIL import Image
# def landing_page():

#     # Load the image
#     image = Image.open('media/Chromium_Logo.svg.png')
    
#     # # Set the layout
#     # st.set_page_config(layout="wide")
    
#     # Create three columns that span 2/3 of the screen
#     cols = st.columns([1, 1,1,1, 1])  # Left column (1), Center column (2), Right column (1)
    
#     # Place the image in the center column
#     with cols[2]:
#         st.image(image, use_container_width=False, width=300)
    
#     # Add the title centered below the image
#     st.markdown(
#         """
#         <h1 style="text-align: center;">Pace Holdings Explorer</h1>
#         """,
#         unsafe_allow_html=True,
#     )
#     #Test 1 - Working 
#     # # Create a container for the buttons
#     # st.markdown(
#     #     """
#     #     <div style="display: flex; justify-content: space-between; margin: 20px;">
#     #         <button style="flex: 1; margin-right: 10px; padding: 10px;">Button 1</button>
#     #         <button style="flex: 1; margin: 0 10px; padding: 10px;">Button 2</button>
#     #         <button style="flex: 1; margin-left: 10px; padding: 10px;">Button 3</button>
#     #     </div>
#     #     """,
#     #     unsafe_allow_html=True,
#     # )

# #     #Test 2 - Working - using this for now 
# #     #Create a container for the buttons
# #     st.markdown(
# #     """
# #     <style>
# #         .custom-button {
# #             flex: 1;
# #             margin: 0 10px;
# #             padding: 10px;
# #             background-color: #007BFF;
# #             color: white;
# #             border: none;
# #             border-radius: 5px;
# #             cursor: pointer;
# #             font-size: 16px;
# #             transition: background-color 0.3s ease, transform 0.2s ease;
# #         }
# #         .custom-button:hover {
# #             background-color: #0056b3;
# #             transform: scale(1.05);
# #         }
# #         .button-container {
# #             display: flex;
# #             justify-content: space-between;
# #             margin: 20px;
# #         }
# #     </style>
# #     <div class="button-container">
# #         <button class="custom-button">Button 1</button>
# #         <button class="custom-button">Button 2</button>
# #         <button class="custom-button">Button 3</button>
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )
#     #Test 3 - not tested 
#     # Create the buttons with HTML and add session state control
#     # st.markdown(
#     #     """
#     #     <style>
#     #         .custom-button {
#     #             flex: 1;
#     #             margin: 0 10px;
#     #             padding: 10px;
#     #             background-color: #007BFF;
#     #             color: white;
#     #             border: none;
#     #             border-radius: 5px;
#     #             cursor: pointer;
#     #             font-size: 16px;
#     #             transition: background-color 0.3s ease, transform 0.2s ease;
#     #         }
#     #         .custom-button:hover {
#     #             background-color: #0056b3;
#     #             transform: scale(1.05);
#     #         }
#     #         .button-container {
#     #             display: flex;
#     #             justify-content: space-between;
#     #             margin: 20px;
#     #         }
#     #     </style>
#     #     <div class="button-container">
#     #         <button class="custom-button" onclick="Streamlit.setComponentValue('page', 'Refresh Data')">Refresh Data</button>
#     #         <button class="custom-button" onclick="Streamlit.setComponentValue('page', 'Viz')">Viz</button>
#     #         <button class="custom-button" onclick="Streamlit.setComponentValue('page', 'More')">More</button>
#     #     </div>
#     #     """,
#     #     unsafe_allow_html=True,
#     # )

#     # # Create three columns for horizontal alignment
#     # cols = st.columns([1,1,1,1,1,1])  # Adjust the proportions if needed

#     # with cols[1]:
#     #     st.button("Data Refresh", on_click=lambda: st.session_state.update({"page": "Simulator"}))
#     # with cols[3]:
#     #     st.button("Visualization", on_click=lambda: st.session_state.update({"page": "Analytics"}))
#     # with cols[5]:
#     #     st.button("More Features", on_click=lambda: st.session_state.update({"page": "Exit"}))
#     # Create three columns for horizontal alignment

#     # Create three columns for horizontal alignment
#     cols = st.columns([1, 1, 1, 1, 1, 1])  # Adjust the proportions if needed
    
#     button_style = """
#     <style>
#         .custom-button {
#             font-size: 16px;
#             padding: 10px 20px;
#             margin: 5px;
#             color: white;
#             background-color: #007BFF;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             text-align: center;
#             transition: background-color 0.3s ease, transform 0.2s ease;
#         }
#         .custom-button:hover {
#             background-color: #0056b3;
#             transform: scale(1.05);
#         }
#         .button-container {
#             text-align: center;
#         }
#     </style>
#     """
    
#     # Include the CSS styles
#     st.markdown(button_style, unsafe_allow_html=True)
    
#     # Define buttons with their respective actions
#     with cols[0]:
#         st.markdown(
#             '<div class="button-container">'
#             '<button class="custom-button" onclick="window.location.href=\'#Simulator\'">Data Refresh</button>'
#             '</div>',
#             unsafe_allow_html=True,
#         )
    
#     with cols[2]:
#         st.markdown(
#             '<div class="button-container">'
#             '<button class="custom-button" onclick="window.location.href=\'#Analytics\'">Viz</button>'
#             '</div>',
#             unsafe_allow_html=True,
#         )
    
#     with cols[4]:
#         st.markdown(
#             '<div class="button-container">'
#             '<button class="custom-button" onclick="window.location.href=\'#Exit\'">More Features</button>'
#             '</div>',
#             unsafe_allow_html=True,
#         )

#     # Use Streamlit buttons for page navigation
#     if 'page' not in st.session_state:
#         st.session_state.page = 'Landing_Page'  # Default to "Refresh Data" on first load

#     # Manage the session state and page content
#     if st.session_state.page == "Refresh Data":
#         st.write("You are on Page: Refresh Data")
#         # Add content for "Refresh Data" here
#     elif st.session_state.page == "Viz":
#         st.write("You are on Page: Viz")
#         # Add content for "Viz" here
#     elif st.session_state.page == "More Features":
#         st.write("You are on Page: More Features")
#         # Add content for "More" here

# def custom_button(label, button_id, background_color="#007BFF", hover_color="#0056b3", text_color="white", width="150px", height="50px", font_size="16px"):
#     """
#     Generate a custom-styled button using HTML and CSS.

#     Args:
#         label (str): The text displayed on the button.
#         button_id (str): The unique identifier for the button (used in JavaScript).
#         background_color (str): The button's background color.
#         hover_color (str): The color of the button when hovered over.
#         text_color (str): The color of the text on the button.
#         width (str): The width of the button.
#         height (str): The height of the button.
#         font_size (str): The font size of the button text.
#     """
#     custom_style = f"""
#     <style>
#         #{button_id} {{
#             background-color: {background_color};
#             color: {text_color};
#             width: {width};
#             height: {height};
#             font-size: {font_size};
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             transition: background-color 0.3s ease, transform 0.2s ease;
#         }}
#         #{button_id}:hover {{
#             background-color: {hover_color};
#             transform: scale(1.05);
#         }}
#     </style>
#     <button id="{button_id}" onclick="document.getElementById('{button_id}_hidden').click()">{label}</button>
#     """
#     # Render the styled button and create a hidden Streamlit button for interaction
#     st.markdown(custom_style, unsafe_allow_html=True)
#     return st.button(label, key=f"{button_id}_hidden", use_container_width=True)

# def main():
#     # Navigation function 
#     def navigate_to_page(page):
#         st.session_state.page = page

#     # Set app layout to wide
#     st.set_page_config(layout="wide")

#     # Initialize session state
#     if "page" not in st.session_state:
#         st.session_state.page = "Landing_Page"  # Default to the landing page

#     # Set side visibility to none if on the landing page
#     if st.session_state.page == "Landing_Page":
#         hide_sidebar()
#         landing_page()
#     else:
#         st.sidebar.header("Supply Chain Simulator")
#         render_page(st.session_state.page)

# def hide_sidebar():
#     # Hides the sidebar using custom CSS
#     st.markdown(
#         """
#         <style>
#         [data-testid="stSidebar"] {
#             display: none;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
    
# def render_page(page):
#     if page == "Simulator":
#         st.title("Simulator Page")
#         # Add simulator-specific content here
#     elif page == "Analytics":
#         st.title("Analytics Page")
#         # Add analytics-specific content here

#     # landing_page()

# if __name__ == "__main__":
#     main()
import streamlit as st
from PIL import Image

# Hide sidebar for the landing page
def hide_sidebar():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Landing page
def landing_page():
    # Load the image
    image = Image.open('media/Chromium_Logo.svg.png')

    # Create three columns for layout
    cols = st.columns([1, 1, 1, 1, 1])

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

    # Add buttons for navigation
    cols = st.columns([1, 1, 1, 1, 1])

    with cols[1]:
        if st.button("Data Refresh"):
            st.session_state.page = "Simulator"

    with cols[2]:
        if st.button("Visualization"):
            st.session_state.page = "Analytics"

    with cols[3]:
        if st.button("More Features"):
            st.session_state.page = "More"

# Simulator page
def simulator_page():
    st.title("Simulator Page")
    st.write("Content for the Simulator Page")

# Analytics page
def analytics_page():
    st.title("Analytics Page")
    st.write("Content for the Analytics Page")

# More features page
def more_page():
    st.title("More Features Page")
    st.write("Content for the More Features Page")

# Main function
def main():
    # Set app layout to wide
    st.set_page_config(layout="wide")

    # Initialize session state for the current page
    if "page" not in st.session_state:
        st.session_state.page = "Landing_Page"

    if st.session_state.page == "Landing_Page":
        hide_sidebar()
        landing_page()
    else:
        # Sidebar Navigation
        current_page = st.navigation({
            "Main Pages": [
                st.Page(simulator_page, title="Simulator"),
                st.Page(analytics_page, title="Analytics"),
                st.Page(more_page, title="More Features"),
            ]
        })

        # Run the selected page
        current_page.run()

if __name__ == "__main__":
    main()

