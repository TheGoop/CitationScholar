import React from "react";
import { runForceGraph } from "./Graphrun";
import "./Graph.css";

export function ForceGraph({ data }) {
  console.log(data)
  const containerRef = React.useRef(null);

  React.useEffect(() => {
    let destroyFn;

    if (containerRef.current) {
      const { destroy } = runForceGraph(containerRef.current, data);
      destroyFn = destroy;
    }

    return destroyFn;
  }, []);

  return <div ref={containerRef} id="graphwrap" />;
}