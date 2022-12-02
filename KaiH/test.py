# SET FOLDER ENVIRONMENT
import sys
if sys.platform=='win32':
    dots='..'
    kaipath=''
else:
    dots='.'
    kaipath='./KaiH/'

dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')
import streamlit as st
st.set_page_config(layout="wide")
#import plotly.express as px

# SET USR
usr= {'jvk':1,
      'ak':1,
      'kb':1,
      'kh':1}
gwidth=750
s=dict(Intro='Intro',
            jonas='Economic perspective',
            alexej='Further details,
            kaib='Nuclear weapons tests',
            kaih='Nuclear armament',
            sum='Summary',
            Architecture='.')

# STREAMLIT SIDEBAR
st.sidebar.image(f'{kaipath}nuke.jpg')
st.sidebar.title('NU*ES')
slide = st.sidebar.radio('',[s['Intro'],s['kaih'],s['alexej'],s['kaib'],s['jonas'],s['sum'],s['Architecture']])
st.header(slide)
if sys.platform=='win32':
    st.sidebar.title('***LOCAL INSTANCE***')

# STREAMLIT MAINPAGE
#Helper
def spacing():
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')
    st.markdown('####')

def import_plots(plots):
    for i in range (0,len(plots)):
         show_plot(plots,i)

def show_plot(plots,index):
    if index!=0:
        spacing()
    st.header(plots[index][2]['title'])
    st.subheader(plots[index][2]['description'])
    if (plots[index][2]['lib'] == 'plotly_go') or (plots[index][2]['lib'] == 'plotly_chart')or (plots[index][2]['lib'] == 'plotly_express'):
        st.plotly_chart(plots[index][1])
  #  elif (plots[index][2]['lib'] == 'plotly_express'):
  #      st.plotly_chart(plots[index][1])



#PageGen
if slide==(s['kaib']):
    if usr['kb']:
        import plotkb as pkb
        plots=pkb.get_plots()
        import_plots(plots)
elif slide == (s['alexej']):
    if usr['ak']:
        import plotak as pak
        plots=pak.get_plots()
        import_plots(plots)
elif slide == (s['jonas']):
    if usr['jvk']:
        import completejvk as pjvk
        plots=pjvk.get_plots()
        import_plots(plots)
elif slide == (s['kaih']):
    if usr['kh']:
        import plotkh as pkh
        plots=pkh.get_plots()

        #trinity facts
        st.subheader('The Trinity Test in 1945')
        st.image(f'{kaipath}trinity.jpg', width=gwidth)
        st.caption('Trinity: Test of the first nuclear Weapon in New Mexico, US 16.07.45 (Picture Credit: https://www.atomicarchive.com)')
        spacing()

        show_plot(plots, 0)
        st.caption('Amid 1945, the United States became the first nuclear power by building "little-boy" and "fat-man", the first operational atomic bombs (15-20 kts), later dropped on Hiroshima and Nagasaki.')
        #tsar image destruction
        spacing()

        st.subheader('The Tsar Bomb in 1961, peak of the race for stronger weapons')
        st.image(f'{kaipath}tsar.jpg', width=gwidth)
        st.caption('The Tsar Bomb\'s (50,000-60,000 kts) fireball, about 8 km wide at its maximum reached nearly 10.5 km in the sky. (https://wikipedia.de)')


        show_plot(plots,1)
        st.caption('During Cold War, nuclear stockpile rose extremely, allowing severe demolition of the entire planet for several times with the arsenal of a single country.')
        spacing()

        st.subheader('NEW Start in 2012, the latest big nuclear arms reduction treaty')
        st.image(f'{kaipath}newstart.jpg', width=gwidth)
        st.caption('Then-Vice President Joe Biden and Russian Prime Minister Vladimir Putin in Moscow, Russia, in 2012. | AP Photo/Alexander Zemlianichenko  (https://www.politico.com)')


        show_plot(plots,2)
        st.caption('In 2022, the amount of nuclear weapons is severely smaller, than at the peak of the cold war. However, since warheads are much more powerful these days, nuclear deterrence is still given. Interestingly, the nuclear armament mainly takes place in the northern hemisphere of the planet. Current events remind of the volatiliy of the well known concept of mutually assured destruction (MAD).  ')

elif slide == (s['Architecture']):
    st.image(f'{kaipath}architecture.jpg')
    st.caption('Architecture of underlying framework for nu*de data analysis (WIP)')
elif slide == (s['Intro']):
    st.image(f'{kaipath}bikinibomb.jpg')
    st.caption('Showgirl Joy Healy smiles as she straddles a U.S. Air Force missile, wearing a bikini costume, at an American Federation of Labor Union show, in Los Angeles, California, in 1945 (Photo credit: Hulton Archive/Getty Images)')
elif slide == (s['sum']):
    spacing()
    st.subheader('Nuclear deterrence is still given up to this day, however it is difficult to predict the corresponding doctrines of the nuclear powers in the near future, given the current events.')
    st.subheader('jvk')
    st.subheader('ak')
    st.subheader('kb')