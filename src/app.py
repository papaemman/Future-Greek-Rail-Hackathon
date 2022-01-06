import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# from dash import dcc
# from dash import html



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

sidebar_style = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "textAlign": "center",
    "background-color":"lightgray"
    # "margin-left": "2%",
    # "margin-right": "2%"
}



content_style = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto"
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center", #style={"position":"fixed","top":"0","right":"0",}
)

navbar = dbc.Navbar(
    [
        # html.A(
        #     # Use row and col to control vertical alignment of logo / brand
        #     dbc.Row(
        #         [
        #             dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
        #             dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
        #         ],
        #         align="center",
        #         no_gutters=True,
        #     ),
        #     href="https://plot.ly",
        # ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True, style={"position":"fixed","top":"0","z-index":"1","left":"0","width":"100%","height":"6%","padding-bottom":"1%"}
    
)

sidebar = html.Div([
    html.Hr(),
    dbc.Nav([
        dbc.NavLink('Home', href='/Home', active='exact'),
        html.Br(),
        dbc.NavLink('Customers', href='/Customers', active='exact'),
        html.Br(),
        dbc.NavLink('Scenarios', href='/Scenarios', active='exact'),
        html.Br(),
        dbc.NavLink('About', href='/About', active='exact'),
        
    ],
    vertical=True,
    pills=True,
    ),
], style=sidebar_style,)

content = html.Div(id="page-content", style=content_style)

#https://ak.picdn.net/shutterstock/videos/22397962/thumb/11.jpg
app.layout = html.Div([dcc.Location(id="url"), sidebar,navbar, content], 
style={"background-image": 'url("https://images.unsplash.com/photo-1474487548417-781cb71495f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1284&q=80")',
"background-position":"center", "background-attachment":"fixed",
'background-repeat': 'no-repeat',"background-size":"cover","width":"100%","height":"100%",
"overflow-x":"hidden","overflow-y":"hidden"

})
#,"position": "absolute", "top": "0", "left": "0",



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/Home":
        return html.Div( html.H1("The homepage is under construction!",style={"text-align":"center",'color':'white'}),style={"padding-top":"25%","padding-bottom":"50%", "height":"auto","width":"auto"})
    elif pathname == "/Customers":
        return html.Div( html.H1("This menu item is under construction!",style={"text-align":"center"}),style={"padding-top":"25%","padding-bottom":"50%", "height":"auto","width":"auto"})
    elif  "/Scenarios" in pathname:
        return html.Div( html.H1("This menu item is under construction!",style={"text-align":"center"}),style={"padding-top":"25%","padding-bottom":"50%", "height":"auto","width":"auto"})
    elif pathname == "/About":
        return  html.Div( html.H1("about page is under construction!",style={"text-align":"center"}),style={"padding-top":"25%","padding-bottom":"50%", "height":"auto","width":"auto"})
    # If the user tries to reach a different page, return a 404 message
    return html.Div( html.H1("The homepage is under construction!",style={"text-align":"center"}),style={"padding-top":"25%","padding-bottom":"50%", "height":"auto","width":"auto"})



if __name__ == "__main__":
    app.run_server(port=8881,debug = True)
