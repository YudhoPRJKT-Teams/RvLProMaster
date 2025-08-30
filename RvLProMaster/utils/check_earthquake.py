import aiohttp
from .create_log import CreateLog

class CheckEarthquake:
  def __init__(self) -> None:
    self.api_uri = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
    self.shakemap_uri = "https://data.bmkg.go.id/DataMKG/TEWS"
  async def Fetch(self):
    """Fetch Data Earth From BMKG"""
    async with aiohttp.ClientSession() as session:
      async with session.get(self.api_uri) as client:
        if client.status == 200:
          response = await client.json()
          primary_data = response["Infogempa"]["gempa"]
          # Obtain data from BMKG
          self.earthquake_date = primary_data.get("Tanggal")
          self.earthquake_time = primary_data.get("Jam")
          self.earthquake_coordinates = primary_data.get("Coordinates")
          self.earthquake_latitude = primary_data.get("Lintang")
          self.earthquake_longitude = primary_data.get("Bujur")
          self.earthquake_magnitude = primary_data.get("Magnitude")
          self.earthquake_depth = primary_data.get("Kedalaman")
          self.earthquake_region = primary_data.get("Wilayah")
          self.earthquake_potential = primary_data.get("Potensi")
          self.earthquake_felt = primary_data.get("Dirasakan")
          self.earthquake_shakemap = f"{self.shakemap_uri}/{primary_data.get('Shakemap')}"
        else:
          CreateLog("ERROR", f"Unable To Fetch Data From: {self.api_uri}")
        return self