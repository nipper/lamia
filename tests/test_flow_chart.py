import pytest

from lamia.flowchart.shapes import (
    FlowChartEdge,
    FlowChartRenderer,
    FlowChartEdgeRenderer,
    LineStyle,
)
from lamia.base import BaseNode
from itertools import cycle


@pytest.fixture
def edge():
    return FlowChartEdge(start=BaseNode(id="A"), end=BaseNode(id="B"))


@pytest.mark.parametrize(
    "direction,expected_result", [("uni", ""), ("multi", "<"), ("none", "")]
)
def test_edge_render_start_arrow(edge, direction, expected_result):

    edge.direction = direction
    renderer = FlowChartEdgeRenderer(edge)

    assert renderer._render_start_arrow() == expected_result


@pytest.mark.parametrize(
    "direction,expected_result", [("uni", ">"), ("multi", ">"), ("none", "")]
)
def test_edge_render_end_arrow(edge, direction, expected_result):

    edge.direction = direction
    renderer = FlowChartEdgeRenderer(edge)

    assert renderer._render_end_arrow() == expected_result


@pytest.mark.parametrize(
    "style_flag,expected_output",
    [
        (LineStyle.NORMAL, "A(A)-->B(B)"),
        (LineStyle.THICK, "A(A)==>B(B)"),
        (LineStyle.DOTTED, "A(A)-.->B(B)"),
    ],
)
def test_edge_styles(edge, style_flag, expected_output):
    edge.line_style = style_flag

    assert edge.render() == expected_output


@pytest.mark.parametrize(
    "length,line_style,default_length",
    zip(
        range(1, 10),
        cycle([LineStyle.DOTTED, LineStyle.THICK, LineStyle.NORMAL]),
        cycle([11, 10, 10]),
    ),
)
def test_line_length(edge, length, line_style, default_length):

    edge.length = length
    edge.line_style = line_style

    assert len(edge.render()) == default_length + length
