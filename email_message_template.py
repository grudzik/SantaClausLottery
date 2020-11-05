from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_email_for(to_whom, to_whom_mail, drawn_person, money_limit = 200, sex="male", from_whom="Swiety Mikolaj"):
    msg = MIMEMultipart('alternative')
    if sex == "male":
        msg['Subject'] = f"Drogi Święty Mikołaju... Mężny człeku zwany {to_whom}!"
    else:
        msg['Subject'] = f"Droga Święta Pani Mikołaj... Piękna niewiasto o imieniu {to_whom}!"
    msg['From'] = from_whom
    msg['To'] = to_whom_mail

    text = f"""
    """

    STYLE = """
    h1 {
          color: red;
          font-size: 200%;
        }
    h2 {
    font-size: 150%;
          color: black;          
        }
                h6 {
          color: orange;
        }
    h6 {
          color: green;
        }
    """

    html = rf"""
    <html>
    <head>
    <style>
        {STYLE}
    </style>
    </head>
    <body>        
        <p>W tej ciężkiej chwili, gdy nawet śnieg nie pada; gdy jest mokro i często smutno, przychodzę ja! 
        Właściwie mnie nie znasz, bo jestem programem komputerowym, ale to nie znaczy, że nie możemy się poznać. Lubię poznawać nowych ludzi, a szczególnie takich szczodrych, bogatych...
        W końcu, dzięki Tobie nie będę musiał tak nadwyrężać sakiewki, bo wspomożesz mnie i kupisz prezent temu Nicponiowi.
        <br>
        Nie będę ukrywał, że pokładam w Tobie nadzieję, że będzie to coś fajnego... Nie będę też ukrywał, że grono Mikołajów, to Elita - więc zwyczajnie mnie nie zawiedź (:.
            <br>
               __<br>
            .-'  |<br>
           /   <\|<br>
          /     \'<br>
          |_.- o-o<br>
          / C  -._)\<br>
         /',        |<br>
        |   `-,_,__,'<br>
        (,,)====[_]=|<br>
          '.   ____/<br>
           | -|-|_<br>
           |____)_)<br>
    </p>
    <p>
    <ul>
        Właściwie przechodząc do sedna, masz kupić prezent, gdzie:        
        <li>limit to jest <u>{money_limit} zł<ul>,</li>
        <li>osobą, którą wylosowałeś, drogi człowieku, to ...</li>
    </ul>
    <br>
        <center>
        OSOBA KTÓRĄ WYLOSOWAŁEŚ TO... !!!
        <br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br>
        OSOBA KTÓRĄ WYLOSOWAŁEŚ TO... !!! !!!
        <br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br><br>.<br>            
        <h2> OSOBA KTÓRĄ WYLOSOWAŁEŚ TO !!!</h2>
        <h1><u> {drawn_person} </u> </h1>
        <h2>Gratulacje !!!</h2>
        <h3> ho </h2>
        <h3> ho ho ho </h3>
        <h3> ho </h4>
        <h6> ho</h6>
        <h6> ho ho</h6>
        <h6> ho ho ho</h6>
        <h6> ho ho ho ho </h6>
        <h6> ho ho ho ho ho </h6>
        <h6> ho ho ho ho ho ho </h6>
        <h6> ho ho ho ho ho ho ho </h6>
        <h6> ho ho ho ho ho ho ho ho </h6>
        <h6> ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho ho ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho ho ho ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho ho ho ho ho ho ho ho ho ho ho ho ho</h6>
        <h6> ho ho</h6>
        <h6> ho ho</h6>
        <h1> Wesołych Świąt {to_whom} !!! </h1>        
    </center>
    </body>
    </html>
    """
    part1 = MIMEText(text, "plain", "utf-8")
    part2 = MIMEText(html, "html", "utf-8")

    msg.attach(part1)
    msg.attach(part2)

    return msg
