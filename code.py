def counter_app():
    count,change_count = React.useState(0)

    def increment():
        change_count(count+1)

    return React.createElement('button',{'onClick':increment},count)


def render():
    ReactDOM.render(
        React.createElement(counter_app,None),
        document.getElementById("root")
    )


document.addEventListener('DOMContentLoaded',render)
