import * as d3 from "d3";
import './Graph.css'

const BLUE = "#139FFD";
const RED = "#e9382e";

function shadeColor(color, percent) {

    var R = parseInt(color.substring(1,3),16);
    var G = parseInt(color.substring(3,5),16);
    var B = parseInt(color.substring(5,7),16);

    R = parseInt(R * (100 + percent) / 100);
    G = parseInt(G * (100 + percent) / 100);
    B = parseInt(B * (100 + percent) / 100);

    R = (R<255)?R:255;  
    G = (G<255)?G:255;  
    B = (B<255)?B:255;  

    var RR = ((R.toString(16).length==1)?"0"+R.toString(16):R.toString(16));
    var GG = ((G.toString(16).length==1)?"0"+G.toString(16):G.toString(16));
    var BB = ((B.toString(16).length==1)?"0"+B.toString(16):B.toString(16));

    return "#"+RR+GG+BB;
}

export function runForceGraph(container, data) {
    const height = 450;
    const width = 1000;

    const edges = data.edges.map(d => Object.create(d));
    const nodes = data.nodes.map(d => Object.create(d));

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(edges).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("charge", d3.forceManyBody().strength(-800));

    const color = (d) => {
        if (d.id === "Root"){
            return RED
        }
        return shadeColor(BLUE, (2020 - d.year) * -3.25);
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
        .on("dblclick", dblclick)

    function mouseover() {
        let item = d3.select(this)
        item.raise();
        d3.select(this).select("circle").transition()
            .attr("r", 10)
            .style("fill", RED);
        d3.select(this).select("text").transition()
            .style("font", "16px Roboto")
            .attr('x', 16)
            .attr('y', 6)
            .style('fill','#000000');
    }

    function mouseout() {
        let data = d3.select(this).datum();
        if (data.id === "Root"){
            d3.select(this).select("circle").transition()
            .attr("r", 5)
            .style("fill", RED);
        }
        else{
        d3.select(this).select("circle").transition()
            .attr("r", 5)
            .style("fill", shadeColor(BLUE, (2020 - data.year) * -3.25));
        }
        d3.select(this).select("text").transition()
            .style("font", "8px Roboto")
            .attr('x', 6)
            .attr('y', 3)
            .style('fill', '#B1bbc6');
    }

    function dblclick() {
        let data = d3.select(this).datum();
        window.open(data.link);
    }

    node.append('circle')
        .attr("r", 5)
        .attr("fill", d => color(d))

    node.append("text")
        .text(function (d) {
            return (d.id + ', ' + d.year);
        })
        .style('fill', '#B1bbc6')
        .style('font', '8px Roboto')
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

