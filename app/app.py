from flask import *
import random
import sqlite3


app = Flask(__name__)

fChar = ['\t', '\t(', ') ', '\n \t \t', '\n \t', '    ', ' ', ', ', ' ', ' ', ' ', '... ', '\n']
def randPunct():
    return random.randrange(0,len(fChar))

@app.route('/send', methods=['GET', 'POST'])

def send():
    sql = sqlite3.connect('poems.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS poem(textToBreak TEXT)')
    if request.method == 'POST':
        textToBreak = request.form['textToBreak']
        i = 0
        b = {}
        newT = {}
        newerT = []
        t = textToBreak.split()
        for each in t:
            b[i] = fChar[randPunct()]
            newT[i] = each + b[i]
            i += 1
        for each in newT:
            newerT += newT[each]
        together = ''.join(newerT)
        cur.execute('SELECT * FROM poem')
        cur.execute('INSERT INTO poem VALUES(?)', [together])
        sql.commit()    
        return render_template('poemResult.html', textToBreak = together)
    else:
        cur.execute('SELECT * FROM poem')
        uncoded = cur.fetchall() #        allOfThem1 = [[s.encode('utf8') for s in t] for t in uncoded]
        j = ""
        b = []
        k = ""
        for each in reversed(uncoded):
            b = each
            for each1 in b:
                k = each1 + "<br><br>"
                j += ''.join(k)
        return render_template('index.html', workThingy1 = j)


if __name__ == "__main__":
    app.run()
