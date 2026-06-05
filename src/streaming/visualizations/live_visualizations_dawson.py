"""src/streaming/visualizations/live_visualizations_dawson.py.

Project-specific live visualization functions used by the Kafka consumer.

This module creates a live line chart of sale total by message.
The chart opens in a window while the consumer is running and updates
as each message is consumed.
"""

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt

__all__ = [
    "close_live_chart",
    "init_live_chart",
    "save_live_chart",
    "update_live_chart",
]


def init_live_chart() -> tuple[Any, Any, list[int], list[float]]:
    """Create and show an empty live chart.

    Returns:
        A tuple of (figure, axis, x_values, y_values).
    """
    plt.ion()
    figure, axis = plt.subplots(figsize=(9, 5))

    x_values: list[int] = []
    y_values: list[float] = []

    # Apply a consistent color palette for better readability.
    figure.patch.set_facecolor("#F7F9FC")
    axis.set_facecolor("#EEF3FA")
    axis.set_title(
        "Sales Total by Message", color="#1F2A44", fontsize=13, fontweight="bold"
    )
    axis.set_xlabel("Message", color="#1F2A44")
    axis.set_ylabel("Sale Total ($)", color="#1F2A44")
    axis.tick_params(colors="#1F2A44")

    figure.show()
    figure.canvas.draw()
    figure.canvas.flush_events()

    return figure, axis, x_values, y_values


def update_live_chart(
    *,
    figure: Any,
    axis: Any,
    x_values: list[int],
    y_values: list[float],
    message: dict[str, Any],
) -> None:
    """Update the live chart with one consumed message."""
    new_x = int(message["_kafka_offset"])
    x_values.append(new_x)

    new_y = float(message["total"])
    y_values.append(new_y)

    axis.clear()
    axis.set_facecolor("#EEF3FA")
    axis.plot(
        x_values,
        y_values,
        marker="o",
        color="#1D4ED8",
        linewidth=2.2,
        markersize=6,
        markerfacecolor="#F97316",
        markeredgecolor="#C2410C",
    )

    axis.set_title(
        "Sales Total by Message", color="#1F2A44", fontsize=13, fontweight="bold"
    )
    axis.set_xlabel("Message", color="#1F2A44")
    axis.set_ylabel("Sale Total ($)", color="#1F2A44")
    axis.tick_params(colors="#1F2A44")
    axis.grid(True, color="#B6C2D9", linestyle="--", alpha=0.7)

    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.pause(0.05)


def save_live_chart(*, figure: Any, chart_path: Path) -> None:
    """Save the final live chart to an image file."""
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(chart_path, bbox_inches="tight")


def close_live_chart() -> None:
    """Turn off interactive chart mode."""
    plt.ioff()
