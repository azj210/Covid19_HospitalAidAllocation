function initViz() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/views/426DataTest/HospitalBedsMap?:retry=yes&:display_count=y&:origin=viz_share_link";

    var viz = new tableau.Viz(containerDiv, url);
}   


