import socketio

# Exchange namespaces
WAZIRX_NAMESPACE = '/wazirx'
COINSWITCHX_NAMESPACE = '/coinswitchx'
WAZIRX = 'wazirx'
COINSWITCHX = 'coinswitch'

# Base URLs
BASE_URL_PROD = 'wss://ws.coinswitch.co'

# Ticker stream event names
FETCH_ORDER_BOOK_EVENT = 'FETCH_ORDER_BOOK_CS_PRO'
FETCH_TRADES_EVENT = 'FETCH_TRADES_CS_PRO'
FETCH_TICKER_INFO_EVENT = 'FETCH_TICKER_INFO_CS_PRO'
sio = socketio.Client()


def handle_ticker_event(event, data):
    print(f'Ticker Event: {event}')
    print(data)


@sio.event
def connect():
    print('Connected to the server')


@sio.event
def connect_error(data):

    print(f'Connection with the server failed: {data}')
    reconnect()


@sio.event
def disconnect():
    print("Disconnected from the server")
    reconnect()


@sio.on('FETCH_TICKER_INFO_CS_PRO', namespace=WAZIRX_NAMESPACE)
def on_message_wazirx_ticker(data):
    print(data)


@sio.on('FETCH_TRADES_CS_PRO', namespace=WAZIRX_NAMESPACE)
def on_message_wazirx_trades(data):
    print(data)


@sio.on('FETCH_ORDER_BOOK_CS_PRO', namespace=WAZIRX_NAMESPACE)
def on_message_wazirx_order_book(data):
    print(data)


@sio.on('FETCH_TICKER_INFO_CS_PRO', namespace=COINSWITCHX_NAMESPACE)
def on_message_coinswitchx_ticker(data):
    print(data)


@sio.on('FETCH_TRADES_CS_PRO', namespace=COINSWITCHX_NAMESPACE)
def on_message_coinswitchx_trades(data):
 
    print(data)


@sio.on('FETCH_ORDER_BOOK_CS_PRO', namespace=COINSWITCHX_NAMESPACE)
def on_message_coinswitchx_order_book(data):
    print(data)


@sio.on('*')
def catch_all(event, data):
    print(event, data)


def connect_to_ticker_server(exchange, base_url):
    namespace = WAZIRX_NAMESPACE if exchange == WAZIRX else COINSWITCHX_NAMESPACE
    url = base_url
    
    try:
        sio.connect(url=url, namespaces=[namespace], transports='websocket',socketio_path='/pro/realtime-rates-socket', wait=True, wait_timeout=3600)
        pair = "BTC,INR"
        subscribe_data = {
            'event': 'subscribe',
            'currencies': [pair]
        }
        sio.emit(FETCH_TICKER_INFO_EVENT, subscribe_data, namespace=namespace)
    except Exception as e:
        print(e)

def connect_to_trade_server(exchange, base_url):
    namespace = WAZIRX_NAMESPACE if exchange == WAZIRX else COINSWITCHX_NAMESPACE
    url = base_url
    try:
        sio.connect(url=url, namespaces=[namespace], transports='websocket',
                    socketio_path='/pro/realtime-rates-socket', wait=True, wait_timeout=3600)
        pair = "BTC,INR"
        subscribe_data = {
            'event': 'subscribe',
            'pair': pair
        }
    except Exception as e:
        print(e)
    sio.emit(FETCH_TRADES_EVENT, subscribe_data, namespace=namespace)


def connect_to_order_book_server(exchange, base_url):
    namespace = WAZIRX_NAMESPACE if exchange == WAZIRX else COINSWITCHX_NAMESPACE
    url1 = base_url
    pair = "BTC,INR"
    sio.connect(url=url1, namespaces=[namespace], transports='websocket',socketio_path='/pro/realtime-rates-socket/spot/coinswitchx', wait=True, wait_timeout=3600)
    subscribe_data = {
        'event': 'subscribe',
        'pair': pair
    }
    sio.emit(FETCH_ORDER_BOOK_EVENT, subscribe_data, namespace=namespace)


def reconnect():
    print("Reconnecting...")
    connect_to_order_book_server(COINSWITCHX, BASE_URL_PROD)


connect_to_order_book_server(COINSWITCHX, BASE_URL_PROD)

