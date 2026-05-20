import streamlit as st
import pandas as pd


from chatbot import get_ai_response

from database import (
    save_lead,
    get_all_leads,
    delete_lead,
    delete_all_leads
)

from automation import send_notification


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="AI Business Assistant",
    layout="wide"
)


# =========================================
# MAIN TITLE
# =========================================

st.title("🤖 AI-Powered Business Automation Assistant")

st.markdown("""
Welcome to the AI-powered automation platform.

### Features:
- AI Business Chatbot
- Lead Management
- Automation Workflow
- Analytics Dashboard
- Email Automation
- Multilingual Support
""")


# =========================================
# SIDEBAR MENU
# =========================================

st.sidebar.title("Navigation Menu")

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "AI Chatbot",
        "Lead Capture",
        "Admin Dashboard"
    ]
)


# =========================================
# AI CHATBOT WITH CHAT HISTORY
# =========================================

if menu == "AI Chatbot":

    st.header("🤖 AI Business Chatbot")

    # Create session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # Chat input
    user_input = st.chat_input(
        "Ask your business question..."
    )

    # If user enters message
    if user_input:

        # Show user message
        with st.chat_message("user"):

            st.markdown(user_input)

        # Store user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # AI Response
        with st.spinner("AI is thinking..."):

            response = get_ai_response(user_input)

        # Show AI response
        with st.chat_message("assistant"):

            st.markdown(response)

        # Store AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })


# =========================================
# LEAD CAPTURE FORM
# =========================================

elif menu == "Lead Capture":

    st.header("📋 Lead Capture Form")

    with st.form("lead_form"):

        name = st.text_input("Enter Name")

        email = st.text_input("Enter Email")

        phone = st.text_input("Enter Phone")

        message = st.text_area("Enter Message")

        submit = st.form_submit_button("Submit")

        if submit:

            # Save lead
            save_lead(name, email, phone, message)

            # Send automation email
            send_notification(name, email)

            st.success("✅ Lead Submitted Successfully!")


# =========================================
# ADMIN DASHBOARD
# =========================================

elif menu == "Admin Dashboard":

    st.header("📊 Admin Dashboard")

    # Get all leads
    leads = get_all_leads()

    # Create DataFrame
    df = pd.DataFrame(
        leads,
        columns=[
            "ID",
            "Name",
            "Email",
            "Phone",
            "Message"
        ]
    )

    # Show Data Table
    st.dataframe(df)

    # Total Leads Metric
    st.metric(
        label="Total Leads",
        value=len(df)
    )

    # ====================================
    # ANALYTICS DASHBOARD
    # ====================================

    st.subheader("📈 Lead Analytics Dashboard")

    # Email Analytics
    email_counts = df["Email"].value_counts()

    st.bar_chart(email_counts)

    # Phone Length Analytics
    phone_lengths = df["Phone"].astype(str).apply(len)

    st.line_chart(phone_lengths)

    # ====================================
    # DELETE SINGLE RECORD
    # ====================================

    st.subheader("🗑 Delete Lead Record")

    lead_id = st.number_input(
        "Enter Lead ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Record"):

        delete_lead(lead_id)

        st.success("Lead deleted successfully!")

        st.rerun()

    # ====================================
    # DELETE ALL RECORDS
    # ====================================

    st.subheader("⚠ Delete All Records")

    if st.button("Delete All Leads"):

        delete_all_leads()

        st.success("All lead records deleted!")

        st.rerun()
        
    