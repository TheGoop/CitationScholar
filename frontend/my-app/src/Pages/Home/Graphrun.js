import * as d3 from "d3";
import './Graph.css'


export function runForceGraph(container, data) {
    const height = 450;
    const width = 1000;

    const edges = data.edges.map(d => Object.create(d));
    const nodes = data.nodes.map(d => Object.create(d));

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(edges).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
    const color = () => {
        // const scale = d3.scaleOrdinal(d3.schemeCategory10);
        // return d => scale(d.group);
        return "#139FFD";
    }

    //GROUP IS UNNECESSARY

    const drag = (simulation) => {

        function dragstarted(event) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            event.subject.fx = event.subject.x;
            event.subject.fy = event.subject.y;
        }

        function dragged(event) {
            event.subject.fx = event.x;
            event.subject.fy = event.y;
        }

        function dragended(event) {
            if (!event.active) simulation.alphaTarget(0);
            event.subject.fx = null;
            event.subject.fy = null;
        }

        return d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended);
    }

    const svg = d3.select(container)
        .append("svg")
        .attr("viewBox", [0, 0, width, height]);

    const link = svg.append("g")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(edges)
        .join("line")
        .attr("stroke-width", d => Math.sqrt(d.value));

    const node = svg.append("g")
        .selectAll(".node")
        .data(nodes)
        .join("g")
        .attr('class', 'node')
        .call(drag(simulation))
        .on("mouseover", mouseover)
        .on("mouseout", mouseout)

    function mouseover() {
        d3.select(this).select("circle").transition()
            .attr("r", 10)
            .style("fill", "#cf362e");
        d3.select(this).select("text").transition()
            .style("font", "30px sans-serif")
            .attr('x', 16)
            .attr('y', 6);
    }

    function mouseout() {
        d3.select(this).select("circle").transition()
            .attr("r", 5)
            .style("fill", "#3584d7");
        d3.select(this).select("text").transition()
            .style("font", "12px sans-serif")
            .attr('x', 6)
            .attr('y', 3);
    }

    function click() {
        d3.select(this).select("circle").transition()
            .duration(1)
            .attr("r", 16)
            .style("fill", "lightsteelblue");
    }

    node.append('circle')
        .attr("r", 5)
        .attr("fill", "#3584d7")

    node.append("text")
        .text(function (d) {
            return d.id;
        })
        .style('fill', '#000')
        .style('font-size', '12px')
        .attr('x', 6)
        .attr('y', 3);

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("transform", d => `translate(${d.x}, ${d.y})`);
    });

    return svg.node();
}