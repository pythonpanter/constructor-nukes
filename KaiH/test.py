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

# SET USR
usr= {'jvk':1,
      'ak':1,
      'kb':1,
      'kh':1}

s=dict(Intro='Intro',
            jonas='Jonas Story',
            alexej='Alexejs  Story',
            kaib='Kai Bs Story',
            Architecture='Architecture')

# STREAMLIT SIDEBAR
st.sidebar.image(f'{kaipath}nuke.jpg')
st.sidebar.title('NU*ES')
slide = st.sidebar.radio('',[s['Intro'],s['jonas'],s['alexej'],s['kaib'],s['Architecture']])
st.header(slide)
if sys.platform=='win32':
    st.sidebar.title('***LOCAL INSTANCE***')

# STREAMLIT MAINPAGE
#Helper
def import_plots(plots):
    for i in range (0,len(plots)):
         show_plot(plots,i)

def show_plot(plots,index):
    st.header(plots[index][2]['title'])
    st.subheader(plots[index][2]['description'])
    if (plots[index][2]['lib'] == 'plotly_go') or (plots[index][2]['lib'] == 'plotly_chart'):
        st.plotly_chart(plots[index][1])

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
        import plotjvk as pjvk
        plots=pjvk.get_plots()
        import_plots(plots)
elif slide == (s['Architecture']):
    st.image(f'{kaipath}architecture.jpg')
    st.caption('Architecture of underlying framework for nu*de data analysis (WIP)')
elif slide == (s['Intro']):
    st.image(f'{kaipath}bikinibomb.jpg')
    st.caption('Showgirl Joy Healy smiles as she straddles a U.S. Air Force missile, wearing a bikini costume, at an American Federation of Labor Union show, in Los Angeles, California, in 1945  (Photo credit: Hulton Archive/Getty Images)')