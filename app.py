from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT=Path(__file__).resolve().parent
st.set_page_config(page_title='Africa AI Incident Observatory', page_icon='🔎', layout='wide')
df=pd.read_csv(ROOT/'data'/'incidents.csv')
df['incident_date']=pd.to_datetime(df['incident_date'], errors='coerce')
df['year']=df['incident_date'].dt.year

st.title('Africa AI Incident Observatory')
st.caption('Source-traceable incident evidence. Seed release: curated, incomplete, and designed to preserve uncertainty.')

with st.expander('Read before interpreting the data', expanded=False):
    st.markdown("AAIO is an independent research project, not an official AIID/OECD/AU database. A missing country does **not** mean no AI incidents occurred. Severity is an AAIO research rubric; evidence confidence is separate from severity.")

c1,c2,c3,c4=st.columns(4)
c1.metric('Core records',len(df))
c2.metric('Primary countries',df['country'].nunique())
c3.metric('Sectors',df['sector'].nunique())
c4.metric('A/B evidence',int(df['evidence_confidence'].isin(['A','B']).sum()))

st.sidebar.header('Filters')
countries=st.sidebar.multiselect('Country',sorted(df.country.unique()))
sectors=st.sidebar.multiselect('Sector',sorted(df.sector.unique()))
years=st.sidebar.multiselect('Year',sorted(df.year.dropna().astype(int).unique()))
confidence=st.sidebar.multiselect('Evidence confidence',['A','B','C'])
severity=st.sidebar.multiselect('Severity',['Low','Limited','Moderate','High','Critical'])
q=st.sidebar.text_input('Search title/summary')

f=df.copy()
if countries: f=f[f.country.isin(countries)]
if sectors: f=f[f.sector.isin(sectors)]
if years: f=f[f.year.isin(years)]
if confidence: f=f[f.evidence_confidence.isin(confidence)]
if severity: f=f[f.severity_band.isin(severity)]
if q:
    mask=(f.title.fillna('').str.contains(q,case=False,regex=False)|f.summary.fillna('').str.contains(q,case=False,regex=False))
    f=f[mask]

left,right=st.columns(2)
with left:
    by_country=f.groupby('country',as_index=False).size().rename(columns={'size':'records'})
    fig=px.choropleth(by_country,locations='country',locationmode='country names',color='records',scope='africa',title='Records by primary country')
    st.plotly_chart(fig,use_container_width=True)
with right:
    timeline=f.groupby('year',as_index=False).size().rename(columns={'size':'records'})
    fig2=px.bar(timeline,x='year',y='records',title='Incident records by year')
    st.plotly_chart(fig2,use_container_width=True)

st.subheader('Records')
show=['incident_id','incident_date','country','sector','title','severity_score','severity_band','evidence_confidence']
st.dataframe(f[show].sort_values('incident_date',ascending=False),use_container_width=True,hide_index=True)

st.subheader('Incident detail')
for _,r in f.sort_values('incident_date',ascending=False).iterrows():
    with st.expander(f"{r['incident_id']} · {r['title']}"):
        st.write(r['summary'])
        a,b,c=st.columns(3)
        a.write(f"**Evidence:** {r['evidence_confidence']}")
        b.write(f"**Severity:** {r['severity_band']} ({r['severity_score']}/100)")
        c.write(f"**System:** {r['system_type']}")
        st.write(f"**Affected parties:** {r['affected_parties'].replace('|', ', ')}")
        st.write(f"**Response:** {r['response']}")
        st.write(f"**Qualification:** {r['qualification_basis']}")
        st.markdown(f"[Primary evidence link]({r['source_1_url']}) · [Secondary evidence link]({r['source_2_url']})")
        if pd.notna(r.get('aiid_url')): st.markdown(f"[AIID cross-reference]({r['aiid_url']})")

st.caption('Curated by Blessing Ezeobioha. See docs/methodology.md for inclusion and scoring rules.')
