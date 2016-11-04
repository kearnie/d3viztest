Table allRidesTable;

int stationRideCounts[];

void setup() {

  int nStations = stations.length;
  stationRideCounts = new int[nStations]; 
  for (int s=0; s<nStations; s++) {
    stationRideCounts[s] = 0; // initialized to zero yo
  }


  allRidesTable = loadTable("HealthyRideRentals2015Q3.csv", "header"); 
  // Trip id,Starttime,Stoptime,Bikeid,Tripduration,From station id,From station name,To station id,To station name,Usertype

  int nRows = allRidesTable.getRowCount(); 
  for (int i=0; i<nRows; i++) {
    TableRow ithRow = allRidesTable.getRow(i); 
    String ithFromStationName = ithRow.getString("From station name");
    String ithToStationName = ithRow.getString("To station name"); 

    for (int s=0; s<nStations; s++) {
      if (ithFromStationName.contains(stations[s])){
        stationRideCounts[s] = stationRideCounts[s] + 1;
      }
      if (ithToStationName.contains(stations[s])){
        stationRideCounts[s]++;
      }
    }
  }

  println("Station" + "\t" + "nRides"); 
  for (int s=0; s<nStations; s++) {
    println (stations[s] + "\t" + stationRideCounts[s]);
  }
}