function initViz() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/views/426DataTest/HospitalBedsMap?:retry=yes&:display_count=y&:origin=viz_share_link";
    //https://public.tableau.com/views/DeathRatesPopulationDemographics/DeathRatesCensus?:display_count=y&publish=yes&:origin=viz_share_link
    //https://public.tableau.com/views/426DataTest/HospitalBedsMap?:retry=yes&:display_count=y&:origin=viz_share_link
    var viz = new tableau.Viz(containerDiv, url);
}   

function initViz2() {
    var containerDiv = document.getElementById("vizContainer2"),
    url = "https://public.tableau.com/views/testing4_15880608226550/DeathRatesCensus?:display_count=y&publish=yes&:origin=viz_share_link";
    //https://public.tableau.com/views/DeathRatesPopulationDemographics/DeathRatesCensus?:display_count=y&publish=yes&:origin=viz_share_link
    //https://public.tableau.com/views/426DataTest/HospitalBedsMap?:retry=yes&:display_count=y&:origin=viz_share_link
    //https://public.tableau.com/views/DeathRatesPopulationDemographics/DeathRatesCensus?:display_count=y&publish=yes&:origin=viz_share_link
    //https://public.tableau.com/views/testing4_15880608226550/DeathRatesCensus?:display_count=y&publish=yes&:origin=viz_share_link
    var viz = new tableau.Viz(containerDiv, url);
}   


