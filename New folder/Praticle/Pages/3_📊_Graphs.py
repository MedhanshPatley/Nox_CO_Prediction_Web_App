
# import streamlit as st

# st.title("Heatmap")
# # Load your data
# def Heatmap():
#     import streamlit as st
# import plotly.graph_objs as go
# import plotly.io as pio
# import pandas as pd
    
    
# df= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')

# # Compute the correlation matrix
# corr_matrix = df.corr()

# # Define the heatmap trace
# trace = go.Heatmap(z=corr_matrix.values,
#                    x=corr_matrix.columns,
#                    y=corr_matrix.columns,
#                    colorscale='Viridis', # or 'Plasma'
#                    zmin=-1,
#                    zmax=1,
#                    colorbar=dict(title='Correlation',tickfont=dict(color='white'),title_font_color ='white'))

# # Define the layout
# layout = go.Layout(title='Correlation Heatmap',
#                    title_font_color='white',
#                    xaxis=dict(title=None, tickfont={"color": "white"}),
#                    yaxis=dict(title=None, tickfont={"color": "white"}),
#                    plot_bgcolor='black',
#                    paper_bgcolor='black',
#                    hovermode='closest')

# # Create the figure
# fig = go.Figure(data=[trace], layout=layout)

# # Update the x and y axis tick labels to white color
# fig.update_xaxes(tickfont=dict(color='white'))
# fig.update_yaxes(tickfont=dict(color='white'))

# # Use st.plotly_chart() to display the figure in your Streamlit app
# st.plotly_chart(fig)

# st.title("ScatterPlot For CO Gas")
# def Scatter_CO():
#     import streamlit as st
# import plotly.graph_objs as go
# import plotly.io as pio
# import pandas as pd

# # Load your data
# df_1 = pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')

# # Create the trace for the scatter plot
# trace = go.Scatter(x=df_1.loc[:, :'CDP'],
#                    y=df_1['CO'],
#                    mode='lines+markers',
#                    marker=dict(size=10, color=df['CO'], colorscale='Viridis', showscale=True))

# # Create the layout for the scatter plot
# layout = go.Layout(title='AT AP AH AFDP GTEP TIT TAT TEY CDP vs. CO',
#                    xaxis=dict(title='AT AP AH AFDP GTEP TIT TAT TEY CDP', titlefont=dict(size=14)),
#                    yaxis=dict(title='CO', titlefont=dict(size=14)),
#                    plot_bgcolor='rgb(243, 243, 243)',
#                    hovermode='closest',
#                    margin=dict(l=80, r=80, t=100, b=80),
#                    coloraxis_colorbar=dict(title='CO', thickness=20, len=0.4, xanchor='left', yanchor='middle'))

# # Create the figure for the scatter plot
# fig = go.Figure(data=[trace], layout=layout)

# # Update the x and y axis tick labels to white color
# fig.update_xaxes(tickfont=dict(color='white'))
# fig.update_yaxes(tickfont=dict(color='white'))

# # Use st.plotly_chart() to display the figure in your Streamlit app
# st.plotly_chart(fig)

# st.title("ScatterPlot For NOx Gas")
# def Scatter_NO():
#     import streamlit as st
# import plotly.graph_objs as go
# import plotly.io as pio
# import pandas as pd

# # Load the data
# df_2= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')

# # Create the trace for the scatter plot
# trace = go.Scatter(x=df_2.loc[:, :'CDP'],
#                    y=df_2['NOX'],
#                    mode='lines+markers',
#                    marker=dict(size=10, color=df['NOX'], colorscale='Viridis', showscale=True))

# # Create the layout for the scatter plot
# layout = go.Layout(title='AT AP AH AFDP GTEP TIT TAT TEY CDP vs. NOX',
#                    xaxis=dict(title='AT AP AH AFDP GTEP TIT TAT TEY CDP', titlefont=dict(size=14)),
#                    yaxis=dict(title='NOX', titlefont=dict(size=14)),
#                    plot_bgcolor='rgb(243, 243, 243)',
#                    hovermode='closest',
#                    margin=dict(l=80, r=80, t=100, b=80),
#                    coloraxis_colorbar=dict(title='NOX', thickness=20, len=0.4, xanchor='left', yanchor='middle'))

# # Create the figure for the scatter plot
# fig = go.Figure(data=[trace], layout=layout)

# # Render the scatter plot using Plotly
# st.plotly_chart(fig)

