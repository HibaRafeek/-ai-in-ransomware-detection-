from flask import Flask, render_template_string, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


def train_model():
    data = pd.read_csv("ransomware (1).csv")
    X = data[["file_access", "file_modify", "cpu_usage", "disk_usage"]]
    y = data["label"]

    model = LogisticRegression()
    model.fit(X, y)
    return model


model = train_model()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Ransomware Behavior Detector</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { 
            background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
            background-attachment: fixed;
            color: #00ff00; 
            position: relative;
            min-height: 100vh;
            font-family: 'Courier New', monospace;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        }
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                repeating-linear-gradient(
                    0deg,
                    rgba(0, 255, 0, 0.02),
                    rgba(0, 255, 0, 0.02) 1px,
                    transparent 1px,
                    transparent 2px
                );
            z-index: 1;
            pointer-events: none;
            animation: flicker 0.15s infinite;
        }
        @keyframes flicker {
            0% { opacity: 0.97; }
            50% { opacity: 1; }
            100% { opacity: 0.97; }
        }
        .container { position: relative; z-index: 2; }
        .card { 
            background: rgba(20, 20, 35, 0.95); 
            border-radius: 0.5rem; 
            border: 2px solid #00ff00;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.4), inset 0 0 20px rgba(0, 255, 0, 0.1);
        }
        .form-label { 
            font-weight: 500; 
            color: #00ff00 !important;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
        }
        .text-secondary { 
            color: #00cc00 !important; 
            font-size: 0.85rem;
        }
        .form-control {
            background: rgba(10, 10, 25, 0.9);
            border: 1px solid #00ff00;
            color: #00ff00;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
        }
        .form-control:focus {
            background: rgba(10, 10, 25, 0.9);
            border-color: #00ff00;
            color: #00ff00;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
        }
        .form-text { 
            color: #00cc00 !important;
        }
        .result-safe { 
            color: #00ff00; 
            font-weight: 700;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
        }
        .result-danger { 
            color: #ff0000; 
            font-weight: 700;
            text-shadow: 0 0 10px rgba(255, 0, 0, 0.8);
        }
        h1 { 
            color: #00ff00 !important;
            text-shadow: 0 0 20px rgba(0, 255, 0, 0.6);
            font-family: 'Courier New', monospace;
            letter-spacing: 2px;
        }
        .btn-primary {
            background: #00ff00;
            border: 2px solid #00ff00;
            color: #000000;
            font-weight: bold;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
            transition: all 0.3s;
        }
        .btn-primary:hover {
            background: #00cc00;
            border-color: #00cc00;
            box-shadow: 0 0 25px rgba(0, 255, 0, 0.8);
        }
        hr {
            border-color: rgba(0, 255, 0, 0.3);
        }
    </style>
</head>
<body>
<div class="container py-5">
  <div class="row justify-content-center">
    <div class="col-lg-6">
      <div class="text-center mb-4">
        <h1 class="fw-bold">Ransomware Behavior Detector</h1>
        <p class="text-secondary">Enter behavior values to check if it looks like ransomware.</p>
      </div>
      <div class="card p-4 shadow">
        <form method="post">
          <div class="mb-3">
            <label class="form-label">File Access Count</label>
            <input type="number" class="form-control" name="file_access" required min="0" step="1" value="{{ file_access or '' }}">
            <div class="form-text text-secondary">How many files the program is opening.</div>
          </div>
          <div class="mb-3">
            <label class="form-label">File Modify Count</label>
            <input type="number" class="form-control" name="file_modify" required min="0" step="1" value="{{ file_modify or '' }}">
            <div class="form-text text-secondary">How many files the program is changing.</div>
          </div>
          <div class="mb-3">
            <label class="form-label">CPU Usage (%)</label>
            <input type="number" class="form-control" name="cpu_usage" required min="0" max="100" step="1" value="{{ cpu_usage or '' }}">
            <div class="form-text text-secondary">Approximate CPU usage.</div>
          </div>
          <div class="mb-3">
            <label class="form-label">Disk Usage (%)</label>
            <input type="number" class="form-control" name="disk_usage" required min="0" max="100" step="1" value="{{ disk_usage or '' }}">
            <div class="form-text text-secondary">Approximate disk (read/write) activity.</div>
          </div>
          <button type="submit" class="btn btn-primary w-100 fw-semibold">Check Behavior</button>
        </form>

        {% if prediction is not none %}
          <hr class="my-4" />
          <div class="text-center">
            {% if prediction == 1 %}
              <div class="result-danger fs-4">⚠️ Ransomware Detected</div>
              <p class="text-secondary mt-2">Behavior looks similar to ransomware in the training data.</p>
            {% else %}
              <div class="result-safe fs-4">✅ System Safe</div>
              <p class="text-secondary mt-2">Behavior looks like normal software from the training data.</p>
            {% endif %}
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""



@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    file_access = file_modify = cpu_usage = disk_usage = None

    if request.method == "POST":
        try:
            file_access = int(request.form.get("file_access", 0))
            file_modify = int(request.form.get("file_modify", 0))
            cpu_usage = int(request.form.get("cpu_usage", 0))
            disk_usage = int(request.form.get("disk_usage", 0))

            sample = [[file_access, file_modify, cpu_usage, disk_usage]]
            result = model.predict(sample)
            prediction = int(result[0])
        except Exception:
            prediction = None

    return render_template_string(
        HTML_TEMPLATE,
        prediction=prediction,
        file_access=file_access,
        file_modify=file_modify,
        cpu_usage=cpu_usage,
        disk_usage=disk_usage,
    )


if __name__ == "__main__":
    app.run(debug=True)

