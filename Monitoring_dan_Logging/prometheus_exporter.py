from prometheus_client import start_http_server, Summary, Counter, Gauge
import time

# Contoh metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Number of requests processed')
MODEL_STATUS = Gauge('model_status', 'Status of the model')

@REQUEST_TIME.time()
def process_request():
    time.sleep(0.5)  # simulasi kerja

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus scrape endpoint
    MODEL_STATUS.set(1)  # misal model aktif
    while True:
        REQUEST_COUNT.inc()
        process_request()
