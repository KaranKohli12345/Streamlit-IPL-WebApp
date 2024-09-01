import streamlit as st
import requests

st.set_page_config(page_title='Karan Kumar | IPL Analysis Dashboard')

st.sidebar.title('IPL Dashboard')
option = st.sidebar.selectbox('What do you want to know about?', ['Team', 'Team Vs Team','Batter','Bowler'])

team_images = {
    'Chennai Super Kings': 'images/csk.jpg',
    'Deccan Chargers': 'images/dc.jpeg',
    'Delhi Capitals': 'images/dlc.png',
    'Delhi Daredevils': 'images/dd.jpg',
    'Gujarat Lions': 'images/gl.png',
    'Gujarat Titans': 'images/gt.png',
    'Kings XI Punjab': 'images/kp.png',
    'Kochi Tuskers Kerala': 'images/ktk.png',
    'Kolkata Knight Riders': 'images/kkr.png',
    'Lucknow Super Giants': 'images/lsg.png',
    'Mumbai Indians': 'images/mi.jpg',
    'Pune Warriors': 'images/pw.png',
    'Punjab Kings': 'images/pk.webp',
    'Rajasthan Royals': 'images/rr.jpg',
    'Rising Pune Supergiant': 'images/rps.jpeg',
    'Rising Pune Supergiants': 'images/rps.jpeg',
    'Royal Challengers Bangalore': 'images/rcb.jpeg',
    'Sunrisers Hyderabad': 'images/srh.png'
}

if option == 'Team':
    response1 = requests.get('https://ipl-api-2-0-7.onrender.com/api/teams')
    teams = sorted(response1.json()['Teams'])

    team = st.sidebar.selectbox('Select team', teams)

    btn = st.sidebar.button('View record')

    if btn:
        col1, col2 = st.columns(2)
        with col1:
            st.header(team)
        with col2:
            st.image(team_images[team])

        overall_team_record_ = requests.get('https://ipl-api-2-0-7.onrender.com/api/team-record-overall?team={}'.format(team))

        overall_team_record = overall_team_record_.json()

        st.subheader('Overall record')
        for i in overall_team_record:
            st.text(i + ' : ' + str(overall_team_record[i]))


elif option == 'Team Vs Team':
    response1 = requests.get('https://ipl-api-2-0-7.onrender.com/api/teams')
    teams = sorted(response1.json()['Teams'])

    team1 = st.sidebar.selectbox('Select Team1', teams)
    team2 = st.sidebar.selectbox('Select Team2', teams)

    btn = st.sidebar.button('View record')

    if btn:
        st.subheader('{} Vs {}'.format(team1, team2))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(team_images[team1])
        with col2:
            st.title('Vs')
        with col3:
            st.image(team_images[team2])

        response2 = requests.get('https://ipl-api-2-0-7.onrender.com/api/teamVsTeam?team1={}&team2={}'.format(team1, team2))

        for i in response2.json():
            st.text(i + ' : ' + str(response2.json()[i]))

            
