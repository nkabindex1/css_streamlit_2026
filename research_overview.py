# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:24:57 2026

@author: xolaninkabinde
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Researcher Overview - Xolani Nkabinde",
    layout="centered"
)

# Header
st.title("Researcher Overview")

# Basic Info
st.header("Xolani Nkabinde")
st.subheader("Field of Research: Cyber Security")
st.write("**Institution:** University of Johannesburg")

st.divider()

# Summary Section
st.header("Summary")
st.write(
    """
    I am an organized and dependable candidate with a strong interest in cybersecurity and artificial intelligence, capable of managing multiple tasks with a positive and detail-oriented approach. I am eager to take on added responsibilities and continuously develop technical skills in areas such as secure systems, data-driven decision-making, and intelligent technologies. I am highly goal-oriented, and through effective planning and time management, I consistently work toward achieving objectives within realistic and measurable timeframes.
    """
)

st.divider()

# Education Section
st.header("Education")

st.markdown(
    """
    **Bachelor of Science (BSc) in Computer Science**  
    University of Johannesburg 
    *2016–2019*  
    """
)

st.divider()

# Skills Section
st.header("Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data & Analysis")
    st.markdown(
        """
        - Data verification and maintenance  
        - Predictive modeling  
        - Data munging  
        - Strong analytical skills
        """
    )

with col2:
    st.subheader("Technical")
    st.markdown(
        """
        - Database development
        """
    )

with col3:
    st.subheader("Professional")
    st.markdown(
        """
        - Excellent communication skills  
        - Leadership skills
        """
    )

st.divider()

# Contact Information
st.header("Contact Information")
st.write(
    "You can reach **Xolani Nkabinde** at 📧 **nkabindex1@gmail.com**."
)
