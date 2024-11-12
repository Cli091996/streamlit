import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="Logo Placement", page_icon=":logo:", layout="wide")
    
    # SVG content
    svg_icon = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-image" style="width: 40px; height: 40px;">
      <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
      <circle cx="8.5" cy="8.5" r="1.5"></circle>
      <polyline points="21 15 16 10 5 21"></polyline>
    </svg>
    """
    
    # Define header customization
    def create_header(icon, text, text_size=30, text_color="black"):
        # Use a single container to render the SVG and text side by side
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; position: absolute; top: 0; left: 0; margin: 0; padding: 0;">
                <div>{icon}</div>
                <div style="font-size: {text_size}px; font-weight: bold; margin-left: 10px; color: {text_color};">
                    {text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    ## Centered logo rendering
    def create_center_logo(icon, transparency=1.0):
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh;">
                <div style="opacity: {transparency};">
                    {icon}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    #Create horizontally aligned buttons
    def create_buttons():
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Data Refresh"):
                st.write("Data Refresh button clicked!")
        with col2:
            if st.button("Data Exploration"):
                st.write("Data Exploration button clicked!")
        with col3:
            if st.button("More"):
                st.write("More button clicked!")

    
    # Render the header at the very top left corner
    create_header(icon=svg_icon, text="Logo Placement", text_size=30, text_color="blue")

    # Render the logo at the center with transparency
    create_center_logo(icon=svg_icon, transparency=0.8)
    
    # Render the buttons below the header or in another position
    create_buttons()
if __name__ == "__main__":
    main()
