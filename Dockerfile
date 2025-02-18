FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY scripts ./scripts

# Make sure all scripts are executable (optional step if required)
RUN chmod +x ./scripts/*

# Run the scripts one by one
CMD python script1.py && python script2.py && python script3.py