# def main():
#      with st.sidebar:
#        select = st.radio(label='EDA Of DataSet',options =['Heatmap()','Scatter CO()','Scatter NOx()'], )
#        if select ==Heatmap():
#            st.write("Heatmap of the dataset")
#        if select == Scatter_CO():
#            st.write("Scatterplot for the CO Gas")
#        elif select ==Scatter_NO():
#            st.write("Scatterplot for the NOx Gas")
           
           
import streamlit as st
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
import base64






def Heatmap():
    df= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')
    # Compute the correlation matrix
    corr_matrix = df.corr()

    # Define the heatmap trace
    trace = go.Heatmap(z=corr_matrix.values,
                       x=corr_matrix.columns,
                       y=corr_matrix.columns,
                       colorscale='Viridis', # or 'Plasma'
                       zmin=-1,
                       zmax=1,
                       colorbar=dict(title='Correlation',tickfont=dict(color='white'),title_font_color ='white'))

    # Define the layout
    layout = go.Layout(title='Correlation Heatmap',
                       title_font_color='white',
                       xaxis=dict(title=None, tickfont={"color": "white"}),
                       yaxis=dict(title=None, tickfont={"color": "white"}),
                       plot_bgcolor='black',
                       paper_bgcolor='black',
                       hovermode='closest')

    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)

    # Update the x and y axis tick labels to white color
    fig.update_xaxes(tickfont=dict(color='white'))
    fig.update_yaxes(tickfont=dict(color='white'))

    # Use st.plotly_chart() to display the figure in your Streamlit app
    st.plotly_chart(fig)

def Scatter_CO():
    import streamlit as st
    import matplotlib.pyplot as plt
    df_1= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')
    # Set up the data and plot
    features = ['AT', 'AP', 'AH', 'AFDP', 'GTEP', 'TIT', 'TAT', 'TEY', 'CDP', 'NOX']
    target = 'CO'

    fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(8, 10))

    for i, feature in enumerate(features):
        row = i // 2
        col = i % 2
        axs[row, col].scatter(df_1[feature], df_1[target], alpha = 0.3)
        axs[row, col].set_xlabel(feature)
        axs[row, col].set_ylabel(target)

    fig.suptitle('Scatter Subplots for Features with CO')
    fig.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)


def Scatter_NO():
    import streamlit as st
    import matplotlib.pyplot as plt
    df_2= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')

    features = ['AT', 'AP', 'AH', 'AFDP', 'GTEP', 'TIT', 'TAT', 'TEY', 'CDP', 'CO']
    target = 'NOX'

    # Create subplots for each feature
    fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(8, 10))

    # Loop through each feature and create a scatter plot with CO
    for i, feature in enumerate(features):
        row = i // 2
        col = i % 2
        axs[row, col].scatter(df_2[feature], df_2[target], alpha = 0.3)
        axs[row, col].set_xlabel(feature)
        axs[row, col].set_ylabel(target)


    fig.suptitle('Scatter Subplots for Features with NO')
    fig.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)
def Hisgram():
    import matplotlib.pyplot as plt
    import streamlit as st
    df_3= pd.read_csv('C:/Users/medha/Desktop/New folder/Praticle/Pages/important.csv')

    # create histogram


# create histogram plot
    fig, ax = plt.subplots(figsize=(10, 10))
    df_3.hist(bins=30, ax=ax)

    # display plot in Streamlit
    st.pyplot(fig)










def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("C:/Users/medha/Desktop/New folder/Praticle/Pages/image (2).jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/wp3205378.jpg");
background-size: 250%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
# Define your Streamlit app
def app():
    # st.set_page_config(page_title='EDA', page_icon=':bar_chart:', layout='wide')
    st.title('Exploratory Data Analysis')

    # Create a sidebar with options for the user to select
    menu = ['Homepage', 'Correlation Heatmap', 'Scatterplot of CO Emissions', 'Scatterplot of NOX Emissions','Histogram']
    choice = st.sidebar.radio('Select an option', menu)

    # Show the appropriate page based on the user's selection
    if choice == 'Homepage':
        st.header('Welcome to the world of Visualisation .')
        st.write('This Section provides an interactive EDA of the dataset.')
        # st.write('Use the sidebar to select a page to view and explore the data!')

    elif choice == 'Correlation Heatmap':
        st.title("HeatMap") 
        Heatmap()
        

    elif choice == 'Scatterplot of CO Emissions':
        st.title("ScatterPlot for CO Gas") 
        Scatter_CO()

    elif choice == 'Scatterplot of NOX Emissions':
        st.title("Scater for NOx Gas") 
        Scatter_NO()
    elif choice == 'Histogram':
        st.title("Histogram") 
        Hisgram()
        
# Run the app
if __name__ == '__main__':
    app()

