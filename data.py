import pandas as pd
import plotly.graph_objects as go
import json
from typing import List, Dict, Any
from mails import handle_send_email


class DataProcessor:
    def __init__(self):
        self.data: List[Dict[str, Any]] = []
        self.alert_triggered = False
    
    def process_data(self, msg: str, symbol: str, alert_threshold: float,
                    chart_placeholder: Any, alert_placeholder: Any) -> None:
        # Parse incoming websocket message
        parsed = json.loads(msg)
        kline = parsed['k']
        
        
        # Extract time and price
        time = pd.to_datetime(kline['t'], unit='ms')
        price = float(kline['c'])
        
        # Update data list
        self.data.append({'time': time, 'price': price})
        if len(self.data) > 100:  # Keep last 100 points
            self.data.pop(0)
        
        # Create dataframe and update chart
        df = pd.DataFrame(self.data)
        
        fig = self.plot_graph(df, symbol)
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        # Check for significant price changes
        self._check_alerts(df, alert_threshold, alert_placeholder)
    
    def _check_alerts(self, df: pd.DataFrame, alert_threshold: float,
                     alert_placeholder: Any) -> None:
        if len(df) > 1:
            change = (df['price'].iloc[-1] - df['price'].iloc[-2]) / df['price'].iloc[-2] * 100
            if abs(change) >= alert_threshold and not self.alert_triggered:
                alert_placeholder.warning(f'Changement Significatif: {change:.2f}%')
                data = {
                    "objet" : 'Changement Significatif',
                    "contenue" : f'Changement Significatif: {change:.2f}%'
                    }

                handle_send_email(data)
                self.alert_triggered = True
            elif abs(change) < alert_threshold:
                self.alert_triggered = False
    
    def plot_graph(self, df: pd.DataFrame, symbol: str):
        fig = go.Figure()
        
        fig.add_trace(
            go.Scatter(
                x=df['time'],
                y=df['price'],
                mode='lines',
                line=dict(
                    shape='spline',
                    width=2,
                    color='rgb(41, 128, 185)'  # Ethereum blue color
                ),
                fill='tozeroy',
                fillcolor='rgba(41, 128, 185, 0.1)'
            )
        )
        
        # Update layout
        fig.update_layout(
            title=f'Prix en Temps Réel: {symbol.upper()}',
            xaxis_title='Time',
            yaxis_title='Price (USDT)',
            showlegend=False,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(230, 230, 230, 0.8)',
                zeroline=False
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(230, 230, 230, 0.8)',
                zeroline=False
            )
        )
        
        return fig
