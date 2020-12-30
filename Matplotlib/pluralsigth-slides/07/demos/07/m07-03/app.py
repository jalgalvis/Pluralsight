from io import BytesIO
import base64

from flask import Flask, render_template, request

import numpy as np
import matplotlib.pyplot as plt

import helper

app = Flask(__name__)

@app.route('/')
def index():
    year = int(request.args.get('year', 2013))
    heights = [month[1] for month in helper.precip_sums_for_year(year=year)]
    plt.bar(np.arange(len(heights)), heights)
    plt.xticks(ticks=np.arange(len(helper.MONTHS)), labels=helper.MONTHS)
    plt.title('Monthly Total Precipitation for {}'.format(year))

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    b64data = base64.b64encode(buf.getvalue()).decode()

    plt.close()

    return render_template('index.html', img=b64data)

if __name__ == '__main__':
    app.run(debug=True)
