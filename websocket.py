import websockets
import asyncio
from typing import Any
from data import DataProcessor

async def stream_data(symbol: str, interval: str, alert_threshold: float,
                     chart_placeholder: Any, alert_placeholder: Any) -> None:
    url = f"wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}"
    processor = DataProcessor()
    
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            processor.process_data(msg, symbol, alert_threshold,
                                chart_placeholder, alert_placeholder)

def start_streaming(symbol: str, interval: str, alert_threshold: float,
                   chart_placeholder: Any, alert_placeholder: Any) -> None:
    asyncio.run(stream_data(symbol, interval, alert_threshold,
                          chart_placeholder, alert_placeholder))